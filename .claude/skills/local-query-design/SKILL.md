---
name: local-query-design
description: How the Caffeine local-data engineer writes every on-device query once as annotated SQLite SQL (the /data:write-query method), proves it against the golden fixture with scripts/data/verify_queries.py, then maps it to a Room @Query and a SwiftData FetchDescriptor + #Predicate with the same reduce step. Money is never summed in SQL. Writes docs/data-model/<feature>-queries.md and sql/<feature>-queries.sql. Loaded by local-data-engineer; read by backend-lead and both developers.
---

# Local Query Design (write once, prove, map twice)

Method adapted from `/data:write-query` (if the `data:write-query` or `data:sql-queries` plugin skill is available, you may load it with the Skill tool; this file wins where they differ). Dialect is always **SQLite** — Room runs on it, and the script runs it, so a query that passes here is the real Room query.

## 1. Understand each read the plan needs
For every screen figure or list in the plan's screen map, write one line before any SQL:
**output columns · filters · aggregation · joins · ordering · limit/paging · which screen and AC.**
One query per figure family (e.g. `spent_by_category` serves the Analytics list and the donut). Reuse an existing query before adding one.

## 2. Write the SQL (rules, each checked)
- Name the columns. Never `SELECT *`.
- **No `SUM`/`AVG`/`TOTAL` on money.** SQLite would turn decimal text into a binary float. SQL filters, joins and orders rows; the **reduce step** (sum, sum by key) runs in the repository with `Decimal` / `BigDecimal`, and in the script with Python `Decimal`. `COUNT(*)` is fine. Signs can be produced as text: `CASE t.type WHEN 'expense' THEN '-' || t.amount ELSE t.amount END AS signedAmount`.
- Filter early on `localDate` (never on `occurredAt` with time-zone maths). Ranges are inclusive: `localDate BETWEEN :start AND :end`, cycle dates come from the domain cycle function, not from SQL.
- Transfers and card payments are excluded from In / Out / Net and budgets with an explicit `type IN ('income','expense')` or `type = 'expense'`.
- Joins: at most 2 per query, `JOIN` (inner) unless a missing parent is a real case. One `UNION ALL` allowed for ledger legs (balances, transfers). CTEs only for readability, one per step, named for what they hold (`movements`).
- Params are named `:start`, `:end`, `:asOf`, `:accountId` — the same names in Room.
- Lists that grow (History) page with `ORDER BY localDate DESC, occurredAt DESC, id DESC LIMIT :limit` and a keyset (`WHERE (localDate, occurredAt, id) < (:lastDate, :lastAt, :lastId)`), not OFFSET.
- A comment says **why** for anything non-obvious.

## 3. Annotate and prove (the mechanical gate)
Put every query in `docs/data-model/sql/<feature>-queries.sql`:
```sql
-- name: spent_by_category
-- purpose: Analytics Spending list (plan AC-xx). Golden §3.
-- params: {"start": "2026-10-25", "end": "2026-11-24"}
-- expect: sum(amount) by categoryName = {"Food & Drink": "12115", "Transport": "1547"}
-- expect: count = 14
-- allow-scan: <reason, only when a full scan is the point>
SELECT c.name AS categoryName, t.amount FROM transactions t JOIN categories c ON c.id = t.categoryId
WHERE t.type = 'expense' AND t.localDate BETWEEN :start AND :end ORDER BY c.sortOrder;
```
Expected values come from `docs/plan/golden-sample-data.md` (never invented). If the feature needs rows the golden set lacks, add them to `docs/data-model/sql/fixtures/golden.sql` **and** list them in `<feature>-queries.md` so ba can add them to the golden sheet.

Run:
```
python3 -I scripts/data/verify_queries.py docs/data-model/sql/<all>-schema.sql docs/data-model/sql/fixtures/golden.sql docs/data-model/sql/<feature>-queries.sql
```
It fails on: SQL errors, a wrong count or sum, `SELECT *`, SUM/AVG/TOTAL, REAL/FLOAT/DOUBLE columns, and a full SCAN of `transactions` without `-- allow-scan:`. Exit 0 is required; paste the PASS lines as evidence.

## 4. Map to both platforms (`<feature>-queries.md`)
For each query: the §1 line, the SQL, then:

| Part | Room (Android) | SwiftData (iOS) |
|---|---|---|
| Rows | `@Query("<same SQL>")` returning a small projection `data class` (only the selected columns, money as `String` → `BigDecimal` in the repository) | `FetchDescriptor<Model>(predicate: #Predicate { $0.typeRaw == "expense" && $0.localDate >= start && $0.localDate <= end }, sortBy: [...])` |
| Observed lists | `Flow<List<Row>>` | `@Query` is UI-only and not allowed; the repository re-fetches on `ModelContext` save notifications and publishes an `AsyncStream` |
| Joins | SQL `JOIN` | relationship key path (`$0.category?.name`) or fetch the ids once and map with a dictionary |
| UNION ALL legs | SQL | two or three fetches, concatenated in the repository |
| Reduce | `rows.fold(BigDecimal.ZERO) { acc, r -> acc + r.amount }` / `groupBy { it.key }` | `rows.reduce(Decimal.zero) { $0 + $1.amount }` / `Dictionary(grouping:by:)` |
| Counts | `SELECT COUNT(*)` | `context.fetchCount(descriptor)` |
| Paging | keyset `WHERE` + `LIMIT` | `fetchLimit` + the same keyset predicate (no `fetchOffset` for growing lists) |

The reduce step and its rounding (half-up, 2 dp, `caffeine-domain`) are written **once** in `<feature>-queries.md` and are identical on both platforms. Repository method names are the same on both (`spentByCategory(cycle:)` / `spentByCategory(cycle)`); backend-lead fixes them in the contract.

Platform details and gotchas: `reference/platform-mapping.md`.

## 5. Readiness checklist (all PASS before DATA_DESIGN_READY)
1. `verify_queries.py` exit 0 over every schema file + the fixture + this feature's queries.
2. Every figure and list in the plan's screen map names a query (table in `<feature>-queries.md`).
3. Every query has at least one `-- expect:` taken from the golden sheet, and money expects are exact to 2 dp.
4. No `SELECT *`, no money aggregate in SQL, no OFFSET paging on growing lists (grep).
5. Every query has its Room and SwiftData mapping and its reduce step.
6. Joins ≤ 2 and UNION ALL ≤ 1 per query, or the reason is written.

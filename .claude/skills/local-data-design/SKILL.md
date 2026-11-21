---
name: local-data-design
description: How the Caffeine local-data engineer designs the on-device tables for SwiftData (iOS) and Room (Android) - keep it simple, one table per thing the user names, money as decimal text, enums as text, a localDate column for cycle maths, indexes for the screens that read them, and the complexity budget. Writes docs/data-model/<feature>-tables.md and sql/<feature>-schema.sql for backend-lead to turn into the contract. Loaded by local-data-engineer; read by backend-lead.
---

# Local Data Design (SwiftData + Room)

The local store is the product in V1.0 (no server until V2.0). It must be **simple enough that both platforms build the same thing from one page**, and Phase 2 sync can copy it row by row.

## 1. Inputs (read first)
`docs/lessons.md` · the plan `docs/plan/<feature>-plan.md` (tasks, ACs, screen map) · `docs/plan/golden-sample-data.md` · `docs/plan/glossary.md` (use its words for table and column names) · existing `docs/data-model/*-model.md`, `docs/data-model/sql/*-schema.sql`, `migrations.md` · `caffeine-domain`, `security-standard` §2 (classes), `swiftdata-patterns`, `room-patterns`.
Extend what exists. Never create a second table for a thing that already has one.

## 2. Simplicity rules (each one is checked)
1. **One table per thing the user names in the UI** (Account, Category, Transaction, Fixed cost, Installment plan, Goal…). No lookup tables for enums, no EAV, no JSON columns, no polymorphic "items" table.
2. **Store facts, derive totals.** Balances, spent, left to spend, net worth, % used are computed from the ledger by queries. No stored running balances, no triggers, no views (SwiftData has none, so Room must not depend on them). A cache table is allowed only after a measured problem (a query over 50 ms on 10,000 transactions on a mid device) and Ton's approval.
3. **Ids:** `id TEXT` uuid, same value on both platforms. Foreign keys are `<thing>Id`.
4. **Money:** `amount` as decimal text in Room (`BigDecimal.toPlainString()`), `Decimal` in SwiftData, always with `currencyCode`. Amounts entered by the user are > 0; the sign comes from `type`. Signed only where the value is a balance (e.g. `openingBalance`, card that owes = negative). Never REAL/FLOAT/DOUBLE.
5. **Enums:** `TEXT` with a CHECK list in the SQL; SwiftData stores the raw `String` (predicates compare strings, not Swift enums).
6. **Dates:** `occurredAt INTEGER` (epoch ms UTC, the instant) **plus** `localDate TEXT 'YYYY-MM-DD'` in the device zone at entry (Asia/Bangkok). Every cycle, day and month filter uses `localDate`, so no time-zone maths runs in SQL or predicates. (Open for Ton: whether a later time-zone change re-dates old rows. Default: no.)
7. **Booleans:** `INTEGER 0/1` in SQL, `Bool` in SwiftData / Kotlin.
8. **Names:** table = plural snake_case (`transactions`, `fixed_costs`); columns = camelCase, **identical** to the SwiftData property and the Room field. Glossary words win ("Fixed cost", not "Recurring bill").
9. **Relationships:** a plain `<thing>Id` column. Delete rule written per FK (`nullify` default; `cascade` only when a child has no meaning alone; seed categories are hidden, never deleted).
10. **Indexes:** one per filter a screen uses, named `idx_<table>_<cols>`. Start with `localDate`, `(type, localDate)` and every FK. No index nobody queries.
11. **Classification:** propose a class for every column (`Public` / `Internal` / `Confidential` / `Restricted`). Restricted columns are `BLOB` ciphertext (AES-256-GCM, `FieldCipher`); backend-lead confirms.

**Complexity budget per feature:** at most 2 new tables and 8 new columns on existing tables. Over budget → write why in `<feature>-tables.md` §Decisions and flag it for backend-lead.

## 3. Outputs
### `docs/data-model/sql/<feature>-schema.sql`
SQLite DDL (the engine Room uses): `CREATE TABLE` with CHECK lists, FKs and `CREATE INDEX`. It must load in `scripts/data/verify_queries.py`. Append to the existing schema; never redefine a table in two files (extend with a `-- ALTER (migration n)` comment block instead).

### `docs/data-model/<feature>-tables.md`
1. **Set Goal** (the readiness checklist §4, PASS/FAIL per line).
2. **Tables**: one table per entity with columns: name · neutral type (`uuid`, `decimal`, `iso4217`, `instant`, `localDate`, `enum(...)`, `string`, `bool`, `int`, `ciphertext`) · SQLite type · SwiftData type · Room type · required · default · class · why the screen needs it.
3. **Indexes**: index → which query in `<feature>-queries.md` uses it.
4. **Relationships and delete rules.**
5. **Platform snippets**: the `@Model` class and the `@Entity` data class, field for field (rules in `swiftdata-patterns` / `room-patterns`).
6. **Migration note**: new table = additive; changed column = needs a SwiftData `VersionedSchema` stage + Room `Migration` (backend-lead records the numbers in `migrations.md`).
7. **Decisions and open questions** (for Ton through backend-lead).

## 4. Readiness checklist (all PASS before DATA_DESIGN_READY)
1. `verify_queries.py` loads the schema and the fixture with exit 0.
2. Every entity and field the plan needs has a column; no column without a plan reason.
3. Grep: no `REAL|FLOAT|DOUBLE` in the schema; every money column has a `currencyCode` beside it (or on its parent row).
4. Every enum has a CHECK list matching the plan values exactly.
5. Every filter used by a query has an index (or an allow-scan reason in the query file).
6. Names identical across tables.md, schema.sql, the `@Model` and the `@Entity` snippets (diff the column lists).
7. Every column has a proposed class; Restricted columns are ciphertext.
8. Within the complexity budget, or the overrun is explained.

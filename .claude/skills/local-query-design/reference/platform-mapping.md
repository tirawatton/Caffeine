# Platform mapping notes (Room ↔ SwiftData)

## Room
- `@Query` SQL is compile-checked against the entities, so the column names in `<feature>-schema.sql` must match the `@Entity` fields exactly.
- CTEs (`WITH`) and `UNION ALL` work in `@Query`. Return a projection data class whose property names equal the SQL aliases.
- Money columns come back as `String`; convert with the `BigDecimalConverter` or in the repository. Never read them as `Double`.
- SQLCipher (foundation T-09) does not change the SQL.
- Observed queries return `Flow`; one-shot reads are `suspend`.

## SwiftData (iOS 18+)
- `#Predicate` supports `==`, `<`, `>=`, `&&`, `||`, optional chaining and `contains` on strings; it does **not** support enum cases, computed properties or custom functions. Hence `typeRaw: String` and `localDate: String`.
- String comparison of `'YYYY-MM-DD'` sorts correctly, so `localDate >= start && localDate <= end` is the range filter.
- No GROUP BY and no SUM: fetch the rows, reduce in the `@ModelActor` repository, return Sendable domain structs.
- Use `propertiesToFetch` on large fetches to load only the needed attributes.
- `fetchCount` for counts; never fetch rows only to count.
- Relationship filters (`$0.category?.name == x`) work, but prefer filtering by the stored id (`$0.categoryId == id`) when both exist: it is faster and maps 1:1 to the Room column.

## Same answer on both
The QA parity check compares repository outputs, not SQL. A query is correct only when Room rows + reduce and SwiftData rows + reduce give the golden value. The script is the neutral referee for the SQL half; the `-cases.md` rows (backend-lead) are the referee for the reduce half.

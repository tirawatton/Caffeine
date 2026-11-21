---
name: swiftdata-patterns
description: SwiftData rules for Caffeine - @Model conventions, Decimal money, typed predicates, repositories, VersionedSchema migrations, in-memory tests. Read by ios-developer, backend-lead.
---

# SwiftData Patterns

- Every `@Model` has `@Attribute(.unique) var id: UUID`. Field names match the logical model in `docs/data-model/<feature>-model.md` exactly (Android uses the same names).
- Money: `Decimal` + `currencyCode: String`. Enums stored as `String` raw values.
- Relationships: declare the inverse; choose delete rules explicitly (`.nullify` default, `.cascade` only when the logical model says so).
- Queries: `#Predicate` with key paths; paginate with `FetchDescriptor.fetchLimit/fetchOffset`.
- Only `Sources/Repositories/` imports SwiftData. Repositories expose domain structs (Sendable value types), not `@Model` objects, to Stores.
- Use a `@ModelActor` repository for background work; never pass `@Model` instances across actors.
- Schema change to a shipped model: new `VersionedSchema` + `SchemaMigrationPlan` stage, recorded in `docs/data-model/migrations.md` with the matching Room migration number.
- Tests: `ModelConfiguration(isStoredInMemoryOnly: true)`.

---
name: data-contract
description: How the Caffeine backend lead writes the one platform-neutral contract per feature that iOS, Android and the future sync backend all follow - logical model, SwiftData and Room mappings, domain models, identical repository interfaces, migrations, validation placement, sync/REST shape, and the shared input-to-output cases table. Includes the contract readiness criteria. Loaded by backend-lead.
---

# Data Contract

Both apps must agree on entity names, field names, types, relationships and results, so behaviour (and Phase 2 sync) stays identical.

## Inputs
The plan, existing `docs/data-model/*.md`, live code in `ios-app/Sources/{Models,Repositories}` and `android-app/app/src/main/kotlin/com/tonapps/caffeine/{model,repository,data}`. Extend what exists; never fork an entity.

## `docs/data-model/<feature>-model.md`
1. **Logical model** (source of truth): entities, fields with neutral types (`uuid`, `decimal`, `iso4217`, `instant`, `localDate`, `enum`, `string`), required / unique, relationships and delete rules.
2. **SwiftData mapping** – `@Model` code (rules in `swiftdata-patterns`).
3. **Room mapping** – `@Entity`, DAO signatures, converters (rules in `room-patterns`).
4. **Domain models** exposed to Store / ViewModel – Swift `struct` and Kotlin `data class`, same field names.
5. **Repository interface** – method names identical on both platforms, `async throws` / `suspend`.
6. **Migration** – SwiftData `VersionedSchema` stage and Room version + `Migration`; append to `docs/data-model/migrations.md` with both numbers.
7. **Validation placement** – which rule lives in the data layer vs the Store / ViewModel.
8. **Sync / REST resource** per entity (documentation until Phase 2; then it is the API built in `backend/`).

## `docs/data-model/<feature>-cases.md`
One row per calculation: case id · input · expected output · plan AC. Cover zero, max, negative/refund, rounding (THB 2 dp, banker's or half-up as `caffeine-domain` says), month boundary, timezone (Asia/Bangkok), transfers excluded from totals. Both developers copy every row into tests; QA asserts every row on both platforms.

## Contract readiness criteria (all must PASS before CONTRACT_READY)
1. Every entity and field the plan needs is in the logical model.
2. Every calculation AC has at least one case row.
3. Names are identical across logical model, SwiftData, Room, domain models and repositories.
4. Money is `decimal` + `iso4217` everywhere (never Double/Float).
5. Migration path defined for every shipped-model change.
6. No conflict with the existing schema (conflict → BLOCKED, ask Ton).

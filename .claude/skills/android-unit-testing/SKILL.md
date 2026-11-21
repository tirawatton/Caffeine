---
name: android-unit-testing
description: How Caffeine Android unit tests are written - JUnit, kotlinx-coroutines-test with runTest and an injected StandardTestDispatcher, a MainDispatcherRule, Turbine for flows, fakes over mocks, parameterized tests for the shared cases table, Room in-memory tests, fixed Clock, zone and locale, naming and folders, coverage. Loaded by android-developer and qa-engineer.
---

# Android — Unit Testing

`tdd-workflow` says *when* (red → green → refactor); this says *how*.

## Framework and layout
- JUnit 4 (works with Compose and Room test rules), `kotlinx-coroutines-test`, Turbine, Truth or kotlin.test assertions. New test libraries go in `gradle/libs.versions.toml` and are listed in the lane file for review.
- JVM tests: `android-app/app/src/test/kotlin/com/tonapps/caffeine/<feature>/` (developer), `…/caffeine/qa/` (qa-engineer). Room and other device tests: `src/androidTest/`.
- One file per type under test: `HomeViewModelTest`, `RoomTransactionRepositoryTest`, `BudgetPaceTest`.

## What to test where
| Unit | Setup | Assert |
|---|---|---|
| Domain function | none | output for **every row** of `docs/data-model/<feature>-cases.md` (JUnit `Parameterized` or a table loop with a clear failure message per row) |
| ViewModel | real ViewModel + **fake** repository (in-memory class implementing the interface), injected `StandardTestDispatcher`, fixed `Clock` | send intents → `viewModel.state.test { … }` (Turbine) / effects via the effects flow |
| Repository | `Room.inMemoryDatabaseBuilder(...)` in `androidTest` (`allowMainThreadQueries()` only in tests) | rules, queries, `Flow` emissions, migrations with `MigrationTestHelper` |

Prefer fakes over MockK; a fake can record calls when an interaction must be asserted.

## Coroutines
- `MainDispatcherRule` sets `Dispatchers.setMain(testDispatcher)`; inject the same dispatcher as IO/Default.
- `runTest { }`; advance with `advanceUntilIdle()` / `runCurrent()`; never `Thread.sleep` or real delays (virtual time skips `delay`, e.g. search debounce).
- Cancellation: start a load, cancel the scope, assert no error state.

## Determinism
`Clock.fixed(Instant.parse("2026-11-18T02:00:00Z"), ZoneId.of("Asia/Bangkok"))`; `Locale.US` and `Locale("th","TH")` for formatting cases. Edge dates in every date suite: month end, Feb 29, cycle start on the 25th/31st, Bangkok midnight vs UTC.

## Naming and quality
- Backtick names that state behaviour: `` fun `over pace when 84 percent used on day 18 of 30`() ``.
- One behaviour per test, arrange-act-assert, no logic in assertions.
- A test that can't fail is a review finding (`code-review`).
- Coverage: Kover or JaCoCo report; every AC listed `AC-xx -> TestName` in the lane file.

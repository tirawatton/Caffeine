---
name: tdd-workflow
description: Red-green-refactor rules for both platforms - what must be test-driven, where tests live, XCTest/Swift Testing and JUnit/coroutines-test conventions. Read by ios-developer, android-developer and qa-engineer.
---

# TDD Workflow

## Loop per unit of logic
1. **Red**: write one failing test taken from an acceptance criterion (`docs/plan/<feature>-plan.md`). Confirm it fails for the right reason.
2. **Green**: minimum code to pass.
3. **Refactor** with the test green, then the next criterion.

## Always TDD
Repository rules, Store / ViewModel intent handling, every calculation in `caffeine-domain` (formatting, budget, pace, cycle dates, validation).

## Do not force TDD on
Pure layout (a View or Composable with no logic). Check those with previews in Dark and Light against the design spec.

## iOS
- Tests in `ios-app/Tests/<Feature>Tests/`. Swift Testing (`@Test`, `#expect`) for new tests; XCTest is fine where needed.
- Store tests: real Store + mock repository; send intents, assert on state. Use `async` tests, never sleeps.
- Repository tests: in-memory `ModelContainer(isStoredInMemoryOnly: true)`.

## Android
- Unit tests in `android-app/app/src/test/kotlin/...`; Room tests in `src/androidTest` with `Room.inMemoryDatabaseBuilder`.
- ViewModel tests: `runTest` + injected `StandardTestDispatcher` + Turbine for flows; never `Thread.sleep`.

## Coverage hand-off
Each developer lists, in its lane status file, which acceptance criteria its tests cover (`AC-03 -> HomeStoreTests.testOverPace`). qa-engineer fills gaps in its own QA test folders and does not re-test logic already covered.

## Parity tests
For every domain calculation, add the same table of input/output cases on both platforms (same values, same expected strings). Put the shared table in `docs/data-model/<feature>-cases.md` so both lanes copy identical cases.

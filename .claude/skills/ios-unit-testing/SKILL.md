---
name: ios-unit-testing
description: How Caffeine iOS unit tests are written - Swift Testing (@Test, #expect, #require, parameterized arguments for the shared cases table), Store tests with fake repositories, repository tests on an in-memory SwiftData container, deterministic clock, calendar, time zone and locale, async and cancellation tests, naming and folders, coverage. Loaded by ios-developer and qa-engineer.
---

# iOS — Unit Testing

`tdd-workflow` says *when* (red → green → refactor); this says *how*.

## Framework and layout
- **Swift Testing** for new tests: `@Suite`, `@Test("readable name")`, `#expect`, `#require` (unwrap without `!`). XCTest only for `measure {}` performance tests.
- Folders: `ios-app/Tests/<Feature>Tests/` (developer), `ios-app/Tests/QA/` (qa-engineer). One file per type under test: `HomeStoreTests.swift`, `TransactionRepositoryTests.swift`, `BudgetPaceTests.swift`.

## What to test where
| Unit | Setup | Assert |
|---|---|---|
| Domain function (budget, pace, cycle, split, formatting) | none | output for **every row** of `docs/data-model/<feature>-cases.md` via `@Test(arguments:)` |
| Store | real Store + **fake** repository (in-memory struct conforming to the protocol), injected clock/calendar/locale | send intents → `#expect(store.state == expected)` |
| Repository | `ModelContainer(for:, configurations: ModelConfiguration(isStoredInMemoryOnly: true))` | rules, queries, delete rules, migrations |

Prefer hand-written fakes over mocking frameworks; a fake records calls when you need to assert one happened.

## Determinism
- Inject `clock: () -> Date` and a `Calendar(identifier: .gregorian)` whose `timeZone` is Asia/Bangkok, obtained with `try #require(TimeZone(identifier: "Asia/Bangkok"))` (no `!`, even in tests).
- Fix the locale (`Locale(identifier: "en_US")` and `"th_TH"` cases for formatting).
- Edge dates in every date suite: month end, Feb 29, cycle start on the 25th/31st, midnight in Bangkok vs UTC.

## Async
- Tests are `async`; `await` the Store's work through a returned task or an intent that awaits. Never `Task.sleep` to "wait for" results.
- Events: `await confirmation { confirm in ... }`.
- Cancellation: start a load, cancel, `#expect` state did not change to error.

## Naming and quality
- Name = behaviour: `@Test("Over pace when 84% used on day 18 of 30")`.
- One behaviour per test; arrange-act-assert; no logic (loops/ifs) in assertions except parameterized arguments.
- A test that can't fail is a review finding (`code-review`).
- Coverage: run with `-enableCodeCoverage YES`; every AC is listed `AC-xx -> TestName` in the lane file.

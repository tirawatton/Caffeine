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

## How to write the tests
Platform mechanics (frameworks, fakes, in-memory stores, dispatchers, determinism, naming) live in `ios-unit-testing` / `android-unit-testing`; screen-level tests in `ios-ui-testing` / `android-ui-testing`. This skill only sets the rhythm and what must be test-driven.

## Coverage hand-off
Each developer lists, in its lane status file, which acceptance criteria its tests cover (`AC-03 -> HomeStoreTests.testOverPace`). qa-engineer fills gaps in its own QA test folders and does not re-test logic already covered.

## Parity tests
For every domain calculation, add the same table of input/output cases on both platforms (same values, same expected strings). Put the shared table in `docs/data-model/<feature>-cases.md` so both lanes copy identical cases.

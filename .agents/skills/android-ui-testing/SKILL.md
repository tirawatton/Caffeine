---
name: android-ui-testing
description: How Caffeine Android UI tests are written with the Compose testing APIs - createAndroidComposeRule with Hilt, finding nodes by the shared testTag ids, semantics assertions, waiting without sleeps, fake data and fixed clock, dark mode, font scale and Thai locale, screen robots, accessibility checks, and how these tests differ from QA's cross-platform Appium suite. Loaded by android-developer and qa-engineer.
---

# Android — UI Testing (Compose)

## Scope
- Developer UI tests prove **each new screen works on Android**: happy path plus one error/empty state per screen, and every navigation in the feature's journey.
- QA's Appium suite (`appium-parity`) proves **Android and iOS behave the same**. Don't duplicate it; share the ids.

## Setup
- Tests in `android-app/app/src/androidTest/kotlin/com/tonapps/caffeine/<feature>/`. `HiltAndroidRule` + `createAndroidComposeRule<HiltTestActivity>()`; a test module replaces repositories with fakes seeded per state (`overPace`, `emptyMonth`) and binds a fixed `Clock`.
- Screen-only tests (no navigation) use `createComposeRule()` and `setContent { CaffeineTheme { XScreen(state = …, onIntent = {}) } }` — fastest, no Hilt.
- Root has `Modifier.semantics { testTagsAsResourceId = true }` so the same tags are Appium resource ids.

## Writing tests
- Find by tag only: `onNodeWithTag("home.addButton")`, ids exactly as in the spec (`<screen>.<element>`). No text or index lookups except for asserting copy.
- Assert semantics: `assertIsDisplayed()`, `assertIsSelected()`, `assertTextEquals("−฿320")`, `assertContentDescriptionEquals(...)`.
- Wait with `composeRule.waitUntil(timeoutMillis = 5_000) { … }` or `waitUntilExactlyOneExists(hasTestTag(...))` — never `Thread.sleep`. Animations: `composeRule.mainClock.autoAdvance` or disable animations on the test device.
- Robots mirror `qa-automation/pages/` (`HomeRobot`, `KeypadRobot`) with methods like `addExpense(amount)`.
- Variants: dark mode via `uiMode` in `setContent` (`CompositionLocalProvider` / theme param), font scale via `LocalDensity` (`fontScale = 2f`), Thai via a locale-wrapped context.
- Accessibility: `AccessibilityChecks.enable()` (Espresso accessibility checks) for screens with Views, and touch-target / content-description assertions for Compose nodes.
- Screenshot evidence for the lane file: `onRoot().captureToImage()` in Dark and Light (screenshot-test libraries only with Ton's approval).

## Run
`./gradlew connectedDebugAndroidTest` on an API 28 and a latest-API emulator.

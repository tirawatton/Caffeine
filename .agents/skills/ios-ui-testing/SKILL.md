---
name: ios-ui-testing
description: How Caffeine iOS UI tests are written with XCUITest - the CaffeineUITests target in project.yml, launch arguments for seeded in-memory data, appearance, Dynamic Type and language, finding elements by the shared accessibility ids, waiting without sleeps, screen objects, accessibility audits, and how these tests differ from QA's cross-platform Appium suite. Loaded by ios-developer and qa-engineer.
---

# iOS — UI Testing (XCUITest)

## Scope
- Developer UI tests prove **each new screen works on iOS**: the happy path plus one error/empty state per screen, and every navigation in the feature's journey.
- QA's Appium suite (`appium-parity`) proves **iOS and Android behave the same**. Don't duplicate it; share the ids.

## Setup
- Target `CaffeineUITests` (`type: bundle.ui-testing`, depends on `Caffeine`) in `ios-app/project.yml`, added to the `Caffeine` scheme's test targets. Run `xcodegen generate` after adding it.
- Tests in `ios-app/UITests/<Feature>UITests.swift`.

## Launch configuration (read by the app in `CaffeineApp.init`, debug builds only)
| Argument | Effect |
|---|---|
| `-uitest` | in-memory store, animations off (`UIView.setAnimationsEnabled(false)`), no onboarding |
| `-seed <fixture>` | load a named fixture (e.g. `overPace`, `emptyMonth`) matching the plan's states |
| `-appearance dark|light` | override `preferredColorScheme` |
| `-UIPreferredContentSizeCategoryName UICTContentSizeCategoryAccessibilityXL` | Dynamic Type check |
| `-AppleLanguages (th) -AppleLocale th_TH` | Thai |
| `-now 2026-11-18T09:00:00+07:00` | fixed clock |

## Writing tests
- Find by id only: `app.buttons["home.addButton"]`, ids exactly as in the spec (`<screen>.<element>`). No label text or index queries.
- Wait with `XCTAssertTrue(el.waitForExistence(timeout: 5))` or predicate expectations — never `sleep`.
- Screen objects mirror `qa-automation/pages/` (`HomeScreen`, `KeypadScreen`) with methods like `addExpense(amount:)`.
- Assert visible results: the signed amount text, the selected state, the next screen's root id.
- `try app.performAccessibilityAudit()` on each new screen (iOS 17+); fix or record exceptions.
- Screenshots for the lane file: `XCTAttachment(screenshot: app.screenshot())` in Dark and Light.

## Run
`xcodebuild test -scheme Caffeine -destination "id=$SIM_ID" -derivedDataPath build/DD -only-testing:CaffeineUITests` on the newest iOS and one iOS 18 simulator.

---
name: appium-parity
description: The cross-platform Appium + Pytest framework in qa-automation/ - one test, both apps, shared accessibility ids, Page Objects, explicit waits, W3C gestures - and the rule that a test passing on one platform and failing on the other is a blocking divergence. Read by qa-parity-tester and by UI engineers who must expose ids.
---

# Appium Parity Testing

## Layout
```
qa-automation/
  conftest.py        # driver fixture parametrised ["ios", "android"]
  pages/base_page.py # waits + gestures; every Page subclasses it
  pages/<screen>_page.py
  tests/test_<feature>.py
  requirements.txt   # Appium-Python-Client, pytest, pytest-html
```

## Rules
- Locators: `AppiumBy.ACCESSIBILITY_ID` only, id format `<screen>.<element>` (e.g. `home.hero.leftToSpend`, `keypad.save`). iOS sets `accessibilityIdentifier`; Android sets `testTag` with `testTagsAsResourceId = true`. No XPath.
- Locators live only in Page classes.
- Explicit waits (`WebDriverWait`) only; never `time.sleep`.
- Gestures via W3C actions or `mobile: scroll` / `mobile: swipe`; no fixed coordinates.
- One test body for both platforms. More than 2 `if driver.platform == ...` branches in one test is itself a divergence finding.
- Assert user-visible results with identical strings on both platforms (formatted amounts, captions, statuses).
- Seed data through a launch argument (`-uiTestSeed <name>` on iOS, intent extra `uiTestSeed` on Android) so both apps start from the same state.

## Capabilities
iOS: XCUITest, iPhone 16/17 simulator, platformVersion 18+. Android: UiAutomator2, emulator API 28 and latest. App paths come from the verifiers' status notes (`.app` from `xcodebuild -derivedDataPath`, `.apk` from `assembleDebug`).

## Run
`pytest qa-automation/tests/test_<feature>.py --ios-app-path <path> --android-app-path <path> --html=docs/review/<feature>-qa.html`
Needs a running Appium 2 server with xcuitest and uiautomator2 drivers. If missing, report "QA unverified: no Appium server".

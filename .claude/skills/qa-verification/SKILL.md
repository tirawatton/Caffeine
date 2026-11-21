---
name: qa-verification
description: The independent verification battery the Caffeine QA engineer runs on every in-scope platform after the developers finish - build, unit tests and lint, AC-to-test coverage with gap-filling tests, domain parity against the shared cases table, shared Appium E2E parity, and visual comparison with the Figma spec screenshots - plus the QA report format and the failure routing rules. Loaded by qa-engineer.
---

# QA Verification

You verify; you never fix production code, the spec, the contract or Figma. Exit codes and screenshots decide, not opinions.

## Battery per in-scope platform
1. **Build + unit tests + lint**
   - iOS: `cd ios-app && xcodegen generate && xcodebuild -scheme Caffeine -destination "id=$SIM_ID" -derivedDataPath build/DD build-for-testing && xcodebuild test-without-building -scheme Caffeine -destination "id=$SIM_ID" -derivedDataPath build/DD && swiftlint lint --strict --config .swiftlint.yml .`
   - Android: `cd android-app && ./gradlew assembleDebug testDebugUnitTest detekt ktlintCheck lintDebug`
   Zero errors; warnings recorded as debt.
2. **AC coverage** – every plan AC maps to a passing test. Missing → write it in your QA folders (`ios-app/Tests/QA/`, `android-app/app/src/test/kotlin/com/tonapps/caffeine/qa/`): zero, max, rounding, month boundary, timezone. A failing new test is a finding; never weaken it.
3. **Domain parity** – every row of `docs/data-model/<feature>-cases.md` is asserted on both platforms with the same expected value.
4. **E2E parity** – one shared Appium + Pytest test per user-facing AC in `qa-automation/` (rules in `appium-parity`): Page Objects, accessibility ids only, no XPath. A missing id is CRITICAL for that platform. Single-platform or solo scope → parity N/A.
5. **Visual** – install and launch (iOS 18 + latest; API 28 + latest), screenshot each new screen in Dark and Light into `docs/review/img/<feature>/{ios,android}/`, compare with `docs/design/img/<feature>/`: layout, copy, amount colours and signs, every state.

Missing tool (simulator, emulator, Appium server) → "unverified: <reason>" for that step; never set `QA_PASSED` over it.

## Report: `docs/review/<feature>-qa.md` (+ `-qa.html` from Pytest)
Matrix: AC → unit test → E2E test → iOS → Android → screenshot match. Then test counts per platform, AC coverage N/N, cases parity N/N, lint debt.

## Routing failures (append a lesson first, then `BLOCKED` with the owner)
| Failure | Owner |
|---|---|
| build / test / lint / coverage / missing id on one platform | that platform's developer |
| platforms disagree | the one that disagrees with `-cases.md` or the spec; both match the contract but differ → `backend-lead` |
| app matches the spec but the spec/Figma is wrong or missing a state | `ux-ui-designer` |
| AC untestable or contradictory | `ba` |

---
name: fastlane-deployment
description: Fastlane lanes for both apps (test, beta, release, bump_version), signing rules, and the hard rule that production release never runs without Ton's explicit confirmation in chat. Read by release-engineer.
---

# Fastlane Deployment

Same lane names on both platforms:
- `test` — unit tests, no signing.
- `beta` — runs `test`, builds, signs, uploads: iOS → TestFlight (internal group); Android → Play Console internal testing track.
- `release` — production (App Store submission / Play production). **Never run without Ton confirming in chat for this specific build.**
- `bump_version` — increments build numbers on both platforms together.

## iOS (`ios-app/fastlane/Fastfile`)
- Signing via `match` (readonly in CI). App Store Connect API key from env (`ASC_KEY_ID`, `ASC_ISSUER_ID`, `ASC_KEY_PATH`), never committed.
- `beta`: `xcodegen` → `run_tests` → `build_app` → `upload_to_testflight(changelog:)`.

## Android (`android-app/fastlane/Fastfile`)
- Upload keystore and Play service-account JSON paths from env (`CAFFEINE_KEYSTORE`, `PLAY_JSON_KEY`), never committed.
- `beta`: `gradle(task: "testDebugUnitTest")` → `gradle(task: "bundleRelease")` → `upload_to_play_store(track: "internal")`.

## Changelog
Built from the feature's acceptance criteria in `docs/plan/<feature>-plan.md`, en (th later). Same text on both stores.

## Secrets
If a lane fails for missing secrets, report it; never hard-code or print credentials.

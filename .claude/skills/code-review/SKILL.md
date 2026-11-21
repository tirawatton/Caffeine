---
name: code-review
description: How the Caffeine backend lead reviews a feature on iOS and Android after QA passes - mechanical greps first (force unwraps, floating-point money, persistence in the UI layer), then architecture, concurrency, contract drift, security, privacy, accessibility and token fidelity, with severity rules and the review file format. Loaded by backend-lead.
---

# Code Review

Read-only on app code. QA already built and tested, so do not rebuild. Review the feature diff (`git diff <base>..HEAD -- ios-app android-app`).

## 1. Mechanical (any hit = CRITICAL)
iOS
```
grep -rnE "[A-Za-z0-9_)\]]!([^=]|$)|try!|as!" ios-app/Sources          # ignore != and comments
grep -rnE "(amount|price|balance|fee|cost|total)\w*\s*:\s*(Double|Float)" ios-app/Sources
grep -rnE "import SwiftData|ModelContext|@Query" ios-app/Sources/Features
```
Android
```
grep -rn "!!" android-app/app/src/main
grep -rnE "(amount|price|balance|fee|cost|total)\w*\s*:\s*(Double|Float)" android-app/app/src/main
grep -rnE "import androidx.room|Dao\b" android-app/app/src/main/kotlin/com/tonapps/caffeine/features
```

## 2. Judgment
| Severity | iOS | Android | Both |
|---|---|---|---|
| CRITICAL | `ObservableObject`/`@Published`, SwiftData outside Repositories, non-Sendable values crossing actors, `Task.detached`, Liquid Glass without iOS 18–25 fallback | `GlobalScope`, Room/DAO in ViewModel or composable, one-shot events in State, hard-coded dispatchers | money or personal data in logs/analytics, secrets in code |
| HIGH | | | contract drift (names or results differ from `<feature>-model.md` or between platforms), raw colour/spacing in feature code, missing label or id, unrecorded spec deviation, tests that assert nothing |
| MEDIUM / LOW | | | naming, long functions, missing preview states, other debt |

## 3. Output: `docs/review/<feature>-review.md`
Grouped by severity; each finding = platform · file:line · rule · minimal fix · owner (`ios-developer` / `android-developer`).
- Any CRITICAL/HIGH → append a lesson, set `BLOCKED` with the owner. After the fix the flow re-runs QA, then this review.
- None → `REVIEW_PASSED`; MEDIUM/LOW stay in the file as debt.

Never edit the code to fix a finding yourself.

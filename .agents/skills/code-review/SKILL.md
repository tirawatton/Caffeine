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

## 1b. Security greps
Lines 1 and 3: any hit = CRITICAL. Lines 2 and 4: review every hit — CRITICAL when it touches tokens, keys or user data, otherwise a finding to justify in the review.
```
grep -rnE "NSAllowsArbitraryLoads|cleartextTrafficPermitted=\"true\"|allowBackup=\"true\"" ios-app android-app
grep -rnE "UserDefaults.*(token|key|secret)|getSharedPreferences|EncryptedSharedPreferences|MD5|SHA1|\"AES/ECB|\"AES/CBC|Random\(\)" ios-app/Sources android-app/app/src/main
grep -rniE "(api[_-]?key|secret|password|BEGIN (RSA|EC|PRIVATE) KEY)\s*[:=]" ios-app android-app backend 2>/dev/null
grep -rnE "print\(|Log\.(d|v|i)\(|privacy: \.public" ios-app/Sources android-app/app/src/main
```
Then check `security-standard` §7 item by item and the feature threat model: every Restricted field encrypted with the right AAD, keys hardware-backed, no data in logs/analytics/widgets/notifications, API calls only through the client with pinning.

## 2. Judgment
| Severity | iOS | Android | Both |
|---|---|---|---|
| CRITICAL (security) | | | any security grep hit, unencrypted Restricted field, key or token outside Keychain/Keystore, disabled TLS checks or pinning, PII in logs |
| CRITICAL | `ObservableObject`/`@Published`, SwiftData outside Repositories, non-Sendable values crossing actors, `Task.detached`, Liquid Glass without iOS 18–25 fallback | `GlobalScope`, Room/DAO in ViewModel or composable, one-shot events in State, hard-coded dispatchers | money or personal data in logs/analytics, secrets in code |
| HIGH | | | contract drift (names or results differ from `<feature>-model.md` or between platforms), raw colour/spacing in feature code, missing label or id, unrecorded spec deviation, tests that assert nothing |
| MEDIUM / LOW | | | naming, long functions, missing preview states, other debt |

## 3. Output: `docs/review/<feature>-review.md`
Grouped by severity; each finding = platform · file:line · rule · minimal fix · owner (`ios-developer` / `android-developer`).
- Any CRITICAL/HIGH → append a lesson, set `BLOCKED` with the owner. After the fix the flow re-runs QA, then this review.
- None → `REVIEW_PASSED`; MEDIUM/LOW stay in the file as debt.

Never edit the code to fix a finding yourself.

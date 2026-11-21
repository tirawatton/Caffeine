# foundation — plan (E00 of the master plan)

Author: `ba` · 2026-11-21 (revision 7) · Platform scope: **Both** · Priority: **Must** · Release: V1.0 (foundation, built first)
Brief source: Ton's master-plan request of 2026-11-21 (main session) and `docs/plan/caffeine-app-master-plan.md` §E00. There is no `docs/briefs/foundation-brief.md` yet. Ton owns briefs; the conductor can write one from §1–§2 below for Ton to confirm.
Decisions applied: `docs/decisions/2026-11-21-ton-answers.md`, covering Q-16 rounding (T-18, T-19), Q-04 splash / shield (T-20 to T-22) and Q-30 split storage (T-02, T-09). Since revision 3 also the v5.1 audit fix pass recorded in CLAUDE.md ("v5.1 — UX/UI audit fix pass (21 Nov 2026)") and `docs/design/tokens-changelog.md`: budget cycle = payday, new and changed tokens. Release: part of **V1.0**.

## Readiness checklist (revision 7, after Ton's fifth-round answers Q-59 to Q-62; Verify pass 1 of 3)
Revision 7 re-ran all 9 checks: **9/9 PASS on pass 1.**
1. PASS: no task added. T-16, T-17 and T-18 keep all 8 fields; their definitions of done list the new ACs.
2. PASS: amended AC-46b and new AC-46c and AC-51e are Given / When / Then with concrete values.
3. PASS: the new ACs are edge cases of T-16 and T-18.
4. PASS: no new flow branch. The State B caption is covered by AC-46b (F11).
5. PASS: no new dependency.
6. PASS: every figure re-derived from the updated `caffeine-domain`: overBy = −(40,000 − 41,200 − 599) = 1,799; 40,000 − 15,046 = 24,954; floor(24,954 / 30) = 831; floor(24,954 / 29) = 860.
7. PASS: no new screen in this feature. The State B hero is E03-T04 / DG-56 (5).
8. PASS: N/A, no KPI.
9. PASS: the T-16 / T-18 security rows cover the new values (Confidential, in memory only; errors carry no values).

**Revision 7** (2026-11-21, Ton's answers Q-59 to Q-62, decisions file Part 6):
- Q-61: T-16 `overBy` = −leftToSpend (spent − budget + committedUnpaid), so the Over budget caption always equals abs(Left to spend). AC-46b now expects overBy 1,799 (was 1,200). AC-45 (no set-aside, overBy 1,200) is unchanged. **backend-lead: update the AC-46b case row.**
- Q-60: `committedUnpaid` includes overdue charges carried from earlier cycles, and E11-T19 sums them. T-16 is unchanged. New AC-46c (24,954) and AC-51e (฿831, then ฿860 on 26 Nov) as case rows.
- Q-59 and Q-62 need no foundation change. The token pipeline (T-01) already carries `night/accent` and `night/income-text`.

## Readiness checklist (revision 6, after Ton's fourth-round answers Q-54 to Q-58; Verify pass 1 of 3)
Revision 6 re-ran all 9 checks: **9/9 PASS on pass 1.** Check 1: no task added; T-16 and T-18 keep all 8 fields. Check 2: AC-43c, AC-46b, AC-51d, AC-54a are Given / When / Then with concrete values. Check 3: the new ACs are edge cases of T-16 / T-18. Check 4: no new flow branch (F11 covers the negative case through AC-46b). Check 5: no new dependency. Check 6: every figure re-derived from the updated `caffeine-domain` (40,000 − 14,447 = 25,553 → ฿851/day; 40,000 − 39,800 − 599 = −399 → ฿0/day, billsExceedBy 399). Check 7: no new screen in this feature (the hero copy is E03, DG-56). Check 8: N/A — no KPI. Check 9: the security rows for T-16 / T-18 cover the new values (Confidential, in memory only; errors carry no values).

**Revision 6** (2026-11-21, Ton's answers Q-54 to Q-58, decisions file Part 5; `caffeine-domain` updated with Ton's approval):
- Q-55 / Q-58: `committedUnpaid` = upcoming **and overdue** unpaid fixed costs of **every kind** (bills, subscriptions, installments) due in the active cycle (T-16 text). Foundation still only computes; the sum comes from E11-T19. New AC-43c (Dec cycle 25,553) and AC-51d (฿851/day).
- Q-54: T-16 returns `billsExceedBy` (= −leftToSpend) when leftToSpend < 0 and spent ≤ budget; T-18 confirms `max(0, floor(...))`. AC-46a now names the output; new AC-46b, AC-54a.
- Q-56 (Mark paid variance) needs no foundation change: T-16 recomputes from the new spent and the new committed sum (E11 ACs).
- The skill now carries master plan §5 rules 9, 10 and 15, so check 6 reads `caffeine-domain` directly.

## Readiness checklist (revision 5, after Ton's third-round answers Q-51 / Q-52 / Q-53; Verify pass 2 of 3)
1. PASS: every task (T-01 to T-24) has all 8 fields (new T-23 shared month-day clamp, T-24 cycle label + previous cycle).
2. PASS: every AC is Given / When / Then with concrete values and no vague words (new AC-43b, AC-46a, AC-65 to AC-71 checked).
3. PASS: every task has at least one error or edge AC (marked *edge*); T-23: AC-66, AC-67, AC-68; T-24: AC-70, AC-71.
4. PASS: every flow branch (F1 to F14) is referenced by at least one AC; no new branch (the new domain errors are F11: AC-46a, AC-68, AC-71).
5. PASS: no dependency cycles and no duplicate tasks. New edges: T-23 → T-14 → T-24, T-16 unchanged (T-02, T-14, T-15), T-17 now also waits for T-23 and T-24. T-23 depends only on T-02, so no cycle. T-24 is not a duplicate of T-14 (T-14 finds the cycle; T-24 names it and steps back one cycle).
6. PASS: every number agrees with `caffeine-domain` **as amended by Ton's binding decisions** (Q-16, Q-48, Q-15, Q-51 B, Q-52, Q-53; master plan §5 rules 9, 10, 15): half-up rounding, signed amounts, transfers excluded, pace status with `<=` on actual spent, elapsed and days left include today, device timezone. Safe to Spend = 40,000 − 33,550 − 599 = ฿5,851 (AC-43b), per day floor(5,851 / 7) = ฿835 (AC-51c), clamp dates in AC-65 to AC-67 match `golden-sample-data.md` §6. Where the skill text still says "budget − expenses", the decision record wins (recorded in master plan §5 rule 15).
7. PASS: every screen state maps to a v5.1 frame or is listed as a Design gap (DG-01, DG-22, DG-23, DG-26). T-23 / T-24 have no screen in this feature (their labels are drawn by E03 / E07 / E12, design impact DG-54).
8. PASS: Analytics says "N/A — no KPI".
9. PASS: every task that touches user data names its data classes and has a security AC (§8; T-23 and T-24 added: AC-68, AC-71).

**Revision 5** (2026-11-21, Ton's answers to Q-51, Q-52, Q-53; decisions file Part 4):
- Q-53: one shared clamp `DayClamp.clamp(year, month, day)` for payday, recurring commitments and card cut-off / due days → new **T-23**; T-14 now calls it.
- Q-52: Home, Analytics and the History default use the budget cycle, labelled by the closing month → new **T-24** `BudgetCycle.label` and `BudgetCycle.previous` (replaces the "possible `BudgetCycle.label`" in the old Q-52 note).
- Q-51 B: Safe to Spend = budget − spent − upcoming unpaid fixed bills in the cycle → **T-16** gains the input `committedUnpaid` (the sum is supplied by E11-T19; foundation only computes). New AC-43b, AC-46a; T-18 gains AC-51c. Budget % and status stay on actual spent.
- AC-03a extended to the new case rows.
- Verify pass 1 failed check 5: T-17 (QA) did not list T-23 / T-24 in its dependencies, so the new functions would have had no independent verification. Fixed. Pass 2: 9/9 PASS.

**Revision 4** (2026-11-21, Ton's second-round answers, decisions file Part 3): Q-15 is answered, so payday / cycle start is now 1–31 with month-end clamping plus a "Last day of the month" option. Changed: §2 non-goals, T-02 (`cycleStartDay` 1–31 + new `cycleStartIsLastDay`, 9 fields), T-09, T-14 (clamping), AC-03a, AC-18, AC-19, AC-38, new AC-38a–AC-38e, T-14 definition of done, §9. Q-48 confirmed AC-51a / AC-53 (days left counts today, last day = 1). No task added or removed; no new flow branch. Checklist re-run: 9/9 PASS on pass 1.

**Revision 3** (2026-11-21, after the v5.1 UX/UI audit fix pass) changed T-01 (build the token pipeline; the 21 Nov token values; AC-01a, AC-01b), T-02 (`cycleStartDay` holds the payday), T-14 (AC-37a), T-16 (AC-43a, AC-44a) and T-18 (AC-51a, AC-51b, re-derived from Q-16 rather than the Figma hero). No task was added or removed; no new flow branch. Pass 1 is clean.

**Revision 2** added T-18 to T-22 and changed T-02, T-09 and T-17.
- Pass 1 of the revision failed check 4: the new branches F12–F14 had no AC.
- They now have AC-59 to AC-64.
- Pass 2 is clean.
- T-22 is a deliberate exception: it is **blocked by Q-31** (priority Should), so the plan stays buildable without it.

Original pass 1 (draft) failed 2 checks, and pass 2 was clean:
- **Check 6:** the per-day allowance used Figma's ฿537/day. That figure counts days remaining *without* today and floors, but `caffeine-domain` counts *with* today (฿6,450 / 13 = ฿496). Fixed by moving the per-day allowance out of this feature (to E03, blocked by Q-16) and logging a lesson.
- **Check 4:** the branch table pointed F1 at AC-17 and F3 at AC-21 (wrong ACs), and two definitions of done named the wrong lint AC. All of these were corrected.

## 1. Need
Every Caffeine feature needs the same base: an app that launches into the four-tab shell, colours and spacing that come from Figma tokens, an encrypted local store with hardware-protected keys, and money / cycle / budget rules that give identical results on iOS and Android. If these were built inside the first user feature, platform plumbing and product behaviour would be mixed in one review, and the two apps could drift on the rules every later screen depends on (5 Whys: drift → parity bugs → blocking bugs → slower features). The real need is a **parity and security baseline**, so that later features only add behaviour.

## 2. Scope
- **Goal:** both apps launch into the Home · Wallet · Analytics · Profile shell on an encrypted store, using generated tokens and shared, tested domain functions.
- **KPI:** none.
- **Platform scope:** Both (`/caffeine-pipeline foundation both`).
- **Priority:** Must.
- **In scope since revision 2:** the Q-16 display rules (per-day allowance, budget %, % vs previous month) as shared domain functions; the splash while the store initialises; the always-on app-switcher shield; a launch gate step that E06 fills with the App Lock prompt; and a storage layout that keeps the main ledger in the strictest class while leaving room for the V1.1 widget snapshot.
- **Non-goals:** any real tab content (each feature replaces its placeholder); the coral + button (Tab bar `State=No add` until E02 ships); the App Lock prompt, the App Lock and Privacy Mode toggles (E06; this feature only stores the two flags, the mask string and the launch gate hook); the Theme setting (E05; this feature follows the system appearance); the widget snapshot file itself (V1.1, E28; exception recorded in `docs/security/exceptions.md`); the payday picker UI (O5 in E04, 12G in E25; this feature stores and computes the rule only); sign-in, network and sync (no network calls in this feature).

## 3. Flow
```mermaid
flowchart TD
  L[App launch] --> SP["Splash (F12) while the store initialises"]
  SP --> K{Wrapped DEK exists?}
  K -- "no · first launch (F1)" --> G[Generate DEK, wrap with KEK]
  K -- "yes (F2)" --> U[Unwrap DEK]
  G -- "fail (F3)" --> E1[storeError STORE-KEY-01]
  U -- "fail (F3)" --> E1
  G --> O[Open encrypted store]
  U --> O
  O -- "fail (F4)" --> E2[storeError STORE-DB-01]
  E1 --> R{Retry (F5)}
  E2 --> R
  R -- success --> O
  R -- fail --> E1
  O -- "first launch (F1)" --> S[Seed AppSettings]
  S --> LG["Launch gate (F14): no-op until E06 adds the App Lock prompt"]
  O -- "returning (F2)" --> LG
  LG --> T[Tab shell · Home selected]
  T --> TS[Tab switch (F6)]
  T --> AP{System appearance (F7)}
  AP -- Dark --> D[night/* Dark]
  AP -- Light --> LI[night/* Light]
  T --> BK[Android back (F8): other tab → Home; Home → background]
  T --> OF[Offline (F9): no network calls, same behaviour]
  T --> PM[Privacy mask helper (F10): ฿••••••]
  T --> VA[Domain validation error (F11): coded error, no values]
  T --> BG["App to background (F13): privacy shield covers the window before the snapshot"]
  BG --> FG[Foreground: shield removed, same tab]
```

| Branch | Covered by |
|---|---|
| F1 first launch | AC-11, AC-18 |
| F2 returning launch | AC-12 |
| F3 key failure | AC-13 |
| F4 store open failure | AC-20 |
| F5 retry | AC-21, AC-22 |
| F6 tab switch | AC-08, AC-10 |
| F7 appearance | AC-06, AC-07 |
| F8 Android back | AC-09 |
| F9 offline | AC-26 |
| F10 privacy mask | AC-33 |
| F11 domain validation | AC-19, AC-38, AC-46, AC-46a, AC-68, AC-71 |
| F12 splash | AC-59, AC-60 |
| F13 background shield | AC-62, AC-63, AC-64 |
| F14 launch gate | AC-61 |

## 4. Tasks

### T-01 Generate design tokens
- **purpose:** Turn the Figma variables and text styles into platform token files that every screen uses.
- **layer:** UI
- **what to build:** Owner `ux-ui-designer`, per `design-tokens`. Every `Caffeine / Night` variable in Dark and Light goes to `ios-app/Resources/Colors.xcassets/Night/<token>.colorset` (Any = Light, Dark = Dark) and to `CaffeineColors.kt` (`dark`, `light`, with alpha kept in ARGB). `Caffeine / Dimensions` (space 0, 8, 16, 24, 32, 40, 48, 64; radius sm, md, lg, xl, full; layout/tab-bar-inset 128; layout/row-divider-inset 72) goes to `DesignTokens.swift` and `CaffeineDimens.kt`. `iOS/*` and `Data/*` text styles go to `DesignTokens.swift` and `CaffeineType.kt`, with the Android font = system Roboto / Roboto Mono (the documented default; Q-24 may change it later, which means regenerating only). Also generate `night/shadow`. Each file carries the generated-file header.
  **The pipeline does not exist yet** (no `scripts/tokens/`, no `docs/design/tokens.json`, no generated files); this task builds it. It must include the 21 Nov 2026 audit changes listed in `docs/design/tokens-changelog.md`: new primitives `coral/650` #CF3D20, `mint/700` #1F714C, `gray/650` #636366; new semantic token **`night/income-text`** (Dark #9EE6C4, Light #1F714C; output name `incomeText` on both platforms, used for income amounts and positive deltas drawn as text, while `night/income` stays for fills); Light `night/accent` → #CF3D20; Light `night/text-secondary` → #636366; `night/on-primary-soft` #1C1C1E at 88% in both modes; `night/on-accent-soft` #1C1C1E at 88% (Dark) and #FFFFFF at 96% (Light). Alpha tokens keep their alpha in the ARGB value / colour set. After generation, `tokens-changelog.md` stops being the only record.
- **error behaviour:** A variable listed in `design-tokens` that is missing in Figma stops generation with the token name. No partial file is written, and the previous files stay.
- **depends on:** none
- **platform:** Both
- **priority:** Must
- **definition of done:** The token diff (Figma both modes vs both outputs) reports 0 differences, AC-01a and AC-01b pass, and both apps compile with the files.

### T-02 Foundation contract
- **purpose:** Define the one data contract, the cases table and the threat model for this feature.
- **layer:** Data
- **what to build:** Owner `backend-lead`, per `data-contract`. Write `docs/data-model/foundation-model.md` with the `AppSettings` entity (single row: `id` uuid, `currencyCode` iso4217 = "THB", `cycleStartDay` int 1–31 = 1 (this is **the user's payday**, because the budget cycle follows payday, Ton A1; O5 and 12B / 12G write it in later features, and 1 means "no payday set"), `cycleStartIsLastDay` bool = false ("Last day of the month", Ton Q-15; when true, `cycleStartDay` is ignored), `themePreference` enum system|light|dark = system, `onboardingCompleted` bool = false, `appLockEnabled` bool = false, `privacyModeEnabled` bool = false, `createdAt` instant; all Internal). Add a **storage layout** section (Ton Q-30): the main ledger lives only in the strictest class (iOS `NSFileProtectionComplete`; Android SQLCipher with a hardware-backed Keystore KEK). A separate widget snapshot file in an App Group (iOS) is **reserved for V1.1** (E28) under exception EX-001 in `docs/security/exceptions.md`. Nothing in foundation may assume that the widget can read the main store. Also document: the wrapped-DEK record (Restricted, never in the store, only in Keychain / app-private storage), the `FieldCipher` wire format (nonce 12 bytes ‖ ciphertext ‖ tag 16 bytes; AAD = `"<recordId>|<fieldName>|<schemaVersion>"`) and repository names (`AppSettingsRepository.get()`, `.update(_:)`). Write `docs/data-model/foundation-cases.md` with one row per calculation AC in T-13 to T-16, T-18 and T-19, plus one fixed `FieldCipher` test vector (key, nonce, AAD, plaintext → ciphertext hex). Write `docs/security/foundation-threats.md` (STRIDE). Append V1 / Room 1 to `migrations.md`.
- **error behaviour:** A plan field that can't be classified → CONTRACT stays not ready and the question goes to Ton (BLOCKED).
- **depends on:** none
- **platform:** Both
- **priority:** Must
- **definition of done:** All 8 contract readiness criteria PASS, every AC in T-13 to T-16, T-18 and T-19 has at least one case row, and the storage layout section exists.

### T-03 iOS project baseline
- **purpose:** Make the iOS project build, test and lint with one command, with the targets later features need.
- **layer:** Platform
- **what to build:** In `ios-app/project.yml`: add a `CaffeineUITests` (bundle.ui-testing) target and a SwiftLint build phase that fails on errors (force unwrap, `try!` and `print(` are errors). Create the folder layout from `mvi-ios` under `Sources/`. Keep `ASSETCATALOG_COMPILER_APPICON_NAME` empty (lesson: no icon chosen). The command is `xcodegen generate && xcodebuild test -scheme Caffeine -destination id=$SIM_ID` (lesson: address simulators by id).
- **error behaviour:** Any build, test or lint failure exits non-zero and no artefact is reported as passing.
- **depends on:** none
- **platform:** iOS
- **priority:** Must
- **definition of done:** The command exits 0 and runs both test targets (AC-04); the lint test case (AC-04a) fails as expected.

### T-04 Android project baseline
- **purpose:** Make the Android project build, test and lint with one command, with the libraries later features need.
- **layer:** Platform
- **what to build:** Update `libs.versions.toml` to current stable (per `kotlin-style`). Add Room + KSP, SQLCipher for Android (`net.zetetic:sqlcipher-android`), Navigation Compose, kotlinx-coroutines, the test libraries from `android-unit-testing` / `android-ui-testing`, and the static analysis from `kotlin-style` (`!!` is an error in production code). Replace the stale comments that name removed agents (`token-sync-engineer`, `android-architect`) with `ux-ui-designer` / `android-developer`. The command is `./gradlew assembleDebug testDebugUnitTest lint` (plus the `kotlin-style` analysis task).
- **error behaviour:** Any failure exits non-zero.
- **depends on:** none
- **platform:** Android
- **priority:** Must
- **definition of done:** The command exits 0 (AC-05); the `!!` test case (AC-05a) fails as expected.

### T-05 Theme wiring
- **purpose:** Apply the generated tokens app-wide and follow the system Dark / Light appearance.
- **layer:** UI
- **what to build:** The root background is `night/bg`. Status bar and system glyphs follow `night/text-primary` (Android: edge-to-edge with light or dark system bar icons to match). Appearance follows the system until E05 adds the Theme setting. If the system reports no preference, use Dark (the Figma default mode). Feature code reads only tokens; raw colours and spacing are a review finding.
- **error behaviour:** A missing colour asset at runtime fails the build (iOS generated asset symbols; Kotlin compile), so no screen ships with a fallback colour.
- **depends on:** T-01, T-03, T-04
- **platform:** Both
- **priority:** Must
- **definition of done:** UI tests AC-06 and AC-07 pass on both platforms.

### T-06 Tab shell
- **purpose:** Give the app its four-tab navigation shell, which every feature plugs into.
- **layer:** UI
- **what to build:** A tab bar with Home · Wallet · Analytics · Profile in this order, built from the DS Tab bar `State=No add` (`272:990`); the + button arrives with E02. The active tab uses the `surface-raised` capsule. Accessibility ids are `tab.home`, `tab.wallet`, `tab.analytics` and `tab.profile`; hit areas are at least 44pt / 48dp. The tab bar sits 40pt from the bottom, and tab content uses bottom padding `layout/tab-bar-inset` (128). Each tab root shows a Large Title placeholder ("Home", "Wallet", "Analytics", "Profile") with id `<tab>.placeholder`; this is scaffold only (DG-23) and is replaced by each feature. Each tab keeps its own navigation stack while switching. Re-tapping the selected tab returns to its root. Android system back from Wallet, Analytics or Profile selects Home; back on Home moves the app to the background.
- **error behaviour:** None visible to the user. An unknown deep-link tab value falls back to Home.
- **depends on:** T-05
- **platform:** Both
- **priority:** Must
- **definition of done:** UI tests AC-08 to AC-10 pass on both platforms, and the Appium smoke (T-17) passes.

### T-07 Key management
- **purpose:** Create and protect the data-encryption key that the store and field encryption use.
- **layer:** Platform
- **what to build:** On first launch, generate a 256-bit DEK with the OS CSPRNG. Wrap it with a hardware-backed, non-exportable KEK: iOS Keychain with `kSecAttrAccessibleWhenUnlockedThisDeviceOnly` (Secure Enclave-backed wrapping key where available); Android Keystore AES-256 with StrongBox when available. Store only the wrapped DEK (iOS Keychain; Android app-private `no_backup` storage). On later launches, unwrap into memory. Use platform crypto only (CryptoKit, Keystore / Tink); never hand-written primitives.
- **error behaviour:** Generation, wrap or unwrap failure → T-10 screen with code `STORE-KEY-01`. Nothing is written to the store, and no existing key or data is deleted.
- **depends on:** T-02, T-03, T-04
- **platform:** Both
- **priority:** Must
- **definition of done:** Unit tests AC-11 to AC-13 pass; QA MASTG storage check passes (AC-14).

### T-08 Field encryption helper
- **purpose:** Provide one AES-256-GCM helper that every Restricted field (memo, merchant, account number, slip payload) uses.
- **layer:** Platform
- **what to build:** `FieldCipher.seal(plaintext, recordId, fieldName, schemaVersion) -> bytes` and `.open(...)`, AES-256-GCM with a random 96-bit nonce per call and a 128-bit tag. AAD is `"<recordId>|<fieldName>|<schemaVersion>"`, and the wire format comes from T-02, identical on both platforms. iOS uses CryptoKit `AES.GCM`; Android uses Tink AEAD or JCA `AES/GCM/NoPadding` with the same format.
- **error behaviour:** Open with the wrong AAD, key or tampered bytes throws `CIPHER-AUTH-01` and returns no partial plaintext.
- **depends on:** T-02, T-07
- **platform:** Both
- **priority:** Must
- **definition of done:** AC-15 to AC-17 pass on both platforms, including the shared test vector.

### T-09 Encrypted local store and AppSettings
- **purpose:** Open the app's encrypted database and seed the settings row every feature reads.
- **layer:** Data
- **what to build:** This is the main ledger, in the strictest class (Ton Q-30); it is never placed in an App Group container. iOS: a SwiftData `ModelContainer` in the app's own Application Support with `FileProtectionType.complete`; the store file has `isExcludedFromBackup = true`, because the key is device-only and a restored copy could never be opened (cross-device restore is E05 iCloud Backup). Android: Room on SQLCipher (`SupportOpenHelperFactory` with the DEK). Schema V1 / Room 1 contains `AppSettings` as in T-02, seeded once on first launch. `AppSettingsRepository` uses identical method names on both platforms. `cycleStartDay` accepts 1–31 (Ton Q-15); `cycleStartIsLastDay` is a plain bool.
- **error behaviour:** Open failure → T-10 with `STORE-DB-01`. An invalid update throws `VALIDATION-CYCLE-01` and keeps the stored value.
- **depends on:** T-02, T-07
- **platform:** Both
- **priority:** Must
- **definition of done:** Unit / instrumented tests AC-18 and AC-19 pass; QA confirms AC-20 (encrypted file).

### T-10 Store failure screen
- **purpose:** Tell the user the data can't be opened, without losing or exposing anything.
- **layer:** UI
- **what to build:** A full-screen state (id `storeError.screen`) shown instead of the tab shell when T-07 or T-09 fails. It shows the error code (`STORE-KEY-01` or `STORE-DB-01`, id `storeError.code`) and a Retry button (`storeError.retry`, at least 44pt / 48dp). Retry runs the key and store opening again. Copy and layout come from ux-ui-designer (**DG-22**); until then, use tokens and the code only.
- **error behaviour:** Retry failure keeps the screen and the code. Data is never deleted automatically. The log gets the code only.
- **depends on:** T-06, T-07, T-09
- **platform:** Both
- **priority:** Must
- **definition of done:** UI tests AC-21 and AC-22 pass, using an injected failing key store.

### T-11 Platform hardening
- **purpose:** Close the platform-level leaks: backups, cleartext traffic, network on launch.
- **layer:** Platform
- **what to build:** Android: keep `allowBackup="false"`; add `dataExtractionRules` (API 31+) and `fullBackupContent` (API 28–30) that exclude `databases/`, `shared_prefs/` and `no_backup/`; set `usesCleartextTraffic="false"` and a `network_security_config` with `cleartextTrafficPermitted="false"`; R8 is on for release. iOS: no `NSAllowsArbitraryLoads` or other ATS exceptions in `Info.plist`. The foundation makes **no network calls**.
- **error behaviour:** A cleartext request (test only) fails with a platform error. The app never retries it over HTTP.
- **depends on:** T-03, T-04
- **platform:** Both
- **priority:** Must
- **definition of done:** AC-23 to AC-26 pass (config greps and a proxy check by QA).

### T-12 Safe logging
- **purpose:** Make it impossible to log user values by accident.
- **layer:** Platform
- **what to build:** `AppLog.event(id:code:)` (Swift) and `AppLog.event(id, code)` (Kotlin) are the only logging API. They take a snake_case event id and an optional error code, with no free-text values. iOS uses `os.Logger` (`privacy: .private` default). Android strips `Log.d` / `Log.v` from release builds with R8 `-assumenosideeffects`. Grep gate: no `print(` or `NSLog(` in `ios-app/App` and `ios-app/Sources`, and no `android.util.Log` calls in `android-app/app/src/main` outside `AppLog`.
- **error behaviour:** The gate failing blocks the build review (backend-lead) and QA.
- **depends on:** T-03, T-04
- **platform:** Both
- **priority:** Must
- **definition of done:** AC-27 and AC-28 pass.

### T-13 Currency formatter: mask and parity table
- **purpose:** Finish the shared amount formatter, so every screen formats and masks money identically.
- **layer:** Domain
- **what to build:** Extend the existing `CurrencyFormatter` (both platforms) with `masked()` → `"฿••••••"` (฿ plus six U+2022 bullets, independent of the amount). Keep `whole` and `detail` with half-up rounding and the U+2212 minus. Copy every T-02 case row into `CurrencyFormatterTests` and `CurrencyFormatterTest`.
- **error behaviour:** Not applicable to the user (pure function). Any input formats, and no exception is thrown for large values (tested up to ฿999,999,999.99).
- **depends on:** T-02
- **platform:** Both
- **priority:** Must
- **definition of done:** AC-29 to AC-33 pass with identical strings on both platforms.

### T-14 Budget cycle boundaries
- **purpose:** Compute which monthly cycle a moment belongs to, in the device timezone.
- **layer:** Domain
- **what to build:** `BudgetCycle.containing(instant, rule, timeZone)` → first and last local date (inclusive) and days in cycle, where `rule` is `.day(n)` (n = 1–31) or `.lastDayOfMonth`. **Month-end clamping (Ton Q-15):** a month's payday is `DayClamp.clamp(year, month, n)` from **T-23** (min(n, days in that month)), so 29–31 snap back to the last valid day of a shorter month and never roll into the next month; `.lastDayOfMonth` resolves to each month's final day. T-14 must not contain its own clamp code (Ton Q-53: one shared function). The cycle runs from the payday on or before the local date of `instant` to the day before the next month's payday. `BudgetCycle.dayIndex(today)` → days elapsed (including today) and **days left** (including today: (cycle end − today) + 1, Ton Q-48; this is the Home badge count and the per-day divisor).
- **error behaviour:** `.day(n)` with n outside 1–31 throws `VALIDATION-CYCLE-01`, with no date in the message.
- **depends on:** T-02, T-23
- **platform:** Both
- **priority:** Must
- **definition of done:** AC-34 to AC-38, AC-37a and AC-38a to AC-38e pass on both platforms with the T-02 case rows.

### T-15 Cash-flow totals
- **purpose:** One shared In / Out / Net function for Home, History and Analytics.
- **layer:** Domain
- **what to build:** `CashFlow.totals(items)`, where an item is (type expense|income|transfer, amount Decimal > 0, currency). It returns `inTotal`, `outTotal` and `net = in − out` as Decimal. Transfers, including card payments, are excluded. Only THB items are summed in this feature; other currencies throw `VALIDATION-CURRENCY-01` (multi-currency is E27, Q-27).
- **error behaviour:** An amount <= 0 throws `VALIDATION-AMOUNT-01`, with no amount in the message.
- **depends on:** T-02
- **platform:** Both
- **priority:** Must
- **definition of done:** AC-39 to AC-42 pass on both platforms.

### T-16 Budget status
- **purpose:** One shared function for the Budget hero's numbers and status.
- **layer:** Domain
- **what to build:** `BudgetStatus.evaluate(budget: Decimal?, spent: Decimal, committedUnpaid: Decimal = 0, daysElapsed, daysInCycle)` returns `leftToSpend = budget − spent − committedUnpaid` (**Safe to Spend, Ton Q-51 B**; revision 6: `committedUnpaid` = the sum of upcoming **and overdue** unpaid fixed costs of **every kind** (bills, subscriptions, installments, whatever the paying account) due in the active cycle (Ton Q-55, Q-58), computed by E11-T19 and passed in; 0 until E11 ships), `percentUsed = spent / budget` (exact Decimal, not rounded; actual spent only, `committedUnpaid` is not added), `elapsed = daysElapsed / daysInCycle`, `status` (`onTrack` when percentUsed <= elapsed; `overPace` when percentUsed > elapsed and <= 1; `overBudget` when > 1; `noBudget` when budget is nil), and `overBy = −leftToSpend` (= spent − budget + committedUnpaid) when overBudget (revision 7, Ton Q-61: the Over budget caption always equals abs(Left to spend); with committedUnpaid 0 this is spent − budget). `spent` is the sum of expenses only (from T-15 `outTotal`); income never reduces it. `leftToSpend` may be negative while spent ≤ budget (set-aside fixed costs larger than what is left); the function returns the exact value (never clamped to 0) and, revision 6 (Ton Q-54), `billsExceedBy = −leftToSpend` when leftToSpend < 0 and status is `onTrack` or `overPace` (absent otherwise), which feeds the hero helper "Bills exceed budget by ฿x" in E03. When status is `overBudget`, `billsExceedBy` is absent and `overBy` carries the full deficit, including set-aside fixed costs (State B, Ton Q-61). `committedUnpaid` also includes overdue charges carried from earlier cycles (Ton Q-60); E11-T19 computes that sum, so T-16 does not change for it. Per-day allowance and % display are in T-18 and T-19; the Forecast (E18) uses this same `leftToSpend` as its daily-spending amount (Ton Q-51 A).
- **error behaviour:** budget <= 0, spent < 0, committedUnpaid < 0, or daysElapsed outside 1…daysInCycle throws `VALIDATION-BUDGET-01`, with no values in the message.
- **depends on:** T-02, T-14, T-15
- **platform:** Both
- **priority:** Must
- **definition of done:** AC-43 to AC-47, AC-43a, AC-43b, AC-43c, AC-44a, AC-46a, AC-46b and AC-46c pass on both platforms.

### T-17 QA: shell smoke, parity and security checks
- **purpose:** Verify both apps independently: shell behaviour, identical domain results, security baseline.
- **layer:** Platform
- **what to build:** Owner `qa-engineer`. In `qa-automation/tests/test_tab_shell.py` (one body, both platforms), replace the `root.title` smoke with the tab shell checks. Run every `foundation-cases.md` row on both platforms and compare. Run the MASTG checks from `qa-verification` step 6 for storage, crypto, network and backup.
- **error behaviour:** Any mismatch → BLOCKED, routed by the conductor table (developer, or backend-lead when both match the contract but differ).
- **depends on:** T-05 to T-16, T-18 to T-21, T-23, T-24 (T-22 is verified once Q-31 unblocks it)
- **platform:** Both
- **priority:** Must
- **definition of done:** AC-48 to AC-50 pass, every revision-2 AC (AC-51 to AC-64), revision-3 AC (AC-37a, AC-43a, AC-44a, AC-51a, AC-51b), revision-4 AC (AC-38a–AC-38e), revision-5 AC (AC-43b, AC-46a, AC-51c, AC-65 to AC-71) revision-6 AC (AC-43c, AC-46b, AC-51d, AC-54a) and revision-7 AC (AC-46b as amended, AC-46c, AC-51e) passes on both platforms, and `docs/review/foundation-qa.md` is written.

### T-18 Per-day allowance (Ton Q-16)
- **purpose:** One shared rule for "฿x a day left" on the Budget hero.
- **layer:** Domain
- **what to build:** `BudgetStatus.perDayAllowance(leftToSpend, today, cycleEnd)`. Remaining days = (cycleEnd − today) + 1, so today counts and the divisor on the last day is 1. Result = **max(0, floor(leftToSpend / remainingDays))** to whole baht (Ton Q-16, Q-54): if leftToSpend <= 0, the result is ฿0.
- **error behaviour:** today after cycleEnd throws `VALIDATION-CYCLE-02`, with no values in the message.
- **depends on:** T-02, T-14, T-16
- **platform:** Both
- **priority:** Must
- **definition of done:** AC-51 to AC-54, AC-51a, AC-51b, AC-51c, AC-51d, AC-51e and AC-54a pass on both platforms with the case rows.

### T-19 Percentage display rules (Ton Q-16)
- **purpose:** One shared rule for the budget % and the "% vs previous month" figures.
- **layer:** Domain
- **what to build:**
  - `PercentDisplay.budget(spent, budget) -> Int`: spent / budget × 100, rounded half-up to an integer. While spent < budget, the result is capped at 99, so 99.1–99.9% (and anything that would round to 100) shows 99. 100% appears only when spent >= budget; above that, half-up with no cap (Ton set no cap for the budget %).
  - `PercentDisplay.change(current, previous) -> .value(Int) | .overCap | .notComparable`: (current − previous) / previous × 100, rounded half-up (the `caffeine-domain` rounding rule) to an integer. A value above +999 returns `.overCap`, shown as ">999%". previous = 0 returns `.notComparable` (how it is shown is open, Q-41, and decided in E12).
- **error behaviour:** budget <= 0 or a negative input throws `VALIDATION-PERCENT-01`, with no values in the message.
- **depends on:** T-02
- **platform:** Both
- **priority:** Must
- **definition of done:** AC-55 to AC-58 pass on both platforms with the case rows.

### T-20 Splash while the store initialises (Ton Q-04)
- **purpose:** Show a branded splash while keys and the store open, then route.
- **layer:** UI
- **what to build:** A splash (id `splash.screen`), with layout from ux-ui-designer (**DG-01**), shown from launch until T-07 / T-09 finish. On iOS it follows `UILaunchScreen`; on Android, the SplashScreen API. Then: success → the launch gate (F14) → the tab shell; failure → T-10. The launch gate is a single step that E06 fills: when `appLockEnabled` is true it will show the privacy shield + biometric prompt. In foundation it passes straight through, because nothing can set the flag yet. Performance target (Ton): the splash shows for under 0.5 s.
- **error behaviour:** Init failure replaces the splash with `storeError.screen` and never shows Home.
- **depends on:** T-06, T-07, T-09, T-10
- **platform:** Both
- **priority:** Must
- **definition of done:** AC-59 to AC-61 pass.

### T-21 App-switcher privacy shield (iOS, and Android API 33+) (Ton Q-04)
- **purpose:** Always hide app content from the app-switcher snapshot.
- **layer:** Platform
- **what to build:** When the app leaves the foreground (iOS `scenePhase` → inactive / background; Android `onPause`), a full-window shield (id `privacy.shield`, design **DG-26**, tokens only) covers the content before the system takes the snapshot. On return, the shield is removed and the same tab and stack show. This always happens, whatever the App Lock or Privacy Mode setting. On Android API 33+, also call `setRecentsScreenshotEnabled(false)`. Do not set FLAG_SECURE (Q-31).
- **error behaviour:** None visible. If the shield view fails to attach, the content is hidden with a plain `night/bg` window cover.
- **depends on:** T-05, T-06
- **platform:** Both
- **priority:** Must
- **definition of done:** AC-62 to AC-64 pass (QA app-switcher screenshot check).

### T-22 Android API 28–32 app-switcher shield (blocked by Q-31)
- **purpose:** Meet Ton's "always shield" rule on Android versions without `setRecentsScreenshotEnabled`.
- **layer:** Platform
- **what to build:** On API 28–32, the only reliable way to hide the recents thumbnail is `FLAG_SECURE`, which also blocks the user's own screenshots in the whole app. The method is chosen by Ton in **Q-31**; build it once he answers.
- **error behaviour:** Until Q-31 is answered, API 28–32 shows the T-21 shield over the window, which may not be captured in time on every device (recorded in the QA report as "unverified: API 28–32 recents").
- **depends on:** T-21
- **platform:** Android
- **priority:** Should
- **definition of done:** The AC-64 check passes on an API 30 emulator using the method from Q-31.

### T-23 Shared month-day clamp (Ton Q-53, Q-15)
- **purpose:** One function that resolves any "day N of the month" rule, used by payday cycles, recurring commitments and card cut-off / due days.
- **layer:** Domain
- **what to build:** `DayClamp.clamp(year, month, day) -> LocalDate` = the date with day-of-month min(day, days in that month) (Gregorian, leap years included); it always snaps **back** and never rolls into the next month. `DayClamp.nextOccurrence(anchorDay, onOrAfter: LocalDate) -> LocalDate` = the first clamped date on or after the given date, computed from the stored anchor each month, so a 31st rule gives 28 Feb then 31 Mar (no drift). This is the only clamp code in either app: T-14 (payday), E11 / E16 (recurring commitments and income) and E10-T13 (card cut-off and due) call it. A grep gate in review finds no other `min(…, daysInMonth)` / `lengthOfMonth()` clamp outside `DayClamp`.
- **error behaviour:** day outside 1–31 or month outside 1–12 throws `VALIDATION-DAY-01`, with no date in the message.
- **depends on:** T-02
- **platform:** Both
- **priority:** Must
- **definition of done:** AC-65 to AC-68 pass on both platforms with the T-02 case rows (`golden-sample-data.md` §6.2, §6.3).

### T-24 Cycle label and previous cycle (Ton Q-52)
- **purpose:** Name a budget cycle the same way on every screen and find the cycle to compare with.
- **layer:** Domain
- **what to build:** `BudgetCycle.label(cycle) -> CycleLabel` with `long` = "<Mon> cycle · <d Mon> – <d Mon>" (closing month = month of the cycle's last day; English 3-letter month abbreviations; day without a leading zero; U+00B7 middle dot and U+2013 en dash, each with a space on both sides) and `short` = "<Mon> cycle"; `comparison` = "vs <Mon> cycle" built from the previous cycle's closing month. Screens render `long` in their own text style (Caption Upper makes it upper case; the string itself is sentence case). `BudgetCycle.previous(cycle, rule)` → the cycle that ends the day before `cycle` starts, using T-14 / T-23. Year display for past-year cycles and the Thai format come from ux-ui-designer (DG-54) and Q-19; this task covers English only.
- **error behaviour:** a cycle whose first date is after its last date throws `VALIDATION-CYCLE-03`, with no date in the message.
- **depends on:** T-14
- **platform:** Both
- **priority:** Must
- **definition of done:** AC-69 to AC-71 pass on both platforms with identical strings.

## 5. Acceptance criteria

**T-01**
- AC-01: Given Figma `night/shadow` is black at 35% in Dark and black at 12% in Light, When tokens are generated, Then iOS `Night/shadow.colorset` has alpha 0.35 (Dark) and 0.12 (Any), and Android `CaffeineColors.dark.shadow = 0x59000000`, `CaffeineColors.light.shadow = 0x1F000000`.
- AC-01a: Given Figma `night/income-text` is #9EE6C4 in Dark and #1F714C in Light, When tokens are generated, Then iOS `Night/income-text.colorset` has Dark #9EE6C4 and Any #1F714C, and Android `CaffeineColors.dark.incomeText = 0xFF9EE6C4`, `CaffeineColors.light.incomeText = 0xFF1F714C`; and Light `accent` = #CF3D20 (`0xFFCF3D20`), Light `textSecondary` = #636366 (`0xFF636366`).
- AC-01b *edge*: Given `night/on-primary-soft` is #1C1C1E at 88% and Light `night/on-accent-soft` is #FFFFFF at 96%, When tokens are generated, Then iOS `on-primary-soft` has alpha 0.88 in both appearances and Android `onPrimarySoft = 0xE01C1C1E` (round(0.88 × 255) = 224); Android `light.onAccentSoft = 0xF5FFFFFF` (round(0.96 × 255) = 245) and `dark.onAccentSoft = 0xE01C1C1E`; no generated file stores these as an opaque colour plus a separate opacity.
- AC-02: Given generation has finished, When the token diff runs over all `Caffeine / Night` variables in both modes and all `Caffeine / Dimensions` variables, Then it reports 0 differences for iOS and 0 for Android.
- AC-03 *edge*: Given `night/bg-clear` is renamed in Figma, When generation runs, Then it stops with "missing token: night/bg-clear", and the previously generated files are unchanged byte for byte.

**T-02**
- AC-03a: Given the contract is written, When backend-lead checks it, Then `AppSettings` has 9 fields, each classified Internal, the storage layout reserves the V1.1 widget snapshot outside the main store, `cycleStartDay` has range 1–31 and `cycleStartIsLastDay` defaults to false, and the cases file has at least one row for each of AC-29 to AC-47, AC-43b, AC-43c, AC-46a, AC-46b, AC-46c, AC-51c, AC-51d, AC-51e, AC-54a and AC-65 to AC-71 (values from `golden-sample-data.md` revision 4).
- AC-03b *edge*: Given a plan field has no class in `security-standard` §2, When the contract is checked, Then CONTRACT_READY is not set and the field is listed in `docs/status.md` Notes for Ton.

**T-03**
- AC-04: Given a clean checkout, When `xcodegen generate && xcodebuild test -scheme Caffeine -destination id=$SIM_ID` runs, Then it exits 0 and runs `CaffeineTests` and `CaffeineUITests`.
- AC-04a *edge*: Given a file in `ios-app/Sources` contains `try!`, When the build runs, Then SwiftLint fails the build and names that file and line.

**T-04**
- AC-05: Given a clean checkout, When `./gradlew assembleDebug testDebugUnitTest lint` runs, Then it exits 0.
- AC-05a *edge*: Given a file in `android-app/app/src/main` contains `!!`, When static analysis runs, Then it exits non-zero and names that file and line.

**T-05**
- AC-06: Given the device is in Dark appearance, When the app opens, Then the root background is `night/bg` (Dark) and the status bar glyphs use `night/text-primary` (Dark).
- AC-07 *edge*: Given the app is open on Home in Dark, When the device switches to Light, Then the background becomes `night/bg` (Light) without a relaunch, and Home stays selected.

**T-06**
- AC-08: Given a first launch that opened the store, When the shell appears, Then 4 tabs show in the order Home, Wallet, Analytics, Profile, `tab.home` is selected, `home.placeholder` is visible, and no + button exists.
- AC-09 *edge* (Android): Given Wallet is selected, When system back is pressed, Then Home is selected; When back is pressed again, Then the app moves to the background and the process keeps its state.
- AC-10 *edge*: Given Analytics is selected, When `tab.analytics` is tapped again twice, Then Analytics stays selected at its root and its navigation stack depth is 1.
- AC-10a: Given each tab button, When its frame is measured, Then the hit area is at least 44×44pt (iOS) / 48×48dp (Android).

**T-07**
- AC-11: Given a fresh install, When first launch finishes, Then exactly 1 wrapped DEK exists (iOS Keychain item with accessibility `WhenUnlockedThisDeviceOnly`; Android file in `no_backup/`), and the 32 raw DEK bytes appear in no file under the app container.
- AC-12: Given the app was launched once, When it is relaunched, Then the unwrapped DEK equals the first-launch DEK (test hook compares SHA-256 of both), and no new wrapped DEK is created.
- AC-13 *edge*: Given the key store throws on unwrap (injected), When the app launches, Then `storeError.screen` shows `STORE-KEY-01`, and the wrapped DEK and store file are not deleted.
- AC-14 *security*: Given an Android device backup (`adb backup` or a Google cloud backup test) or an unencrypted iOS device backup, When it is inspected, Then it contains neither the wrapped DEK nor the KEK.

**T-08**
- AC-15: Given key K, plaintext "dinner with Ploy", the fixed recordId uuid from `foundation-cases.md`, field `memo` and schema 1, When `seal` runs twice, Then the two outputs differ, and both `open` to "dinner with Ploy".
- AC-16 *edge*: Given a value sealed with field `memo`, When `open` is called with field `merchant`, Then it throws `CIPHER-AUTH-01` and returns no bytes.
- AC-17: Given the test vector in `foundation-cases.md`, When the iOS and Android `open` run on the same ciphertext hex, Then both return the vector's plaintext.

**T-09**
- AC-18: Given a fresh install, When first launch finishes, Then `AppSettings` has exactly 1 row: currencyCode "THB", cycleStartDay 1, cycleStartIsLastDay false, themePreference "system", onboardingCompleted false, appLockEnabled false, privacyModeEnabled false.
- AC-19 *edge*: Given AppSettings has cycleStartDay 1, When `update(cycleStartDay: 32)` or `update(cycleStartDay: 0)` is called, Then it throws `VALIDATION-CYCLE-01` and the stored value is still 1; When `update(cycleStartDay: 31)` is called, Then the stored value is 31 (Ton Q-15).
- AC-20 *security*: Given the app has written AppSettings, When the Android database file is opened with plain SQLite (no key), Then opening fails with "file is not a database"; and on iOS the store file's `FileProtectionType` is `complete` and `isExcludedFromBackup` is true.

**T-10**
- AC-21: Given the store fails to open (injected), When the app launches, Then `storeError.screen` shows `STORE-DB-01` and no tab is shown; When `storeError.retry` is tapped and the injected failure is cleared, Then Home appears with `tab.home` selected.
- AC-22 *edge*: Given the failure persists, When Retry is tapped 3 times, Then the screen still shows `STORE-DB-01`, the store file size is unchanged, and the log has 4 entries `store_open_failed / STORE-DB-01` with no other values.

**T-11**
- AC-23: Given the iOS `Info.plist`, When it is searched, Then `NSAppTransportSecurity` has no `NSAllowsArbitraryLoads`, `NSAllowsArbitraryLoadsInWebContent` or exception domains.
- AC-24: Given the Android manifest, When it is read, Then `allowBackup="false"`, `usesCleartextTraffic="false"`, `networkSecurityConfig` sets `cleartextTrafficPermitted="false"`, and the data extraction rules exclude `databases`, `sharedpref` and `no_backup`.
- AC-25 *edge*: Given an instrumented test issues `GET http://example.com`, When it runs, Then the request fails with a cleartext-not-permitted error (Android) / ATS error (iOS).
- AC-26 (offline, F9): Given airplane mode is on and it is a first launch, When the app opens, Then the shell shows Home, and a proxy / network monitor records 0 requests during launch and 3 tab switches.

**T-12**
- AC-27: Given the source tree, When the grep gate runs, Then `print(` and `NSLog(` have 0 matches in `ios-app/App` and `ios-app/Sources`, and `Log.d(`, `Log.v(`, `Log.i(`, `Log.w(`, `Log.e(` and `println(` have 0 matches in `android-app/app/src/main` outside `AppLog`.
- AC-28 *edge*: Given `AppLog.event("store_open_failed", code: "STORE-DB-01")`, When the log is captured, Then the line contains exactly `store_open_failed` and `STORE-DB-01`, and the API offers no parameter that accepts an amount or free text.

**T-13**
- AC-29: Given 6450 with sign expense, When `whole` runs, Then the result is "−฿6,450" (U+2212 minus).
- AC-30: Given 52000 with sign income, When `whole` runs, Then the result is "+฿52,000".
- AC-31: Given 320 with sign expense, When `detail` runs, Then the result is "−฿320.00".
- AC-32 *edge*: Given 2.5 neutral, When `whole` runs, Then "฿3" (half-up, not banker's "฿2"); Given 0.005 neutral, When `detail` runs, Then "฿0.01"; Given 999999999.99 neutral, When `detail` runs, Then "฿999,999,999.99". Both platforms give identical strings.
- AC-33 *security* (F10): Given any amount, e.g. 6450, When `masked()` runs, Then the result is "฿••••••" and its length does not depend on the amount (6450 and 2400000 give the same string).

**T-14**
- AC-34: Given startDay 1 and time zone Asia/Bangkok, When `containing(2026-11-30T16:30:00Z)` runs (23:30 on 30 Nov local), Then the cycle is 2026-11-01 to 2026-11-30 with 30 days.
- AC-35 *edge*: Given startDay 1 and Asia/Bangkok, When `containing(2026-11-30T17:30:00Z)` runs (00:30 on 1 Dec local), Then the cycle is 2026-12-01 to 2026-12-31 with 31 days.
- AC-36: Given startDay 25 and local date 2026-11-24, When `containing` runs, Then the cycle is 2026-10-25 to 2026-11-24 with 31 days.
- AC-37: Given the cycle 2026-11-01 to 2026-11-30 and today 2026-11-18, When `dayIndex` runs, Then days elapsed = 18 and days remaining = 13.
- AC-37a (payday cycle, revision 3): Given startDay 25 (payday), Asia/Bangkok and today 2026-11-18, When `containing` and `dayIndex` run, Then the cycle is 2026-10-25 to 2026-11-24 with 31 days, days elapsed = 25 and days remaining = 7 (today counted in both).
- AC-38 *edge* (F11): Given rule `.day(0)` or `.day(32)`, When `containing` runs, Then it throws `VALIDATION-CYCLE-01`, whose message contains no date.
- AC-38a *edge* (clamping, Ton Q-15): Given rule `.day(31)`, Asia/Bangkok and local date 2027-02-15, When `containing` and `dayIndex` run, Then the cycle is 2027-01-31 to 2027-02-27 with 28 days (the February payday is 28 Feb, not 3 Mar), and days left = 13.
- AC-38b *edge*: Given rule `.day(31)` and local date 2027-03-10, Then the cycle is 2027-02-28 to 2027-03-30 with 31 days; Given local date 2027-04-15, Then the cycle is 2027-03-31 to 2027-04-29 with 30 days (April payday clamps to 30 Apr).
- AC-38c *edge* (leap year): Given rule `.day(31)` and local date 2028-02-10, Then the cycle is 2028-01-31 to 2028-02-28 with 29 days (the February payday is 29 Feb 2028); Given rule `.day(29)` and local date 2027-02-28, Then the cycle is 2027-02-28 to 2027-03-28 with 29 days.
- AC-38d *edge*: Given rule `.day(30)` and local date 2027-03-15, Then the cycle is 2027-02-28 to 2027-03-29 with 30 days (the March payday stays 30 Mar).
- AC-38e (Last day of the month): Given rule `.lastDayOfMonth` and local dates 2027-02-15 and 2027-04-15, Then the cycles are 2027-01-31 to 2027-02-27 and 2027-03-31 to 2027-04-29, identical to `.day(31)` for the same dates (glossary G-6).

**T-15**
- AC-39: Given income 52,000, expenses 20,000 and 13,550, and a card payment transfer of 5,000, When `totals` runs, Then in = 52,000, out = 33,550, net = 18,450 (formatted "+฿52,000", "−฿33,550", "+฿18,450").
- AC-40 *edge*: Given only one transfer of 5,000, When `totals` runs, Then in = 0, out = 0, net = 0 (net formatted neutral "฿0").
- AC-41 *edge*: Given an empty list, When `totals` runs, Then in, out and net are all 0.
- AC-42 *edge*: Given an expense with amount 0, When `totals` runs, Then it throws `VALIDATION-AMOUNT-01` with no amount in the message.

**T-16**
- AC-43: Given budget 40,000, spent 33,550, day 18 of 30, When `evaluate` runs, Then leftToSpend = 6,450, percentUsed = 0.83875, elapsed = 0.6, status = overPace.
- AC-43a (payday cycle, revision 3): Given budget 40,000, spent 33,550, day 25 of 31, When `evaluate` runs, Then leftToSpend = 6,450, percentUsed = 0.83875, elapsed = 25/31 (0.806…), status = overPace.
- AC-43b (Safe to Spend, Ton Q-51 B, revision 5): Given budget 40,000, spent 33,550, committedUnpaid 599 (AIS due 22 Nov, unpaid) and day 25 of 31, When `evaluate` runs, Then leftToSpend = 5,851, percentUsed = 0.83875 (the 599 is not added), elapsed = 25/31 and status = overPace.
- AC-44 *edge*: Given budget 40,000, spent 24,000, day 18 of 30, When `evaluate` runs, Then percentUsed = 0.6 = elapsed and status = onTrack.
- AC-44a *edge* (revision 3): Given budget 40,000, spent 32,000, day 25 of 31, When `evaluate` runs, Then percentUsed = 0.8 <= elapsed 25/31 and status = onTrack (the Figma 1B frame shows Over pace with this data; code follows the rule).
- AC-45 *edge*: Given budget 40,000, spent 40,000, day 18 of 30, Then leftToSpend = 0 and status = overPace; Given spent 41,200, Then status = overBudget and overBy = 1,200 (caption "Over budget by ฿1,200").
- AC-46 *edge* (F11): Given budget nil and spent 33,550, Then status = noBudget; Given budget 0, Then it throws `VALIDATION-BUDGET-01` with no values in the message.
- AC-46a *edge* (revision 5, F11): Given committedUnpaid −1, When `evaluate` runs, Then it throws `VALIDATION-BUDGET-01` with no values in the message; Given budget 40,000, spent 39,800, committedUnpaid 599 and day 25 of 31, Then leftToSpend = −399 (exact, not clamped to 0), percentUsed = 0.995, status = overPace, overBy is absent and (revision 6, Ton Q-54) billsExceedBy = 399.
- AC-43c (revision 6, Ton Q-55): Given budget 40,000, spent 0, committedUnpaid 14,447 (Rent 12,000 + Spotify 139 + iPhone installment 1,290 + Netflix 419 + AIS 599, all due in the Dec cycle 25 Nov – 24 Dec 2026) and day 1 of 30, When `evaluate` runs, Then leftToSpend = 25,553, percentUsed = 0, status = onTrack and billsExceedBy is absent.
- AC-46b *edge* (revision 6, Ton Q-54): Given budget 40,000, spent 40,000, committedUnpaid 599 and day 25 of 31, When `evaluate` runs, Then leftToSpend = −599, status = overPace (1.0 is not > 1) and billsExceedBy = 599; Given spent 41,200 and committedUnpaid 599, Then leftToSpend = −1,799, status = overBudget, **overBy = 1,799** (revision 7, Ton Q-61: caption "Over budget by ฿1,799", equal to abs(leftToSpend)) and billsExceedBy is absent.
- AC-46c *edge* (revision 7, Ton Q-60): Given budget 40,000, spent 0, committedUnpaid 15,046 (the 5 Dec-cycle charges 14,447 + the Nov AIS 599 carried because it is still unpaid) and day 1 of 30, When `evaluate` runs, Then leftToSpend = 24,954, percentUsed = 0, status = onTrack, and billsExceedBy and overBy are absent.
- AC-47: Given budget 40,000, expenses of 33,550 and income of 52,000 in the cycle, When spent is taken from `CashFlow.totals(...).outTotal` and evaluated on day 18 of 30, Then leftToSpend = 6,450 (income does not reduce spend).

**T-17**
- AC-48: Given both debug builds, When `pytest tests/test_tab_shell.py` runs against iOS and Android, Then tapping `tab.wallet`, `tab.analytics` and `tab.profile` shows `wallet.placeholder`, `analytics.placeholder` and `profile.placeholder` on both platforms.
- AC-49 *edge*: Given every row in `foundation-cases.md`, When QA runs both platforms' test suites, Then every row's output is identical on iOS and Android (0 mismatches).
- AC-50 *security*: Given the MASTG storage, crypto, network and backup checks, When QA runs them on both builds, Then each check is PASS, or a tool gap is written as "unverified: <tool>" (never reported as PASS).

**T-18** (Ton Q-16)
- AC-51: Given leftToSpend 6,450, cycle 2026-11-01 to 2026-11-30 and today 2026-11-18, When `perDayAllowance` runs, Then remaining days = 13 and the result is ฿496 (6,450 / 13 = 496.15, floored).
- AC-51a (payday cycle, revision 3): Given leftToSpend 6,450, cycle 2026-10-25 to 2026-11-24 and today 2026-11-18, When `perDayAllowance` runs, Then remaining days = 7 and the result is ฿921 (6,450 / 7 = 921.43, floored). The Figma hero's "฿1,075" (÷ 6) does not follow Ton Q-16 and is not a test value (master plan DG-48).
- AC-51b *edge* (revision 3): Given leftToSpend 40,000, cycle 2026-11-25 to 2026-12-24 and today 2026-11-25 (first day), When it runs, Then remaining days = 30 and the result is ฿1,333 (40,000 / 30 = 1,333.33, floored; Figma 1I shows ฿1,379).
- AC-51c (revision 5, Ton Q-51): Given leftToSpend 5,851 (from AC-43b), cycle 2026-10-25 to 2026-11-24 and today 2026-11-18, When `perDayAllowance` runs, Then remaining days = 7 and the result is ฿835 (5,851 / 7 = 835.86, floored); Given today 2026-11-21, Then remaining days = 4 and the result is ฿1,462 (1,462.75 floored). The function never returns 835 × 7 as an amount.
- AC-51d (revision 6, Ton Q-55): Given leftToSpend 25,553 (from AC-43c), cycle 2026-11-25 to 2026-12-24 and today 2026-11-25, When `perDayAllowance` runs, Then remaining days = 30 and the result is ฿851 (851.77 floored).
- AC-51e (revision 7, Ton Q-60): Given leftToSpend 24,954 (from AC-46c), the same cycle and today 2026-11-25, When it runs, Then the result is ฿831 (831.8 floored); Given today 2026-11-26, Then remaining days = 29 and the result is ฿860 (860.48 floored).
- AC-52: Given leftToSpend 6,458.40 and 13 remaining days, When it runs, Then the result is ฿496 (496.80 floored, not ฿497).
- AC-53 *edge*: Given today = cycle end (2026-11-30) and leftToSpend 1,200, When it runs, Then remaining days = 1 and the result is ฿1,200 (the badge reads "1 day left", Ton Q-48).
- AC-54 *edge*: Given leftToSpend −1,200 (over budget) or 0, When it runs, Then the result is ฿0; Given today 2026-12-01 with cycle end 2026-11-30, Then it throws `VALIDATION-CYCLE-02` with no values in the message.
- AC-54a *edge* (revision 6, Ton Q-54): Given leftToSpend −399 (from AC-46a), cycle 2026-10-25 to 2026-11-24 and today 2026-11-18, When `perDayAllowance` runs, Then remaining days = 7 and the result is ฿0 (max(0, floor(−399 / 7)) = max(0, −57) = 0), never a negative per-day figure.

**T-19** (Ton Q-16)
- AC-55: Given spent 33,550 and budget 40,000 (83.875%), When `PercentDisplay.budget` runs, Then 84.
- AC-56 *edge*: Given budget 40,000 and spent 39,640 (99.1%), 39,800 (99.5%) or 39,980 (99.95%), When it runs, Then 99 in all three cases.
- AC-57 *edge*: Given budget 40,000 and spent 40,000, Then 100; Given spent 41,200, Then 103; Given spent 0, Then 0.
- AC-58: Given previous 40,000 and current 36,000, When `PercentDisplay.change` runs, Then `.value(−10)`; Given previous 40,000 and current 39,800 (−0.5%), Then `.value(−1)` (half-up, away from zero); *edge:* Given previous 1,000 and current 11,000 (+1,000%), Then `.overCap` (shown ">999%"); Given previous 0, Then `.notComparable`.

**T-20** (Ton Q-04)
- AC-59: Given an installed app on QA's reference iPhone and Pixel (named in `foundation-qa.md`), When it is cold-launched 10 times, Then `splash.screen` shows first and Home appears with the splash visible for under 0.5 s in every run.
- AC-60 *edge*: Given the store fails to open (injected), When the app launches, Then the splash is replaced by `storeError.screen` (`STORE-DB-01`), and `tab.home` never appears.
- AC-61 *edge*: Given a test sets `appLockEnabled = true` in AppSettings, When the app launches, Then the launch gate step is invoked exactly once before the tab shell shows (a test probe records the call). The prompt itself is E06.

**T-21** (Ton Q-04)
- AC-62 *security*: Given Home is showing, When the app goes to the background, Then `privacy.shield` covers the whole window before the snapshot, and the app-switcher image shows no tab placeholder text and no amount (QA screenshot of the app switcher, iOS and Android API 33+).
- AC-63 *edge*: Given the shield is showing and App Lock is off, When the app returns to the foreground, Then the shield is removed and the previously selected tab (Wallet in the test) is still selected.
- AC-64 *edge*: Given Android API 34, When the app is in recents, Then `setRecentsScreenshotEnabled(false)` is in effect (no content in the thumbnail), and FLAG_SECURE is not set (a user screenshot of the foreground app still works).

**T-23** (Ton Q-53, Q-15)
- AC-65: Given day 31, When `DayClamp.clamp` runs for (2027, 2), (2028, 2), (2027, 4) and (2027, 3), Then the results are 2027-02-28, 2028-02-29, 2027-04-30 and 2027-03-31; Given day 15 and (2027, 2), Then 2027-02-15.
- AC-66 *edge*: Given day 29 or 30 and (2027, 2), When `clamp` runs, Then the result is 2027-02-28 in both cases (never 2027-03-01 or 2027-03-02); Given day 29 and (2028, 2), Then 2028-02-29.
- AC-67 *edge* (no drift): Given anchor day 31, When `nextOccurrence` is called with onOrAfter 2027-01-01 and then with the day after each result, Then the results are 2027-01-31, 2027-02-28, 2027-03-31, 2027-04-30, 2027-05-31; Given anchor day 30 (a card due day) and onOrAfter 2027-02-15, Then the result is 2027-02-28, 13 days later (`golden-sample-data.md` §6.3).
- AC-68 *edge* *security* (F11): Given day 0, day 32 or month 13, When `clamp` runs, Then it throws `VALIDATION-DAY-01` and the message contains no date or day number.

**T-24** (Ton Q-52)
- AC-69: Given the cycle 2026-10-25 to 2026-11-24, When `BudgetCycle.label` runs, Then `long` = "Nov cycle · 25 Oct – 24 Nov", `short` = "Nov cycle" and `comparison` = "vs Oct cycle"; When `previous` runs with rule `.day(25)`, Then the cycle is 2026-09-25 to 2026-10-24 and its `long` = "Oct cycle · 25 Sep – 24 Oct". Both platforms return byte-identical strings (U+00B7, U+2013).
- AC-70 *edge*: Given rule `.day(1)` and local date 2026-11-18, Then `long` = "Nov cycle · 1 Nov – 30 Nov"; Given rule `.day(31)` and local date 2027-02-15, Then `long` = "Feb cycle · 31 Jan – 27 Feb" and `previous` is 2026-12-31 to 2027-01-30, "Jan cycle · 31 Dec – 30 Jan"; Given rule `.day(25)` and local date 2027-01-10, Then `long` = "Jan cycle · 25 Dec – 24 Jan" and `comparison` = "vs Dec cycle".
- AC-71 *edge* *security* (F11): Given a cycle with first date 2026-11-24 and last date 2026-10-25, When `label` runs, Then it throws `VALIDATION-CYCLE-03` and the message contains no date.

## 6. Screen map
| State | Journey step | v5.1 Dark node | Light | Notes |
|---|---|---|---|---|
| Tab bar, Home selected | H1 (journey 02) | `448:6722` (tab bar only) | twin +482pt, from the ux spec | Use DS Tab bar `State=No add` `272:990` |
| Tab bar, Wallet selected | W-A (journey 07) | `448:11831` (tab bar only) | twin | |
| Tab bar, Analytics selected | 4A (journey 09) | `448:6926` (tab bar only) | twin | |
| Tab bar, Profile selected | 7A (journey 12) | `448:29581` (tab bar only) | twin | Profile tab hosts Settings |
| Tab root placeholders | none | none | none | **Design gap DG-23**: scaffold only, never shipped to beta; ux-ui-designer confirms no design is needed |
| Store error screen | none | none | none | **Design gap DG-22**: copy and layout needed before beta |
| Splash | none (journey 01 gap) | none | none | **Design gap DG-01** (splash under 0.5 s, wordmark `448:5314` is the brand asset) |
| App-switcher privacy shield | none | none | none | **Design gap DG-26** (the same shield is reused by E06 behind the App Lock prompt) |

## 7. Analytics
N/A — no KPI.

## 8. Security
| Task | Data touched (class) | Security AC |
|---|---|---|
| T-02 | AppSettings (Internal), wrapped DEK (Restricted) | AC-03a, AC-03b |
| T-07 | DEK / KEK (Restricted) | AC-11, AC-14 |
| T-08 | Restricted fields (memo, merchant, numbers) | AC-15, AC-16 |
| T-09 | AppSettings (Internal), store file | AC-20 |
| T-10 | error codes only (Public) | AC-22 (log holds the code only) |
| T-11 | the whole container (all classes) | AC-24, AC-26 |
| T-12 | logs (must hold no Confidential or Restricted data) | AC-27, AC-28 |
| T-13 | amounts (Confidential) | AC-33 |
| T-14 / T-15 / T-16 | dates, amounts, budget (Confidential, in memory only) | AC-38, AC-42, AC-46 (errors carry no values) |
| T-17 | all | AC-50 |
| T-18 / T-19 | amounts, budget (Confidential, in memory only) | AC-54 (errors carry no values) |
| T-16 (rev 5) | committed unpaid bills sum (Confidential, in memory only) | AC-46a (error carries no values) |
| T-23 / T-24 | dates, cycle labels (Confidential, in memory only) | AC-68, AC-71 (errors carry no date) |
| T-20 | none shown; store init only | AC-60 |
| T-21 / T-22 | everything on screen (Confidential, Restricted) | AC-62, AC-64 |
Threat model: `docs/security/foundation-threats.md` (T-02, backend-lead).

## 9. Open questions (top 2 for this feature; neither blocks starting it)
1. **Q-31 Android API 28–32 shield:** "Always shield" needs FLAG_SECURE there, which also blocks user screenshots everywhere. Accept, or accept a best-effort shield on API 28–32? (blocks T-22 only)
2. **Q-41 % vs previous month when the previous month is ฿0:** T-19 returns `.notComparable`; how it is shown is decided in E12. Also noted: Ton's ">999%" cap applies to "% vs previous month" only; the budget % has no cap in his answer.

Answered by Ton on 2026-11-21 and applied here: Q-16 (T-18, T-19), Q-04 (T-20, T-21), Q-30 (T-02, T-09). Q-24 Android font stays at the Roboto default (non-blocking). Applied in revision 3 from the CLAUDE.md audit fix record: payday = cycle start (T-02, AC-37a, AC-43a, AC-51a). Applied in revision 4 (decisions file Part 3): Q-15 month-end clamping and "Last day of the month" (T-02, T-09, T-14, AC-38a–AC-38e); Q-48 days left counts today, last day = 1 (T-14 `dayIndex`, AC-53). Applied in revision 5 (decisions file Part 4): Q-53 one shared clamp (T-23, T-14), Q-52 cycle label + previous cycle (T-24), Q-51 B Safe to Spend input (T-16, AC-43b, AC-46a, AC-51c). Applied in revision 6 (decisions file Part 5): Q-55 every fixed-cost kind, Q-58 overdue (T-16 `committedUnpaid`, AC-43c, AC-51d), Q-54 negative Left to spend (T-16 `billsExceedBy`, T-18 max(0, …), AC-46a, AC-46b, AC-54a); Q-56 and Q-57 need no foundation change. Applied in revision 7 (decisions file Part 6): Q-61 full-deficit caption (T-16 `overBy` = −leftToSpend, AC-46b amended), Q-60 carry-forward (no T-16 change; AC-46c, AC-51e show the carried sum); Q-59 and Q-62 need no foundation change. Golden figures for case rows: `docs/plan/golden-sample-data.md` revision 4.

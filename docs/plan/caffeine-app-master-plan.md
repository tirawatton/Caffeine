# Caffeine app — master plan and backlog

Author: `ba` · 2026-11-21 (revision 4, after Ton's second-round answers; revision 3 was the v5.1 UX/UI audit fix pass) · Scope: the whole app, iOS (`ios-app/`) + Android (`android-app/`), platform scope **Both**
Sources: Figma v5.1 page `446:10036` and Feature Journeys `482:29722` (via `docs/design/figma-inventory-v5.1.md`), `CLAUDE.md` (incl. "v5.1 — UX/UI audit fix pass (21 Nov 2026)"), `docs/design/ux-audit-v5.1-2026-11-21.md` (findings 01–21 + fix status), `docs/design/tokens-changelog.md`, `docs/agentic-workflow.md`, the `caffeine-domain` and `security-standard` skills, the repo state on 2026-11-21, and **Ton's binding decisions in [`docs/decisions/2026-11-21-ton-answers.md`](../decisions/2026-11-21-ton-answers.md)** (where they conflict with Figma or revision 1, the decisions win).

**Revision 4 (2026-11-21) in one paragraph:** Ton answered Q-48, Q-15, Q-47, Q-49, Q-50 and findings 13–15 (decisions file Part 3, which also now holds the payday-cycle rule A1 and the card due-date rule A2). Home reads **"7 days left · ฿921/day"** and the last day reads "1 day left"; payday 29–31 **clamps** to the last valid day of short months, plus a "Last day of the month" option; the forecast ends on the **current cycle end** and its daily-spending line matches Home's ฿921 (E18 unblocked, with the line totals provisional on new Q-51); the Figma "9:41" stays (DG-50 won't-fix, builds use the native status bar); the DS values on Home v5 become the global standard (DG-52). New drafts: [`golden-sample-data.md`](golden-sample-data.md) and [`glossary.md`](glossary.md). New questions Q-51 (forecast line totals), Q-52 (period labels under a payday cycle), Q-53 (card days 29–31; Ton's clamping answer names payday only).

**Revision 3 (2026-11-21) in one paragraph:** the audit fix pass changed the design in ways that change the backlog. Onboarding page 3 is now Fixed costs (household stays V2.0); Sign in no longer promises cloud sync; Sync & devices is marked V2.0 with no web app; **the budget cycle follows payday (25th–24th)**; **the card payment due date drives the due badge, reminders and forecast** (cut-off = statement date only); a new `night/income-text` token and 7 token value changes; destructive text on raised surfaces moved to a `night/bg` container; the ✓ Paid badge is fixed. Where the redesigned frames compute a derived figure differently from Ton's Q-16 rule (per day ÷ 6 instead of ÷ 7), **Q-16 wins** (DG-48). Changes: §0, §2, §3, §5 rules 3, 4, 10–12, E00, E03, E04, E05, E10 (new E10-T13), E11, E13, E18, E19, E23, §6.1 (new screen map delta), §7 (DG-34 closed, DG-47–DG-50 new, deferred findings 13–15), §8 (Q-15 partly answered, Q-47–Q-50 new).

This is the **backlog**, not a feature plan. Each epic below becomes one `/caffeine-pipeline <feature> both` run. `ba` then writes `docs/plan/<feature>-plan.md` with the full 8-field tasks and complete ACs (the `ba-planning` checklist). The first one, `docs/plan/foundation-plan.md`, is written and ready (revision 2).

---

## 0. Start here (any agent)

| Question | Answer |
|---|---|
| What stage are we at? | Design v5.1 is complete for most of V1.0 (with design gaps, §7). Code: both apps are **scaffolds only**: a placeholder root view, `CurrencyFormatter` with a parity test, and an Appium smoke test. No feature has gone through the pipeline yet. Ton answered 11 blockers on 2026-11-21. |
| What runs next? | `/caffeine-pipeline foundation both`. Status is `PLAN_READY`, so **ux-ui-designer** (T-01 tokens, DG-01 splash, DG-22 store error, DG-23 placeholders, DG-26 privacy shield) **∥ backend-lead** (T-02 contract with the storage layout, cases including the Q-16 rounding rows, threat model) start in parallel. Then GATE 1 (Ton), then ios-developer ∥ android-developer. |
| After foundation? | Follow the V1.0 build order in §4. For each, `ba` writes the feature plan when the conductor starts it. |
| What can't start yet? | Tasks marked "blocked" in §6, until the open question (§8.1) is answered or ux-ui-designer closes the design gap (§7). |
| Where are the rules? | Money / budget / pace: `caffeine-domain`, plus Ton's Q-16 rounding (§5 rule 9 until the skill is updated). Security: `security-standard` + `docs/security/exceptions.md`. Tokens: `design-tokens`. Lessons: `docs/lessons.md` (read first). |

### 0.1 Master-plan readiness checklist (revision 4, Verify pass 2 of 3)
Revision 4 re-ran all 9 checks: **9/9 PASS on pass 2.**
- Pass 1 failed check 6: the golden sheet's last-day row first showed "87%". Re-derived: (33,550 + 599) / 40,000 = 85.37% → 85%.
- Pass 1 also failed check 8: Ton's Q-15 answer names payday only, but the old Q-15 also asked about card cut-off / due days 29–31. Applying the clamp to cards too would be an assumption, so it is new Q-53.
- Pass 2 is clean. The checks below were all re-run and still hold with the revision 4 figures (7 days left, ฿921/day, the clamping dates in foundation AC-38a–e, forecast horizon 24 Nov, golden reconciliation §8).

Revision 3 checks (still PASS):
1. PASS: every journey 01–13 and 15–17 maps to at least one epic (14 is the gaps page, §7/§8).
2. PASS: every Dark frame in the inventory (sections A–M) is referenced by a task, or by an epic in a later release. The replaced household onboarding frames `614:37371` / `614:37475` are listed in §6.1 as "do not build".
3. PASS: every task has an id, title, owner role, platform, dependencies and Figma frames (or "none" / a DG id).
4. PASS: every epic has key ACs in Given / When / Then with concrete values, including at least one error or edge AC and one security AC.
5. PASS: no dependency cycles. The build order (§4) is a topological order of the epic dependencies (new E10-T13 sits inside E10; E13-T03 and E18-T01 depend on it, and E10 precedes E13 and E18 in §4).
6. PASS: every number agrees with `caffeine-domain` and Ton's Q-16 rules: per day ฿921 = floor(6,450 / 7) for the payday cycle 25 Oct–24 Nov on 18 Nov (Figma's ฿1,075 = 6,450 / 6 is a design error, DG-48); ฿496 = floor(6,450 / 13) for a 1st-of-month cycle; elapsed 25 / 31 on 18 Nov; budget % 99% rule; "Due in 22 days" from 18 Nov to 10 Dec.
7. PASS: every undesigned screen is a Design gap (DG-xx) routed to ux-ui-designer, with the tasks it blocks.
8. PASS: every answered question links to the decisions file or the CLAUDE.md design record; every remaining or new question names the tasks it blocks; no answer is assumed.
9. PASS: every epic that touches user data names its data classes; the Q-30 exception is recorded as EX-001.

**Revision 3 verify log:**
- Pass 1 failed check 6: the redesigned frames (and the hand-off note "per-day = left ÷ days left") give "฿1,075/day" on 18 Nov and "29 days left / ฿1,379" on 25 Nov, which divide by the days *after* today. Every AC was re-derived from Q-16 instead (÷ 7 → ฿921; ÷ 30 → ฿1,333; ฿40,000 ÷ 7 → ฿5,714), and a lesson was logged (second time this happened).
- Pass 1 also failed check 8: the "days left" badge count (6 or 7 on 18 Nov) is not covered by Q-16, which defines only the per-day divisor. It is new question Q-48, not an assumption.
- Pass 2 is clean.

**Revision 2 verify log:**
- Pass 1 failed check 5: E16 and E18 still depended on E15 budget-cycle, which Ton's roadmap does not place. They now depend on E03 (the monthly budget from O5) and E11.
- Pass 1 also failed check 8: E13's notification copy named a category, which conflicts with `security-standard` §2. This is new question Q-40, not a decision.
- Pass 2 is clean.

**Revision 1:**
- Pass 1 failed on 9O `448:31560` and `501:28956` being unmapped, an untestable E03 AC, and a wrong task count.
- Pass 2 was clean.

### 0.2 Legend
- **Owner:** `BA` = ba · `UX` = ux-ui-designer · `LEAD` = backend-lead · `IOS` = ios-developer · `AND` = android-developer · `DEV` = the same task built by **both** ios-developer and android-developer (one task per lane, identical ACs, identical results) · `QA` = qa-engineer.
- **Figma:** v5.1 **Dark** node ids. Every Dark frame has a Light twin 482pt to the right on page `446:10036`; ux-ui-designer lists both in the spec. DS = Design System component.
- **Ton** = decided in `docs/decisions/2026-11-21-ton-answers.md` (question id in brackets).
- **Gate tasks (every epic has these; not repeated in the tables):** `Exx-G1` feature plan (BA) → `Exx-G2` spec + screenshots + a11y + token update (UX) ∥ `Exx-G3` contract + cases + threat model (LEAD) → **GATE 1, Ton approves** → build tasks → `Exx-G4` QA → `Exx-G5` review + beta (LEAD) → **GATE 2, Ton releases**.
- A task marked "moved" keeps its id for traceability and is not counted.

---

## 1. Current state (2026-11-21)

| Area | State |
|---|---|
| `ios-app/` | XcodeGen `project.yml` (iOS 18, Swift 6, strict concurrency, bundle `com.tonapps.caffeine` placeholder, no AppIcon, no signing), placeholder `RootView`, `CurrencyFormatter.swift` + tests, `.swiftlint.yml`, empty `Sources/{Features,Models,Repositories,Shared/*}`. |
| `android-app/` | Gradle KTS, AGP 8.7.3 / Kotlin 2.1.0 / Compose BOM 2024.12.01 (to update), minSdk 28, placeholder `MainActivity`, `CurrencyFormatter.kt` + test, `values` / `values-th`, `allowBackup=false`. No Room, Navigation or SQLCipher yet; comments name removed agents (fixed in foundation T-04). |
| `qa-automation/` | Pytest + Appium, `test_smoke.py`. |
| `docs/` | Master plan, foundation plan, Ton's decisions, `docs/security/exceptions.md` (EX-001). No data models yet (`migrations.md` baseline only), no tokens. |
| Figma | v5.1 page (Dark + Light, sections A–M); Feature Journeys 01–17; App Prototype (its + tap → 1N link is **wrong** per Ton Q-17, DG-46). **UX/UI audit fix pass done 21 Nov 2026** (findings 01–12, 16, 17, 19, 20 fixed; 12 partly, 13–15 deferred by Ton; status table at the end of `docs/design/ux-audit-v5.1-2026-11-21.md`). Token changes are recorded in `docs/design/tokens-changelog.md` only: **the token pipeline does not exist yet** (foundation T-01). |

---

## 2. Release roadmap (Ton Q-10)

| Release | Ton's scope | Epics |
|---|---|---|
| **V1.0 core MVP** | Dashboard (Left to spend + quick actions), Add Transaction (keypad, camera / photo e-slip, installments), Wallet (multi-account, card cycle, reconcile), History (search & filter), Fixed Costs & Recurring Income, Core Analytics (Spending, Cash Flow, Net Worth), Settings (Privacy Mode, App Lock, Backup / Export), User Profile (financial baseline + core achievements) | E00 foundation (built first) · E01 accounts-categories · E02 add-transaction · E03 home-dashboard · E04 first-run · E05 settings-backup · E06 app-lock-privacy · E07 history · E08 scan-slip · E09 batch-import · E10 wallet · E17 reconcile · E11 fixed-costs (incl. installments) · E16 payday-recurring-income · E12 analytics · E19 export · E25 profile-rewards (core achievements, Q-45) · E13 notifications (kept because Fixed-costs bills and budget alerts need them; privacy-safe copy, Ton Q-18) · E14 release-readiness |
| **V1.1** | Home Screen widgets (Left to spend, Quick Scan) and Month-End Cash Flow Forecast | E28 widgets (with EX-001 snapshot) · E18 forecast |
| **V1.2** | Financial Goals (ring-fenced savings) and Trip & Party Budget (multi-currency, split engine) | E26 goals · E27 trips |
| **V2.0** | Shared Household / Family Space (real-time multi-user sync) | E21 sync-backend · E22 household-family · E23 sync-devices (BA placement: 6A and the sync states belong to sync; the 6A frame is now labelled "Sync & devices (V2.0 — not in V1.0)") |
| **No release** | Web app (the 6A "Web app · Chrome on Mac" device row was removed on 21 Nov 2026; no epic builds a web client) | — |

**V1.0 copy must not promise V2.0 features (audit findings 01, 02):** onboarding has no household page (page 3 is Fixed costs), Sign in says "Encrypted on this iPhone · back up to your private iCloud" (no sync claim), and no V1.0 screen links to 6A.
| **Not in Ton's roadmap (Q-44)** | — | E15 budget-cycle (9A / 9B category limits) · E20 tax-pro (9M / 9N, Pro) · E24 smart-banner (P2) |

---

## 3. Epic map

| Epic | Pipeline feature | Release | Journey(s) | Figma section | Depends on | Blocked by (§7 gaps / §8 questions) | Data classes |
|---|---|---|---|---|---|---|---|
| E00 | `foundation` | V1.0 | shell of all, 01 launch | C, D, E, I tab bars | — | T-22 only: Q-31 | Internal, Restricted keys |
| E01 | `accounts-categories` | V1.0 | 04 | B (2E) | E00 | DG-05 (Add Account sheet), DG-06, DG-31, DG-36 / Q-38, Q-09, **Q-53** (card days 29–31) | Restricted (account no.), Confidential |
| E02 | `add-transaction` | V1.0 | 03 | B (2A, 2B), tab bar | E01 | DG-40 (context menu), Q-34, DG-04 | Restricted (memo, merchant), Confidential |
| E03 | `home-dashboard` | V1.0 | 02 | C | E02 | DG-39, **DG-48**, Q-05 / DG-03, Q-20, **Q-52** (period label) | Confidential |
| E04 | `first-run` | V1.0 | 01 | A | E03 | DG-41, DG-32, DG-28, **DG-47**, **DG-49**, Q-08, **Q-39**, **Q-46** (Android Apple sign-in) | Confidential, Restricted (tokens, backup key) |
| E05 | `settings-backup` | V1.0 | 12 | I (7A–7F) | E04 | **Q-39**, Q-19, DG-15, DG-16, DG-17, DG-27, DG-28 | all classes (backup) |
| E06 | `app-lock-privacy` | V1.0 | 17, 01 | M (12H, 12A Privacy), I (7B) | E05 | Q-32, DG-02 / DG-26 | Restricted (biometric result) |
| E07 | `history` | V1.0 | 10 | G | E02 | **Q-07 / DG-12, DG-13** | Restricted, Confidential |
| E08 | `scan-slip` | V1.0 | 05 | B (2C, 2D) | E02, E01 | E08-T00 spike result, DG-24, DG-30, DG-45 | Restricted (slip image, QR payload, OCR text) |
| E09 | `batch-import` | V1.0 | 06 | B (2C batch) | E08 | DG-25 | Restricted |
| E10 | `wallet` | V1.0 | 07 | E | E01, E02 | DG-05, DG-07, DG-08, Q-20, Q-35 / DG-09 | Restricted, Confidential |
| E17 | `reconcile` | V1.0 | 07 | E (9C–9E) | E10 | — | Confidential |
| E11 | `fixed-costs` | V1.0 | 08 | F, B (2B installment) | E02, E03, E08 | DG-42, DG-43, DG-11, DG-10, Q-02, **Q-43** (DG-34 closed 21 Nov) | Confidential |
| E16 | `payday-recurring-income` | V1.0 | 08, 11 | F (9F, 9G), C (9H) | E11, E03 | Q-08 | Confidential |
| E12 | `analytics` | V1.0 | 09 | D | E02, E10 | Q-41 | Confidential |
| E19 | `export` | V1.0 | 09, 12 | I (9I) | E07 | — | Restricted (export file) |
| E25 | `profile-rewards` | V1.0 | 17 | M | E03, E06 | **Q-45**, Q-28 | Confidential |
| E13 | `notifications` | V1.0 | 02 (bell) | none | E03, E11, E10-T13 | **Q-40**, Q-05 / DG-03, DG-29 | Internal (copy holds no amounts) |
| E14 | `release-readiness` | V1.0 gate | — | Branding | all V1.0 epics | Q-25, Q-26, Q-19, Q-23 | — |
| E28 | `widgets` | V1.1 | 13 | I (6B) | E03, E11, E06 | Q-06 / DG-21, EX-001 Android point | Confidential (EX-001) |
| E18 | `forecast` | V1.1 | 11, 09 | H (9J, 9K), D (9L) | E16, E11, E03, E10-T13 | **Q-51** (line totals; horizon settled by Ton Q-47) | Confidential |
| E26 | `goals` | V1.2 | 15 | K | E10, E03 | Q-29, DG-35 | Confidential |
| E27 | `trips` | V1.2 | 16 | L | E02, E08, E12 | **Q-27**, Q-29, DG-35 | Confidential, Restricted |
| E21 | `sync-backend` | V2.0 | 13 | none | V1.0 | Q-33 | all (E2E) |
| E22 | `household-family` | V2.0 | 02, 03, 05, 07, 13 | C (1B), B (2B family, 2D family), E (W-C, W-D, Household) | E21 | DG-19 | Restricted, Confidential |
| E23 | `sync-devices` | V2.0 | 13 | I (6A, sync states), C (1G) | E21 | Q-01 / DG-18, DG-20 | Internal |
| E15 | `budget-cycle` | unassigned (Q-44) | 11 | H (9A, 9B) | E03, E12 | Q-44 | Confidential |
| E20 | `tax-pro` | unassigned (Q-44) | 11 | H (9M), B (9N) | E19 | Q-44, Q-03, Q-22, DG-14 | Restricted |
| E24 | `smart-banner` | unassigned (Q-44) | 05 | B (2A Smart Banner) | E08 | Q-44 | Restricted |

**Totals: 29 epics, 267 build / design / QA tasks** (V1.0 207 · V1.1 12 · V1.2 16 · V2.0 18 · unassigned 14), **plus 5 gate tasks per epic (145).** Revision 1 had 252. Revision 2 was +14 net: +16 new or moved-in tasks (E00 +5, E04 +4, E05 +1, E08 +2, E11 +2, E28 +2), −2 tasks moved out (E04-T01 → E00-T20, E06-T05 → E00-T21). Revision 3 is +1: E10-T13 card due-date rule (E11-T15 stays counted; it is marked done).

---

## 4. Recommended build order (one `/caffeine-pipeline <feature> both` at a time)

| # | Run | Release | Can start when |
|---|---|---|---|
| 1 | `foundation` | V1.0 | **now** (PLAN_READY) |
| 2 | `accounts-categories` | V1.0 | DG-05 Add Account sheet designed |
| 3 | `add-transaction` | V1.0 | DG-40 context menu designed |
| 4 | `home-dashboard` | V1.0 | DG-39 empty-state button designed; DG-48 hero figures corrected ("7 days left · ฿921/day"); Q-52 answered |
| 5 | `first-run` | V1.0 | DG-41, DG-47 and DG-49 designed; Q-39 answered (Android Apple sign-in waits for Q-46) |
| 6 | `settings-backup` | V1.0 | Q-39 answered |
| 7 | `app-lock-privacy` | V1.0 | Q-32 answered |
| 8 | `history` | V1.0 | Q-07 answered, DG-12 and DG-13 designed |
| 9 | `scan-slip` | V1.0 | E08-T00 spike done (6 banks) |
| 10 | `batch-import` | V1.0 | — |
| 11 | `wallet` | V1.0 | — |
| 12 | `reconcile` | V1.0 | — |
| 13 | `fixed-costs` | V1.0 | DG-42, DG-43, DG-11 designed; Q-43 answered |
| 14 | `payday-recurring-income` | V1.0 | — (Q-15 answered 21 Nov) |
| 15 | `analytics` | V1.0 | — |
| 16 | `export` | V1.0 | — |
| 17 | `profile-rewards` | V1.0 | Q-45 answered |
| 18 | `notifications` | V1.0 | Q-40 answered |
| 19 | `release-readiness` | V1.0 | Q-25, Q-26 answered |
| 20–21 | `widgets` → `forecast` | V1.1 | EX-001 Android point decided |
| 22–23 | `goals` → `trips` | V1.2 | Q-27 answered |
| 24–26 | `sync-backend` → `household-family` → `sync-devices` | V2.0 | Q-33 answered |

Runs 2–4 can't overlap (each needs the previous one's data). After run 4, two features may run at once **only** on different screens with no shared entity (for example `history` ∥ `wallet`), using `isolation: "worktree"`.

---

## 5. Cross-cutting rules (apply to every epic; QA checks every feature)
1. **Parity:** the same input gives the same output on iOS and Android. A different string or number is a blocking bug.
2. **Money:** `Decimal` / `BigDecimal` + ISO 4217, half-up to 2 dp, signed, one formatter per platform.
3. **Colours:** coral expense / mint income / `text-primary` transfer; summary totals neutral; tokens only; Dark and Light both ship. **Since 21 Nov 2026:** income amounts and positive deltas drawn as **text** use `night/income-text` (Dark #9EE6C4, Light #1F714C); mint **fills** (badges, bars, circles) keep `night/income`. The ✓ Paid badge is a solid `tint-mint` fill with `text-on-light` label and check. (The `caffeine-domain` colour rule still names `night/income` for amounts; the skill owner should add `income-text`.)
4. **Accessibility:** hit areas at least 44pt / 48dp; ids and labels on every control; chart and hero summaries for VoiceOver / TalkBack; largest Dynamic Type / font scale without clipped amounts; Reduce Motion shows final states. **Since 21 Nov 2026:**
   - Every text / background pair is at least 4.5:1 (3:1 for large text) in Dark **and** Light; QA probes Light first.
   - Secondary ink on periwinkle or coral blocks uses `night/on-primary-soft` / `night/on-accent-soft` at 100% layer opacity. Never add layer or paint opacity on top (that was the 2.86:1 keypad hint bug).
   - Light text links use `text-primary`, never periwinkle or lilac.
   - **Destructive text on a raised surface** (e.g. 5F "Cancel subscription", 7F "3 recent transactions will be lost.") sits in a `night/bg` container with a 1pt `glass-stroke`, never coral on `surface-raised`.
   - Segment, Segmented control, Filter chip, Meta chip, Dropdown pill, Space pill, Tag and Switch are drawn at 32–40pt but must have a 44pt (iOS `contentShape`) / 48dp (Android `minimumInteractiveComponentSize`) hit area; every feature spec repeats this.
5. **Security:** fields classified; Restricted fields use FieldCipher; nothing Confidential or Restricted in logs, analytics, notifications, widgets or the app-switcher snapshot (shield always on, Ton Q-04); Privacy Mode masks every amount as `฿••••••`.
6. **Figma numbers are sample data:** compute from state.
7. **Glass on Android API 28–30:** solid `glass-*` fill, no blur (DG-38).
8. **Notifications (Ton Q-18):** no amounts and no account names in push or local notifications. Approved style: "You have a credit card bill due tomorrow. Tap to review details." Whether a category name may appear is open (Q-40).
9. **Display rounding (Ton Q-16, implemented in foundation T-18 / T-19):**
   - **Per day left** = floor(left to spend / ((cycle end − today) + 1)), ฿0 when nothing is left.
   - **Budget %** is half-up to an integer, but never shows 100 while spent < budget (so 99.1–99.9% shows 99%).
   - **% vs previous month** is rounded to an integer, and anything above 999% shows ">999%".
   - Recommend that the skill owner folds these into `caffeine-domain`.
   - **Figma hero figures after the 21 Nov audit fix divide by the days after today** (฿6,450 ÷ 6 = ฿1,075; ฿40,000 ÷ 29 = ฿1,379). That contradicts Q-16. Code and ACs use Q-16 (÷ 7 → ฿921; ÷ 30 → ฿1,333); the frames are corrected under DG-48.
   - **Days left (Ton Q-48)** = (cycle end − today) + 1, the same count as the per-day divisor: "7 days left · ฿921/day" on 18 Nov (cycle ends 24 Nov); the last day reads "1 day left". The forecast daily-spending line uses the same figures (Ton Q-47).
10. **Budget cycle = payday (Ton A1, decisions file Part 3; audit finding 11):** the budget cycle starts on the user's payday (sample: 25th → cycle 25th–24th). There is one stored value: `cycleStartDay` holds the payday. It is set in O5 and in 12B / 12G, and shown as "Budget & Cycle · ฿40,000 · 25th" in Settings and "Current cycle: 25 Oct – 24 Nov 2026, set by your payday." on 9A. Whether 9A can change it separately is part of Q-44 (9A has no release yet). When no payday is set, the cycle starts on the 1st (foundation default). **Payday 29–31 (Ton Q-15):** clamps to the last valid day of a shorter month (31st → 28 Feb, 29 Feb in a leap year, 30 Apr) and never rolls into the next month; "Last day of the month" (12G) resolves to each month's final day (stored as `cycleStartIsLastDay`, foundation T-02). Worked cycles: `golden-sample-data.md` §6.
11. **Card due-date rule (Ton A2, decisions file Part 3; audit finding 12):** the **payment due date** drives the due badge, bill reminders and the forecast. The **statement cut-off date** is shown only as the statement date. One shared domain function computes it (E10-T13). Sample: cut-off 25, due day 10, today 18 Nov 2026 → statement 26 Oct–25 Nov, payment due 10 Dec, "Due in 22 days".
12. **Platform-named copy:** Figma strings name iPhone, iCloud, Excel and Numbers ("Encrypted on this iPhone · back up to your private iCloud", "QR read on this iPhone", "right on this iPhone", "opens in Excel and Numbers"). Android must not show "iPhone" or "iCloud". Android strings come from DG-49; until it is closed, Android tasks with these strings are not ready for GATE 1.
13. **Status bar (Ton Q-49):** both builds use the native OS status bar (iOS adapts to Light / Dark; Android through edge-to-edge system bars). The Figma "9:41" is not a spec value and is not drawn by the app.
14. **Sample data and names (Ton, findings 13–15):** every spec, `*-cases.md` row, preview and QA check uses [`golden-sample-data.md`](golden-sample-data.md) and the terms in [`glossary.md`](glossary.md) (both drafts until Ton reviews them). Concept "Safe to Spend" = UI "Left to spend"; Total Cash Balance, Net Cash Flow and Net Worth are never used interchangeably.

---

## 6. Epics and tasks

### E00 · foundation (V1.0) · full plan: `docs/plan/foundation-plan.md`
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E00-T01 | Generate design tokens: **build the token pipeline** (`scripts/tokens/`, `tokens.json`, iOS colour sets + `DesignTokens.swift`, Android `Caffeine{Colors,Dimens,Type}.kt`; none exist yet), including the 21 Nov changes: new `night/income-text`, primitives `coral/650`, `mint/700`, `gray/650`, Light `accent` / `text-secondary`, `on-primary-soft` 88%, `on-accent-soft` 88% / 96% (`tokens-changelog.md`) | UX | Both | — | variables |
| E00-T02 | Contract: AppSettings (incl. appLockEnabled, privacyModeEnabled), FieldCipher, storage layout (Ton Q-30), cases, threat model | LEAD | Both | — | — |
| E00-T03 | iOS project baseline | IOS | iOS | — | — |
| E00-T04 | Android project baseline | AND | Android | — | — |
| E00-T05 | Theme wiring | DEV | Both | T01, T03, T04 | — |
| E00-T06 | Tab shell (`State=No add`) | DEV | Both | T05 | DS `272:990`; `448:6722`, `448:11831`, `448:6926`, `448:29581` |
| E00-T07 | Key management | DEV | Both | T02–T04 | — |
| E00-T08 | FieldCipher helper | DEV | Both | T02, T07 | — |
| E00-T09 | Encrypted main ledger (strictest class) + AppSettings | DEV | Both | T02, T07 | — |
| E00-T10 | Store failure screen | DEV | Both | T06, T07, T09 | DG-22 |
| E00-T11 | Platform hardening | DEV | Both | T03, T04 | — |
| E00-T12 | Safe logging | DEV | Both | T03, T04 | — |
| E00-T13 | Formatter mask + parity table | DEV | Both | T02 | — |
| E00-T14 | Budget cycle boundaries: payday rule 1–31 or last day, month-end clamping (Ton Q-15), days left incl. today (Ton Q-48) | DEV | Both | T02 | — |
| E00-T15 | Cash-flow totals | DEV | Both | T02 | — |
| E00-T16 | Budget status | DEV | Both | T02, T14, T15 | — |
| E00-T17 | QA | QA | Both | T05–T21 | — |
| E00-T18 | Per-day allowance, floor, today counts (Ton Q-16) | DEV | Both | T14, T16 | — |
| E00-T19 | Percentage display: budget % 99% rule, % change >999% (Ton Q-16) | DEV | Both | T02 | — |
| E00-T20 | Splash while the store initialises (under 0.5 s) + launch gate hook (Ton Q-04; was E04-T01) | DEV | Both | T06, T07, T09, T10 | DG-01 |
| E00-T21 | App-switcher privacy shield, always (iOS, Android API 33+) (Ton Q-04; was E06-T05) | DEV | Both | T05, T06 | DG-26 |
| E00-T22 | Android API 28–32 shield (**blocked by Q-31**) | AND | Android | T21 | DG-26 |
Key ACs: `foundation-plan.md` AC-01 to AC-64 plus revision 3's AC-01a, AC-01b, AC-37a, AC-43a, AC-44a, AC-51a, AC-51b and revision 4's AC-38a–AC-38e (e.g. payday 31 on 15 Feb 2027 → cycle 31 Jan–27 Feb, 13 days left). For example AC-51: left ฿6,450 on Nov 18 of Nov 1–30 → ฿496/day; AC-51a: left ฿6,450 on 18 Nov in the payday cycle 25 Oct–24 Nov → 7 days → ฿921/day; AC-56: 99.5% → "99%"; AC-01a: Light `night/income-text` → #1F714C on both platforms.

### E01 · accounts-categories (V1.0, journey 04)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E01-T01 | Contract: Account (name, type Cash / Bank Account / Credit Card / E-Wallet, initial balance, colour / icon, includeInNetWorth default true, last-4 Restricted, credit limit, statement cut-off day 1–31, payment due day 1–31, hidden, archived, pinned), Category, Brand list (Ton Q-13) | LEAD | Both | E00 | — |
| E01-T02 | Seed categories once (8 expense, 5 income), idempotent | DEV | Both | T01 | — (DG-36) |
| E01-T03 | `createDefaultCashAccount()`: "Cash", type Cash, ฿0, included in net worth; idempotent; called when onboarding completes (E04-T07) (Ton Q-13) | DEV | Both | T01 | — |
| E01-T04 | Account repository + balance = initial + income − expense − transfers out + transfers in | DEV | Both | T01 | — |
| E01-T05 | From-account sheet | DEV | Both | T04 | `462:26319` |
| E01-T06 | To-account sheet (sending account disabled at 40%) | DEV | Both | T05 | `464:27062` |
| E01-T07 | Category sheet (Recent, Subscriptions brands, grid, New category tile) | DEV | Both | T02 | `464:28156` |
| E01-T08 | New category | DEV | Both | T07 | `470:27586`, `470:28092` |
| E01-T09 | Photo as category icon (encrypted thumbnail) | DEV | Both | T08 | `472:28274` |
| E01-T10 | **Add Account sheet** (Ton Q-13): one bottom sheet with Account Name, Account Type, Initial Balance, Card Colour / Icon, Include in Net Worth (on). Credit Card adds Credit Limit, Statement Cut-off Day (1–31), Payment Due Day (1–31). Entry points: Wallet "+ Add Account", Dashboard empty state "Add Account" (blocked by **DG-05** design) | DEV | Both | T04 | DG-05 |
| E01-T11 | Edit / reorder / hide category (blocked by DG-06, Q-09) | DEV | Both | T07 | DG-06 |
| E01-T12 | Brand logo assets | UX | Both | — | DS `467:1528` |
| E01-T13 | QA verification | QA | Both | T02–T11 | — |
Key ACs:
- Given onboarding completes and no account exists, When `createDefaultCashAccount()` runs twice, Then exactly 1 account "Cash" with balance ฿0 exists, included in net worth.
- Given the Add Account sheet with type Credit Card, When it opens, Then Credit Limit, Statement Cut-off Day and Payment Due Day show; *edge:* Given type Bank Account, Then those 3 fields are hidden; Given an empty Account Name, Then Save is disabled; Given a cut-off day of 0 or 32, Then it is rejected (how days 29–31 behave in short months for cut-off / due: Q-53).
- Given KBank Savings with initial ฿10,000, an expense of ฿320, an income of ฿52,000 and a transfer out of ฿5,000, Then the balance is ฿56,680.
- *security:* Given an account with last-4 4410, When the database is read without FieldCipher, Then last-4 is ciphertext.

### E02 · add-transaction (V1.0, journey 03)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E02-T01 | Contract: Transaction (… linkedFixedCostId for Ton Q-21), Favorite, Tag | LEAD | Both | E01 | — |
| E02-T02 | Domain validation | DEV | Both | T01 | — |
| E02-T03 | Keypad engine (Q-34) | DEV | Both | T01 | `448:5374` |
| E02-T04 | 2A Expense | DEV | Both | T02, T03 | `448:5374` |
| E02-T05 | 2A Income | DEV | Both | T04 | `446:10197` |
| E02-T06 | 2A Transfer / card payment | DEV | Both | T04 | `448:5488` |
| E02-T07 | Date and Memo chips | DEV | Both | T04 | `448:5374` |
| E02-T08 | Save (persist, refresh, failure path) | DEV | Both | T04 | — |
| E02-T09 | + button **tap opens 2A Keypad (Expense) directly** (Ton Q-17); switch the tab bar from `State=No add` | DEV | Both | T04 | DS tab bar |
| E02-T10 | + **long-press opens the quick context menu**: Scan Slip (camera) · Pick Slip from Photos · Add Transfer (Ton Q-17; replaces the 1N grid as the + target; design **DG-40**) | DEV | Both | T09, T06 | DG-40 (`446:10311` superseded) |
| E02-T11 | 2B Details (tags, merchant, receipt, memo) | DEV | Both | T04 | `448:5602` |
| E02-T12 | Favorites | DEV | Both | T08 | `448:5374` (DG-04) |
| E02-T13 | QA verification | QA | Both | T02–T12 | — |
Key ACs:
- Given Home is showing, When + is tapped, Then 2A opens with type Expense; When + is long-pressed, Then a menu with exactly "Scan Slip", "Pick Slip from Photos" and "Add Transfer" shows. Choosing Add Transfer opens 2A Transfer; the two slip items open 2C camera and the Photos picker (they route to the 2A Expense unreadable path until E08 ships).
- Given Cash ฿2,000, When an expense of ฿320, Food & Drink, from Cash is saved on 2026-11-18, Then Recent shows "−฿320" and Cash shows ฿1,680.
- *edge:* amount 0 → Save disabled; date 2026-11-20 on 2026-11-18 → rejected; a transfer to the same account → rejected; a card payment of ฿5,000 → spent unchanged.
- *security:* memo "dinner with Ploy" is ciphertext at rest and absent from logs.

### E03 · home-dashboard (V1.0, journey 02)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E03-T01 | Contract: Home read model | LEAD | Both | E02 | — |
| E03-T02 | Use the foundation display rules on the hero (per day E00-T18, budget % E00-T19) (Ton Q-16) | DEV | Both | T01 | — |
| E03-T03 | Budget hero v5 On track / Over pace (from data, round caps, 300pt), in the **payday cycle** (§5 rule 10); hero secondary text on `on-primary-soft` 88% with no extra opacity; badge "N days left" / "1 day left" from foundation T-14 days left (Ton Q-48); Figma per-day and days-left figures are wrong (DG-48); cycle label per **Q-52** | DEV | Both | T02 | `448:6722` |
| E03-T04 | Over budget hero; detail line "of ฿40,000 · ฿41,200 spent" (no "spending paused", audit 17); secondary ink `on-accent-soft` | DEV | Both | T03 | `448:6790` |
| E03-T05 | Budget warning at 90% and above | DEV | Both | T03 | `446:10784` |
| E03-T06 | Spend wave + VoiceOver summary | DEV | Both | T03 | `448:6722` |
| E03-T07 | No-budget state 1L ("Set monthly budget" target: Q-44) | DEV | Both | T03 | `446:11256` |
| E03-T08 | Large figures 1M | DEV | Both | T03 | `446:11324` |
| E03-T09 | Alert slot (Budget > Settlement (V2.0) > Bills) | DEV | Both | T03 | `446:10784` |
| E03-T10 | Recent transactions + See all | DEV | Both | T01 | `446:10920` |
| E03-T11 | Month sheet 1J | DEV | Both | T03 | `446:11106` |
| E03-T12 | Empty states 1H / 1I, incl. the **"Add Account" button** in the empty state (Ton Q-13, **DG-39**) → E01-T10; 1H scan copy "Reads the QR code on Thai bank e-slips, right on this iPhone." (Android string: DG-49) | DEV | Both | T03, E01-T10 | `446:10152`, `446:11062`, DG-39, DG-49 |
| E03-T13 | Header: avatar → 12A (E25, V1.0), Space pill (Q-20), bell (Q-05 / DG-03) | DEV | Both | T01 | `448:6722` |
| E03-T14 | QA verification | QA | Both | T02–T13 | — |
Key ACs:
- Given payday 25 (cycle 25 Oct–24 Nov 2026), budget ฿40,000, expenses ฿33,550 and today 18 Nov 2026, When Home opens, Then Left to spend "฿6,450", "84%" used, Over pace (84% > elapsed 25 / 31 = 81%), and "฿921/day" (floor of 6,450 / 7; **not** Figma's ฿1,075), and the badge reads **"7 days left"** (Ton Q-48; not Figma's "6 days left").
- *edge:* Given payday 25 and today 24 Nov 2026 (last day of the cycle) with ฿5,851 left, Then the badge reads **"1 day left"** and the hero shows "฿5,851/day".
- *edge:* Given payday 31 and today 15 Feb 2027, Then the cycle is 31 Jan–27 Feb 2027 and the badge reads "13 days left" (Ton Q-15 clamping).
- Given no payday set (cycle 1–30 Nov), the same budget and expenses and today 18 Nov, Then "฿496/day" (floor of 6,450 / 13).
- *edge:* Given payday 25, expenses ฿32,000 of ฿40,000 on 18 Nov, Then status is **On track** (80% ≤ 81%) (this is the 1B data; the frame still shows Over pace, DG-48).
- *edge:* Given payday 25 and today 25 Nov 2026 (first day of the 25 Nov–24 Dec cycle, nothing spent), Then "฿40,000" left and "฿1,333/day" (floor of 40,000 / 30; Figma's 1I shows ฿1,379).
- *edge:* Given expenses ฿39,800, Then the hero shows "99%", not "100%"; Given ฿41,200, Then the Over budget hero shows "Over budget by ฿1,200", "103%" and the detail "of ฿40,000 · ฿41,200 spent".
- *a11y:* Given Light mode, When the hero renders, Then "LEFT TO SPEND" and the detail line use `night/on-primary-soft` (#1C1C1E at 88%, 4.76:1 on #8C88F8) with no extra layer opacity.
- *edge:* Given 92% spent and 3 bills due, Then exactly one alert card shows (Budget).
- *security:* Given Home loads, When the log is captured, Then it has no amount, category or memo (Privacy Mode masking is verified in E06-T07).

### E04 · first-run (V1.0, journey 01)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E04-T01 | *moved to E00-T20 (splash)* | — | — | — | — |
| E04-T02 | Onboarding pager O6·1–3 (revision 3 copy): 1 "Never run short before payday" (chip "On track for payday"), 2 "Scan a slip. / We log it." (pill "QR read on this iPhone"), **3 "Know every bill / before it lands" (Fixed costs; pill "Reminder before each charge")**. No household page in V1.0 (the old page 3 `614:37371` is replaced; household is V2.0). Android strings: DG-49 | DEV | Both | E00 | `448:4716`, `448:4808`, `448:5106` |
| E04-T03 | Vignettes and motion (Reduce Motion = final state). Page 3 vignette is real Fixed costs hero + 2 Fixed cost rows + glass chip; its motion is **not designed yet (DG-47)** | DEV | Both | T02 | same, DG-47 |
| E04-T04 | iOS Sign in: **Sign in with Apple + Continue with Google + Continue as Guest** (Ton Q-11; DG-41, DG-32); trust line "Encrypted on this iPhone · back up to your private iCloud" (no sync claim); Light "Continue as Guest" in `text-primary` | IOS | iOS | T02 | `448:5314` (text `448:5327`), DG-41 |
| E04-T05 | O5 Monthly budget setup; payday 1–31 or "Last day of the month" sets the cycle (Ton A1, Q-15; whether payday is required is Q-08); Skip → 1L | DEV | Both | E03 | `446:10038` |
| E04-T06 | O6 Loading 3 s → Home 1H | DEV | Both | T05 | `501:28700` (notes `501:28956`) |
| E04-T07 | First-run completion: set onboardingCompleted, **call E01-T03 to create the ฿0 Cash account** (Ton Q-13), returning user → Home (or the E06 lock) | DEV | Both | T05, E01-T03 | — |
| E04-T08 | QA verification | QA | Both | T02–T12 | — |
| E04-T09 | **Backup key on sign-in** (Ton Q-11): random 256-bit backup key from the CSPRNG, bound to the signed-in identity and the private cloud container; storage and recovery on a new device per **Q-39** | DEV | Both | T04, T11 | — |
| E04-T10 | Guest path: no identity, no cloud backup key until linked (Guest backup: **Q-39**); link later via 12B Guest | DEV | Both | T04, T11 | `597:37438` |
| E04-T11 | Android Sign in: **Continue with Google (primary) + Continue as Guest** (Ton Q-11; DG-41, DG-28); trust line per DG-49 (must not say "iPhone" or "iCloud") | AND | Android | T02 | `448:5314`, DG-41, DG-49 |
| E04-T12 | Android **Sign in with Apple (web OAuth)** for iOS → Android migration (Ton Q-11; **blocked by Q-46**: the web flow needs a redirect endpoint and client-secret signing, i.e. a server in a local-first V1) | AND | Android | T11 | DG-41 |
Key ACs:
- Given a first launch on iOS, When Sign in shows, Then exactly 3 options show: Sign in with Apple, Continue with Google, Continue as Guest; on Android: Continue with Google, Sign in with Apple, Continue as Guest (Google first).
- Given O5 amount ฿40,000, When Start tracking is tapped, Then after Loading, Home 1H shows "฿40,000", On track, and Wallet holds 1 account "Cash" ฿0.
- Given O5 amount ฿40,000 and payday 25 on 18 Nov 2026, When Start tracking is tapped, Then `cycleStartDay` = 25, Home uses the cycle 25 Oct–24 Nov 2026 and shows "7 days left" and "฿5,714/day" (floor of 40,000 / 7).
- *edge:* Given O5 payday 31 on 15 Feb 2027, When Start tracking is tapped, Then `cycleStartDay` = 31 and the current cycle is 31 Jan–27 Feb 2027 (not ending 2 Mar); Given "Last day of the month", Then `cycleStartIsLastDay` = true and the cycle dates are the same.
- Given a first launch, When the onboarding pager shows, Then it has exactly 3 pages titled "Never run short before payday", "Scan a slip. We log it." and "Know every bill before it lands", and no page mentions a shared wallet, household or settle-up.
- *edge:* Given Reduce Motion is on, When page 3 shows, Then the Fixed costs hero, both rows and the "Netflix reminder set" chip show in their final positions with no movement.
- *edge (Android):* Given the Android build, When Sign in and onboarding page 2 show, Then no string contains "iPhone" or "iCloud" (strings from DG-49).
- *edge:* Given the O5 amount is empty or ฿0, Then Start tracking is disabled; Given Skip on O5, Then Home shows 1L, and the Cash account still exists; Given Google sign-in is cancelled, Then Sign in stays with no account created (DG-32 copy).
- *security:* Given sign-in succeeds, Then identity tokens and the backup key are only in the Keychain / Keystore-protected storage, never in UserDefaults / SharedPreferences or logs.

### E05 · settings-backup (V1.0, journey 12)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E05-T01 | Contract: settings fields; **Cloud Backup interface** (one interface, provider per platform; client-encrypted snapshot format, restore points) (Ton Q-12) | LEAD | Both | E00 | — |
| E05-T02 | 7A / 7B Settings; "Budget & Cycle" value = budget · payday ("฿40,000 · 25th"); footer "Caffeine <version> (<build>) · Made in Bangkok" from the build, never hard-coded | DEV | Both | E04 | `448:29581`, `448:29755` |
| E05-T03 | Theme System / Light / Dark | DEV | Both | T02 | `448:29755` |
| E05-T04 | Haptics; Language (Q-19) | DEV | Both | T02 | `448:29755` |
| E05-T05 | iOS provider: **iCloud Drive private container**, client-side encrypted snapshots; 7C Back Up Now, auto-backup, cellular, restore list | IOS | iOS | T01, E04-T09 | `448:29929` |
| E05-T06 | Backup failed (offline) 7D, both providers | DEV | Both | T05, T08 | `448:30041` |
| E05-T07 | Restore confirmation 7F, both providers; the data-loss row sits in a `night/bg` container with 1pt `glass-stroke` (§5 rule 4) | DEV | Both | T05, T08 | `448:30157` (row `448:30220` / Light `448:30290`) |
| E05-T08 | Android provider: **Google Drive AppData folder (`drive.appdata`)**, client-side encrypted; same 7C behaviour (Android variant DG-28) | AND | Android | T01, E04-T09 | `448:29929`, DG-28 |
| E05-T09 | Rows with no screen yet (DG-15, DG-16, DG-17) | DEV | Both | T02 | DG-15–17 |
| E05-T10 | Delete my data (DG-27) | DEV | Both | T02 | DG-27 |
| E05-T11 | Settings states (Guest, failed subtitle) | DEV | Both | T02 | `448:31268` |
| E05-T12 | QA verification | QA | Both | T02–T13 | — |
| E05-T13 | **Encrypted local backup file `.caffeine`**: export and import through the system share sheet / file picker (Ton Q-12); key or passphrase per **Q-39** | DEV | Both | T01 | DG-28 (export / import entry) |
Key ACs:
- Given Theme Light is chosen, Then the app switches immediately and keeps Light after a relaunch.
- *edge:* Given no network, When Back Up Now is tapped, Then 7D shows "Backup failed" / "No internet connection" with the stored last successful time, and nothing is uploaded.
- *edge:* Given 3 transactions newer than the restore point, Then 7F says "3 recent transactions will be lost."; Cancel changes nothing.
- *a11y:* Given Light mode, When 7F shows, Then "3 recent transactions will be lost." is `night/accent` (#CF3D20) on a `night/bg` container with a 1pt `glass-stroke` (4.59:1), not on `surface-raised`.
- Given budget ฿40,000 and payday 25, When 7A opens, Then the Budget & Cycle row value reads "฿40,000 · 25th"; Given marketing version 1.0 and build 2026.11, Then the footer reads "Caffeine 1.0 (2026.11) · Made in Bangkok".
- *security:* Given a snapshot is uploaded to iCloud or Drive, When the remote file is read without the backup key, Then it is ciphertext; Given a `.caffeine` file, When opened in a text editor, Then no amount, memo or name is readable.

### E06 · app-lock-privacy (V1.0, journeys 17 and 01)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E06-T01 | Contract / threat model: lock state, re-lock timeout (Q-32), biometric result never stored | LEAD | Both | E05 | — |
| E06-T02 | App Lock toggle (Face ID / Touch ID, BiometricPrompt, passcode fallback) | DEV | Both | T01 | `448:29755`, DG-17 |
| E06-T03 | **Launch with App Lock on** (Ton Q-04): after the splash, the launch gate shows the privacy shield overlay and starts the Face ID / fingerprint prompt automatically. App Lock off → Dashboard. The same applies on return per Q-32 | DEV | Both | T02, E00-T20, E00-T21 | DG-02 / DG-26 |
| E06-T04 | App Lock gate 12H for sensitive edits | DEV | Both | T02 | `597:38284` |
| E06-T05 | *moved to E00-T21 / E00-T22 (app-switcher shield, always on)* | — | — | — | — |
| E06-T06 | Privacy Mode toggle (`฿••••••`, counts unmasked, "Tap to reveal for 30s") | DEV | Both | E00-T13 | `597:34846`, `448:29755` |
| E06-T07 | Retrofit the Privacy Mode mask on every screen already built | DEV | Both | T06 | — |
| E06-T08 | QA verification (MASTG AUTH, PLATFORM) | QA | Both | T02–T07 | — |
Key ACs:
- Given App Lock is on, When the app is cold-launched, Then the splash is followed by the shield with the biometric prompt started automatically, and no amount is visible until it succeeds.
- *edge:* Given biometrics fail or are cancelled, Then the shield stays with "Use passcode"; Given App Lock is off, Then the splash goes straight to the Dashboard.
- Given Privacy Mode is on, When "Tap to reveal" is tapped, Then amounts show for 30 s, then are masked again.
- *security:* Given Privacy Mode is on, Then Home, Wallet, History and Analytics show every amount as "฿••••••".

### E07 · history (V1.0, journey 10)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E07-T01 | Contract: search over Restricted memo / merchant (R-2), filters, period | LEAD | Both | E02 | — |
| E07-T02 | 8A ledger by day, neutral day nets | DEV | Both | T01 | `448:14381` |
| E07-T03 | Summary row, contextual "Total outflow", tap → 4C | DEV | Both | T02 | `448:14381` |
| E07-T04 | Search + tag suggestions | DEV | Both | T02 | `448:14495` |
| E07-T05 | Period picker 8C | DEV | Both | T02 | `448:14717` |
| E07-T06 | Filters 8D + badge + Reset; results 8E | DEV | Both | T02 | `448:14859`, `448:14575` |
| E07-T07 | Totals of visible items only, transfers excluded | DEV | Both | T03–T06 | `448:14575` |
| E07-T08 | No matches 8J | DEV | Both | T04 | `448:14649` |
| E07-T09 | Swipe delete + Undo 8G | DEV | Both | T02 | `448:15085`, `448:15215` |
| E07-T10 | Duplicate (blocked by Q-07, DG-12) | DEV | Both | T09 | DG-12 |
| E07-T11 | Detail sheet 8H | DEV | Both | T02 | `448:15331` |
| E07-T12 | Receipt viewer 8I (in memory only) | DEV | Both | T11 | `448:15531` |
| E07-T13 | Edit transaction (blocked by Q-07, DG-13) | DEV | Both | T11 | DG-13 |
| E07-T14 | States 8K | DEV | Both | T03 | `448:31386` |
| E07-T15 | QA verification | QA | Both | T02–T14 | — |
Key ACs:
- Given Nov income ฿52,000, expenses ฿33,550 and a transfer of ฿5,000 (42 entries), Then "Net cash flow · 42 entries", "+฿18,450", In "+฿52,000", Out "−฿33,550".
- *edge:* "#home" → 2 expenses totalling ฿2,180 and no income → "Total outflow" "฿2,180"; no match → 8J, "฿0".
- *edge:* Delete then Undo → the same id is back and the totals are unchanged.
- *security:* after viewing a receipt in 8I, no decrypted image file exists in the container.

### E08 · scan-slip (V1.0, journey 05) — hybrid on-device pipeline (Ton Q-14)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E08-T00 | **Spike** with sample slips from **KBank, SCB, BBL, KTB, Krungsri, TTB**: barcode detection + OCR accuracy for Amount, Date / Time, Merchant / Recipient per bank, before the parser is locked. Output: per-bank accuracy table + parser rules in `docs/data-model/scan-slip-spike.md`. Real slips are Restricted: anonymise, keep out of the repo | LEAD | Both | — | — |
| E08-T01 | Contract: slip parse result (bank code, transaction reference, amount, date / time, merchant / recipient), field tags "From slip" / "Suggested", **duplicate key = sending bank code + transaction reference**, encrypted image + payload + OCR text | LEAD | Both | T00, E02 | — |
| E08-T02 | **Barcode step**: iOS `VNDetectBarcodesRequest`, Android ML Kit Barcode; verify it is a bank-slip QR; extract sending bank code + transaction reference; 2C viewfinder, flash, Close | DEV | Both | T01 | `448:6206` |
| E08-T03 | 2C "Choose a slip from Photos" | DEV | Both | T02 | `448:6206` |
| E08-T04 | 2C Error (no valid slip QR) + Choose another photo / Use as receipt & type amount | DEV | Both | T02 | `448:6272` |
| E08-T05 | Unreadable → 2A keypad with the photo attached (P4) | DEV | Both | T04, E02 | `446:10651` |
| E08-T06 | 2D lean review (thumbnail, tags, Attach slip switch, Save); badge and tag copy for OCR-read fields per **DG-45** | DEV | Both | T02, T11 | `446:10443`, DG-45 |
| E08-T07 | On-device category suggestion with reason | DEV | Both | T06 | `446:10443` |
| E08-T08 | Scan entry points: 2A chip, long-press menu items (E02-T10), 1H CTA | DEV | Both | T02, E02-T10 | `446:10197`, `446:10152` |
| E08-T09 | Camera permission denied / restricted (DG-24) | DEV | Both | T02 | DG-24 |
| E08-T10 | QA verification | QA | Both | T02–T12 | — |
| E08-T11 | **OCR step** on the same image, run at the same time: iOS `VNRecognizeTextRequest`, Android ML Kit Text Recognition; parse Amount, Date / Time, Merchant / Recipient with the T00 rules | DEV | Both | T01 | — |
| E08-T12 | **Duplicate-slip check** on bank code + transaction reference, before saving; warning UI per DG-30 | DEV | Both | T02, T06 | DG-30 |
Key ACs:
- Given a KBank slip for ฿320.00 whose QR holds bank code + transaction reference, When it is scanned, Then 2D shows "−฿320.00", the date / time and recipient read by OCR, tagged as "From slip" (copy per DG-45), and no "Bank verified".
- *edge:* Given the same slip (same bank code + transaction reference) was saved before, When it is scanned again, Then the duplicate warning shows and nothing is saved without confirmation.
- *edge:* Given a photo with no slip QR, Then 2C Error shows "No valid e-slip QR found in this image"; Given airplane mode, Then scanning works with 0 network requests.
- *security:* Given a slip is saved, Then the image, QR payload and OCR text are ciphertext at rest.

### E09 · batch-import (V1.0, journey 06)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E09-T01 | Contract: batch job, max size | LEAD | Both | E08 | — |
| E09-T02 | Photos multi-select | DEV | Both | T01 | `448:6342` |
| E09-T03 | Reading progress (barcode + OCR per photo) | DEV | Both | T02, E08-T11 | `446:10383` |
| E09-T04 | Review list + "Save N expenses" (P1); duplicates in the batch flagged by E08-T12 | DEV | Both | T03 | `446:10383` |
| E09-T05 | Row → 2D → back | DEV | Both | T04 | `446:10443` |
| E09-T06 | Unreadable row → 2A | DEV | Both | T04 | `446:10651` |
| E09-T07 | Limited / denied Photos access | DEV | Both | T02 | `448:6074`, DG-25 |
| E09-T08 | QA verification | QA | Both | T02–T07 | — |
Key ACs: Given 3 slips with 1 unreadable, Then "Save 2 expenses"; *edge:* 2 photos of the same slip → 1 is flagged as a duplicate; all unreadable → Save disabled. *security:* a cancelled batch leaves no plaintext copies.

### E10 · wallet (V1.0, journey 07)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E10-T01 | Contract: net worth (includeInNetWorth, credit negative), hide vs exclude, card cycle (cut-off, due) | LEAD | Both | E01 | — |
| E10-T02 | W-A carousel (Card face / Detailed) | DEV | Both | T01 | `448:11831` |
| E10-T03 | Card details strip + card face pill + Account tile: statement period from the cut-off day; **due badge from the payment due date** (E10-T13, §5 rule 11); usage vs limit, available credit | DEV | Both | T02, T13 | `448:11831` |
| E10-T04 | Metric hero Mint net worth | DEV | Both | T01 | `448:11831` |
| E10-T05 | Grid W-B | DEV | Both | T02 | `448:12047` |
| E10-T06 | Account menu W-F | DEV | Both | T02 | `448:12607` |
| E10-T07 | Hide W-G; Exclude W-H | DEV | Both | T06 | `448:12767`, `448:12931` |
| E10-T08 | Add / Manage accounts W-E with **"+ Add Account" → E01-T10** (Ton Q-13) | DEV | Both | T02, E01-T10 | `448:12453` |
| E10-T09 | Pay card → 2A card payment prefilled | DEV | Both | T03, E02-T06 | `448:5488` |
| E10-T10 | States 3I | DEV | Both | T02 | `448:30764` |
| E10-T11 | Net worth detail, Archived, Reconnect (DG-07–09, Q-35) | DEV | Both | T04 | DG-07–09 |
| E10-T12 | QA verification | QA | Both | T02–T11, T13 | — |
| E10-T13 | **Card due-date rule (domain, revision 3)**: `CardCycle.statement(cutOffDay, today)` → the open statement period (the one containing today); `CardCycle.nextPaymentDue(cutOffDay, dueDay, today)` → the first date on or after today whose day of month = due day, the days until it (0 = today), and the statement it pays (the latest statement that closed before that date). Shared by E10-T03 (badge), E13-T03 (reminders) and E18 (forecast). Cut-off is never used for the badge. Cut-off / due days 29–31: Q-53 (Ton's Q-15 clamping names payday only) | DEV | Both | T01 | `448:11831` (sample "Due in 22 days") |
Key ACs: Given Savings ฿62,400, Cash ฿2,000 and KBank Credit owing ฿12,840, Then net worth "฿51,560"; *edge:* Savings with Include in Net Worth off → "−฿10,840"; Given a cut-off day of 25 and today 2026-11-18, Then the current statement period is 26 Oct–25 Nov. *security:* in Privacy Mode, balances are "฿••••••" and only last-4 shows.
- E10-T13: Given cut-off day 25, payment due day 10 and today 2026-11-18, When `nextPaymentDue` runs, Then the due date is 2026-12-10 and days until = 22; the card pill reads "Due in 22 days" and the strip "Payment due 10 Dec · in 22 days" with "Cut-off 25 Nov" (**not** "in 7 days", which would be the cut-off).
- *edge:* Given cut-off day 5, due day 25 and today 2026-11-18, Then the open statement period is 6 Nov–5 Dec, the next payment due is 2026-11-25 (7 days), and it pays the statement 6 Oct–5 Nov.
- *edge:* Given cut-off day 25, due day 10 and today 2026-12-10, Then the next payment due is 2026-12-10 and days until = 0 (badge copy for 0 days comes from the E10 spec).
- *edge:* Given cut-off day 0 or 32 (or due day 0 or 32), Then it throws `VALIDATION-CARD-01` with no values in the message.

### E17 · reconcile (V1.0, journey 07)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E17-T01 | Contract: adjustment type, excluded from budgets | LEAD | Both | E10 | — |
| E17-T02 | 9C menu with Reconcile | DEV | Both | T01 | `448:13105` |
| E17-T03 | 9D Balance adjustment | DEV | Both | T02 | `448:13267` |
| E17-T04 | 9E Untracked income | DEV | Both | T02 | `448:13457` |
| E17-T05 | QA verification | QA | Both | T02–T04 | — |
Key ACs: Given app balance ฿56,680 and an actual ฿57,000, When an adjustment is saved, Then the balance is ฿57,000 and spent is unchanged; *edge:* an actual equal to the balance disables Save. *security:* adjustments are Confidential; logs hold event ids only.

### E11 · fixed-costs (V1.0, journey 08)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E11-T01 | Contract: Subscription, InstallmentPlan, payment record linked to a Transaction (Ton Q-21), match rule for "Link to bill" (**Q-43**) | LEAD | Both | E02 | — |
| E11-T02 | Hero (timeline from data) | DEV | Both | T01 | `448:13650` |
| E11-T03 | Subscriptions list, filters, sort | DEV | Both | T01 | `448:13650` |
| E11-T04 | Timeline dot + callout (callout text `text-on-inverse` on the inverse pill; the Light frame `448:13743` was black on charcoal before 21 Nov) | DEV | Both | T02 | `448:13712` |
| E11-T05 | Swipe **Mark paid → opens the confirmation sheet** (E11-T17); Skip | DEV | Both | T03, T17 | `448:13774` |
| E11-T06 | Detail sheet 5F; "Cancel subscription" button on a `night/bg` container with 1pt `glass-stroke` (§5 rule 4) | DEV | Both | T03 | `448:13988` (button `448:14043` / Light `448:14099`) |
| E11-T07 | Installments 5D | DEV | Both | T01 | `448:13848` |
| E11-T08 | Schedule sheet 5G | DEV | Both | T07 | `448:14100` |
| E11-T09 | + menu 5E | DEV | Both | T02 | `448:13916` |
| E11-T10 | Installment section on 2B | DEV | Both | T07, E02-T11 | `448:5602` |
| E11-T11 | Add subscription form (DG-11); payoff calculator (DG-10) | DEV | Both | T09 | DG-10, DG-11 |
| E11-T12 | Home Bills alert in the E03 slot | DEV | Both | T03, E03-T09 | `448:6722` |
| E11-T13 | Entry point (Q-02) | DEV | Both | T02 | — |
| E11-T14 | States 5H | DEV | Both | T02 | `448:31210` |
| E11-T15 | Design fix ✓ Paid badge (DG-34) — **done 21 Nov 2026**: solid `tint-mint` fill, `text-on-light` label and check (11.8:1 both modes) on all 24 v5.1 badges | UX | Both | — | `448:13649` |
| E11-T16 | QA verification | QA | Both | T02–T18 | — |
| E11-T17 | **Mark paid confirmation sheet** (Ton Q-21): amount, paying account, payment date; Confirm posts an Expense linked to the bill and reduces Left to spend; Cancel changes nothing (DG-42) | DEV | Both | T01, E02-T08 | DG-42 |
| E11-T18 | **"Link this transaction to your upcoming <bill> bill?"** prompt in 2B and 2D when a new expense matches an upcoming bill (rule Q-43); Link = mark the bill paid by this transaction, with no second expense (Ton Q-21; DG-43) | DEV | Both | T01, E02-T11, E08-T06 | DG-43 |
Key ACs:
- Given Netflix ฿419 due tomorrow and budget left ฿6,450, When Mark paid → Confirm with Cash and today's date, Then 1 expense of ฿419 linked to Netflix is created, Left to spend shows ฿6,031, and Netflix shows ✓ Paid.
- *edge:* Given ฿419 Netflix was already logged manually and matches (rule Q-43), When it is saved in 2B, Then the prompt "Link this transaction to your upcoming Netflix bill?" shows; Link marks the bill paid and the expense count stays 1.
- Given a ฿1,990 / month plan of 6 terms from Sep 2026 with 2 paid, Then "2 of 6", next Nov 2026, ends Feb 2027.
- *a11y:* Given Light mode and Spotify marked paid, When 5A renders, Then the ✓ Paid badge is a solid `tint-mint` fill with `text-on-light` "Paid" and check (no mint text on mint); Given 5F in Light, Then "Cancel subscription" is `night/accent` on a `night/bg` container with a 1pt `glass-stroke` (4.59:1).
- *security:* bill reminders follow §5 rule 8 (no amount, no account name).

### E16 · payday-recurring-income (V1.0, journeys 08 and 11)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E16-T01 | Contract: RecurringIncome; payday = budget cycle start (§5 rule 10: `cycleStartDay` 1–31 + `cycleStartIsLastDay`, clamped per Ton Q-15); the 25 Nov salary belongs to the cycle that starts that day | LEAD | Both | E11 | — |
| E16-T02 | 9F Income filter | DEV | Both | T01 | `448:14218` |
| E16-T03 | 9G New recurring income | DEV | Both | T01 | `448:14280` |
| E16-T04 | 9H payday Confirm receipt card | DEV | Both | T03, E03-T09 | `448:6858` |
| E16-T05 | QA verification (incl. 9O states `448:31560`) | QA | Both | T02–T04 | `448:31560` |
Key ACs: expected ฿52,000 + ฿12,000 → "+฿64,000"; Confirm on payday records ฿52,000 once; *edge:* a second Confirm records nothing. *security:* the income baseline is Confidential.

### E12 · analytics (V1.0 core: Spending, Cash Flow, Net Worth, journey 09)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E12-T01 | Contract: aggregations; % vs previous month from E00-T19 (prev ฿0: Q-41) | LEAD | Both | E02 | — |
| E12-T02 | Header + Spending / Cash Flow / Trends | DEV | Both | T01 | `448:6926` |
| E12-T03 | 4A Spending | DEV | Both | T02 | `448:6926` |
| E12-T04 | 4B + Insight entry | DEV | Both | T03 | `446:11393` |
| E12-T05 | 4E Insight sheet (Adjust budget target depends on Q-44) | DEV | Both | T04 | `448:7174` |
| E12-T06 | 4C Cash Flow | DEV | Both | T02 | `448:7014` |
| E12-T07 | 4D Trends / Net Worth | DEV | Both | T02, E10-T04 | `446:11493` |
| E12-T08 | States 4F | DEV | Both | T02 | `448:31108` |
| E12-T09 | Chart accessibility summaries | DEV | Both | T03, T06, T07 | — |
| E12-T10 | QA verification | QA | Both | T02–T09 | — |
Key ACs: Nov ฿36,000 vs Oct ฿40,000 → "↓ 10% vs Oct" (integer, Ton Q-16); *a11y:* in Light, positive deltas and income figures drawn as text (e.g. 4C "+฿18,450", 4D "↑ 12%") use `night/income-text` #1F714C, never #9EE6C4; *edge:* Nov ฿11,000 vs Oct ฿1,000 → ">999%"; Nov expenses ฿33,550 → the hero and rows sum to ฿33,550. *security:* Privacy Mode masks values; chart shapes stay.

### E19 · export (V1.0 — part of Settings Backup / Export)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E19-T01 | Contract: CSV columns, PDF layout | LEAD | Both | E07 | — |
| E19-T02 | 9I Export sheet; CSV caption "Full ledger · opens in Excel and Numbers" (was "UTF-8 (Thai safe)"; Android caption per DG-49) | DEV | Both | T01 | `448:30297`, DG-49 |
| E19-T03 | Share; temp file deleted after | DEV | Both | T02 | — |
| E19-T04 | QA verification | QA | Both | T02–T03 | — |
Key ACs: 42 transactions → 42 CSV rows, signed, 2 dp; *edge:* an empty range disables Export. *security:* the temp file is gone after the share sheet closes.

### E25 · profile-rewards (V1.0: baseline + core achievements, journey 17)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E25-T01 | Contract: Profile, baseline, Mission, Achievement (core set **Q-45**), Q-28 items | LEAD | Both | E03 | — |
| E25-T02 | 12A Profile + Guest + Privacy | DEV | Both | T01, E06 | `597:33917`, `597:34380`, `597:34846` |
| E25-T03 | 12C / 12D / 12F badges | DEV | Both | T02 | `597:35290`, `597:35800`, `597:36810` |
| E25-T04 | 12E share card | DEV | Both | T03 | `597:36316` |
| E25-T05 | 12B Edit + 12G payday behind 12H | DEV | Both | T02, E06-T04 | `597:37098`, `597:37438`, `597:37770` |
| E25-T06 | 12I unlock toast | DEV | Both | T03, E02 | `597:38380` |
| E25-T07 | Avatar → 12A; Settings profile row → 12H → 12B | DEV | Both | T02 | — |
| E25-T08 | QA verification | QA | Both | T02–T07 | — |
Key ACs: the badge count shows "n / N", where N = the size of the core set (Q-45); *edge:* with 3 focus pills chosen, the others are disabled at 40%. *security:* the share card has no amount.

### E13 · notifications (V1.0, privacy-safe)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E13-T01 | Permission pre-prompt (DG-29) | DEV | Both | E03 | DG-29 |
| E13-T02 | Budget alerts at 90% / 100%, once per threshold per cycle, generic copy (Ton Q-18; category name: **Q-40**) | DEV | Both | E03, T01 | DG-44 |
| E13-T03 | Bill-due reminders, generic copy ("You have a credit card bill due tomorrow. Tap to review details."); card reminders are scheduled from the **payment due date** (E10-T13), never the cut-off (§5 rule 11). Onboarding page 3 promises "Reminder before each charge" | DEV | Both | E11, T01, E10-T13 | DG-44 |
| E13-T04 | Bell + notifications list (Q-05, DG-03) | DEV | Both | E03-T13 | DG-03 |
| E13-T05 | Schedule notifications when data changes (app unlocked); never read the main ledger while locked (Ton Q-30 split storage) | LEAD | Both | — | — |
| E13-T06 | QA verification | QA | Both | T01–T05 | — |
Key ACs: spent reaching ฿36,000 of ฿40,000 → one 90% alert, then one 100% alert, with no repeats; *edge:* permission denied → nothing scheduled, the in-app alert still shows; Given KBank Credit with cut-off day 25 and due day 10 on 18 Nov 2026, When reminders are scheduled, Then the "due tomorrow" reminder is set for 9 Dec 2026, and none is set for 24 Nov 2026. *security:* Given any scheduled notification, Then its title and body contain no "฿", digits of an amount, or account names.

### E14 · release-readiness (V1.0 gate)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E14-T01 | Bundle id / package, team, signing (Q-25) | LEAD | Both | — | — |
| E14-T02 | App icon assets (Q-26) | UX | Both | — | `537:335` / `537:357` / `537:379` |
| E14-T03 | Wire AppIcon | DEV | Both | T02 | — |
| E14-T04 | fastlane test + beta | LEAD | Both | T01 | — |
| E14-T05 | Privacy policy, PDPA consent, store privacy labels (incl. Google / Apple sign-in and Drive / iCloud backup scopes) | LEAD | Both | — | — |
| E14-T06 | Localization (Q-19) | DEV | Both | — | — |
| E14-T07 | Crash reporting with no PII (Q-23) | LEAD | Both | — | — |
| E14-T08 | Dependency scan in CI | LEAD | Both | T04 | — |
| E14-T09 | Full regression + MASTG L2 | QA | Both | T03–T08 | — |
Key ACs: 0 secrets found in the repo; *edge:* no icon → beta BLOCKED; *security:* MASTG L2 all PASS, or an approved exception (EX-001 only).

### E28 · widgets (V1.1, journey 13)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E28-T01 | Contract: widget snapshot JSON (`SafeToSpendAmount`, `BudgetPercentage` only), refresh triggers (EX-001) | LEAD | Both | E03 | — |
| E28-T02 | Widgets: Left to spend, Quick Scan, Next charge, Quick-log (WidgetKit / Glance) | DEV | Both | T01, T05, T06, E11 | `448:30659` |
| E28-T03 | Deep links (Q-06 / DG-21) | DEV | Both | T02 | DG-21 |
| E28-T04 | QA verification | QA | Both | T02, T03, T05, T06 | — |
| E28-T05 | iOS snapshot writer: App Group file, `NSFileProtectionCompleteUntilFirstUserAuthentication`, rewritten on every data change; Privacy Mode on → both values `"••••••"` | IOS | iOS | T01 | — |
| E28-T06 | Android snapshot equivalent (EX-001 open point) | AND | Android | T01 | — |
Key ACs: Given left ฿6,450 and 84%, Then the snapshot holds exactly those 2 keys; *edge:* Privacy Mode on → both read "••••••". *security:* the snapshot file holds no other key, and the main ledger is never in the App Group.

### E18 · forecast (V1.1)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E18-T01 | Contract: forecast formula + cases. **Horizon = current budget cycle end (Ton Q-47)**; lines: Cash & bank (Total Cash Balance) + income dated after today up to cycle end − cash/bank-paid bills due up to cycle end − card payments due (E10-T13) up to cycle end − daily spending ("฿<per day>/day × <days left> days", identical to Home). Next-cycle salary excluded. Line totals: **Q-51** (provisional golden values in `golden-sample-data.md` §4.5) | LEAD | Both | E16, E11, E03, E10-T13 | — |
| E18-T02 | 9J On track; title "Balance on <cycle end>" | DEV | Both | T01 | `448:15814` (frame figures to be re-synced, DG-48 / DG-51) |
| E18-T03 | 9K Shortfall | DEV | Both | T02 | `448:15956` |
| E18-T04 | 9L Cash Flow + forecast card | DEV | Both | T02, E12-T06 | `448:7356` |
| E18-T05 | Hero tap → forecast | DEV | Both | T02, E03-T03 | `448:6722` |
| E18-T06 | QA verification | QA | Both | T02–T05 | — |
Key ACs (revision 4, golden dataset, Ton Q-47; the two line totals marked † are provisional until Q-51):
- Given the golden dataset (payday 25, today 18 Nov 2026), When 9J opens, Then the title reads "Balance on 24 Nov", lines are Cash & bank "฿56,898", Income "฿0" (the 25 Nov salary is excluded), Fixed bills "−฿599" (AIS, 22 Nov), Card payments "฿0" (KBank Credit is due 10 Dec, outside the horizon), Daily spending "฿921/day × 7 days" "−฿6,450"†, and the balance "฿49,849"† with status On track.
- *edge:* Given the forecast and Home on the same day, Then the forecast's per day and days left equal the Home hero's (฿921, 7) — never ฿586 / 11 or ฿1,075 / 6.
- *edge:* Given no payday set (cycle 1–30 Nov) on 18 Nov with ฿10,650 left, Then the title reads "Balance on 30 Nov" and the daily line reads "฿819/day × 13 days".
- *edge:* Given a computed balance below ฿0 (e.g. Cash & bank ฿5,000 with the same lines), Then the status is Shortfall and the balance reads "−฿2,049"†.
- *security:* masked in Privacy Mode.
- **Superseded (revision 3) — kept for history:** the old 9J figures (62,400 + 52,000 − 18,240 − 24,960 − 6,450 = ฿64,750) used a 30 Nov horizon and a cut-off-dated card line.
- **Revision 3 conflict (resolved by Ton Q-47 on 21 Nov):** the 9J/9K line "Card payments · KBank Credit · 25 Nov" (−฿24,960) uses the cut-off date. Under §5 rule 11 the payment is due 10 Dec, which falls outside the "Balance on 30 Nov" horizon, so 9J would read ฿89,710 (64,750 + 24,960). Which horizon applies (30 Nov, the cycle end 24 Nov, or 30 days ahead) is **Q-47**; the 9J/9K frames were not changed. The E18 plan sets the final ACs once Q-47 is answered.
- **Checked in Figma (BA, read-only, 21 Nov):** 9J `448:15814` also shows "Daily spending · ฿586/day × 11 days" (= ฿6,450 ÷ 11, i.e. days after today up to 30 Nov). So the same screen set has three per-day figures for the same ฿6,450: hero ฿1,075 (÷ 6, to 24 Nov), forecast ฿586 (÷ 11, to 30 Nov), Q-16 ฿921 (÷ 7, to 24 Nov incl. today). With the payday cycle, "budget pace" past 24 Nov spans the next cycle. Q-47 must also settle how the forecast's daily-spend line is computed; DG-48 covers the 9J figure once it is. **Resolved:** Ton set ฿921 (÷ 7 to the 24 Nov cycle end) for both Home and the forecast.

### E26 · goals (V1.2, journey 15)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E26-T01 | Contract: Goal | LEAD | Both | E10 | — |
| E26-T02 | 10A Goals filter | DEV | Both | T01 | `580:31286` |
| E26-T03 | 10B / 10C / 10D | DEV | Both | T02 | `580:31432`, `580:31578`, `580:31725` |
| E26-T04 | 10E New goal | DEV | Both | T01 | `580:31871` |
| E26-T05 | 10H top-up + 10I picker | DEV | Both | T03, E02 | `580:32428`, `580:32606` |
| E26-T06 | 10J Withdraw; 10F Complete | DEV | Both | T03 | `580:32897`, `580:32039` |
| E26-T07 | 10G Home pinned goal | DEV | Both | T05, E03 | `580:32219` |
| E26-T08 | QA verification | QA | Both | T02–T07 | — |
Key ACs: left ฿6,450 + a ฿5,000 ring-fenced top-up → ฿1,450; *edge:* withdrawing more than saved is blocked. *security:* Confidential.

### E27 · trips (V1.2, journey 16)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E27-T01 | Contract: Trip, members, sub-budgets, multi-currency + FX (Q-27), split, settlement | LEAD | Both | E02 | — |
| E27-T02 | 11A / 11B / 11C | DEV | Both | T01, E12 | `580:34865`, `580:35068`, `580:35158` |
| E27-T03 | 11D / 11E / 11F | DEV | Both | T02 | `580:35395`, `580:35583`, `580:35739` |
| E27-T04 | 11I JPY keypad + 11J / 11K split | DEV | Both | T03 | `580:36356`, `580:36525`, `580:36770` |
| E27-T05 | 11G Settle up | DEV | Both | T03 | `580:35915` |
| E27-T06 | 11H Home trip pill | DEV | Both | T02, E03 | `580:36156` |
| E27-T07 | 11L slip on trip | DEV | Both | T03, E08 | `580:37009` |
| E27-T08 | QA verification | QA | Both | T02–T07 | — |
Key ACs: ¥3,000 split Equally among 3 → ¥1,000 each; *edge:* Exact shares that don't sum to the total block Done. *security:* names are Confidential.

### E21 · sync-backend (V2.0)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E21-T01 | `openapi.yaml` sync resources; auth reusing the V1 Apple / Google identities | LEAD | Both | V1.0 | — |
| E21-T02 | E2E content key + recovery (Q-33; aligned with the Q-39 backup key) | LEAD | Both | T01 | — |
| E21-T03 | `backend/` service | LEAD | — | T01, T02 | — |
| E21-T04 | Client sync engine | DEV | Both | T01–T03 | — |
| E21-T05 | Certificate pinning | DEV | Both | T04 | — |
| E21-T06 | QA | QA | Both | T04, T05 | — |
Key AC: a synced memo is ciphertext the server can't decrypt; *edge:* a pin mismatch → offline state.

### E22 · household-family (V2.0)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E22-T01 | Contract: Space, Member, split, settlement | LEAD | Both | E21 | — |
| E22-T02 | W-D, W-C, Household wallet | DEV | Both | T01 | `448:12297`, `448:11939`, `448:12163` |
| E22-T03 | 2B Family split | DEV | Both | T01 | `448:5780` |
| E22-T04 | 2D Family | DEV | Both | T03 | `446:10547` |
| E22-T05 | 1B Settlement alert | DEV | Both | T01 | `446:10852` |
| E22-T06 | Invite (DG-19) | DEV | Both | T01 | DG-19 |
| E22-T07 | QA | QA | Both | T02–T06 | — |
Key AC: Ton paid ฿2,500 more, split 50/50 → "Nui owes you ฿1,250"; *edge:* Settlement ranks below Budget. *security:* E2E.

### E23 · sync-devices (V2.0)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E23-T01 | 6A "Sync & devices (V2.0 — not in V1.0)" (entry Q-01 / DG-18); device list has no web app row; status "Live on both" | DEV | Both | E21 | `448:30549` / Light `448:30604` |
| E23-T02 | Sync states | DEV | Both | E21 | `448:30741` |
| E23-T03 | 1G Offline | DEV | Both | T02 | `446:10988` |
| E23-T04 | Import Money Manager (DG-20) | DEV | Both | E21 | DG-20 |
| E23-T05 | QA | QA | Both | T01–T04 | — |
Key AC: 3 queued offline → "Offline · 3"; *edge:* reconnect → 0; *edge:* Given a V1.0 build, Then no screen navigates to 6A. *security:* the import file is deleted after import.

### E15 · budget-cycle (unassigned, Q-44)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E15-T01 | Contract: category limits; cycle start comes from the payday (§5 rule 10) | LEAD | Both | E03 | — |
| E15-T02 | 9A Budget & Cycle + Phase 1.5 states (since 21 Nov: 25th selected, "Current cycle: 25 Oct – 24 Nov 2026, set by your payday.") | DEV | Both | T01 | `448:15578` (segments `448:15605` / `448:15606`, Light `448:15668` / `448:15669`), `448:31560` |
| E15-T03 | 9B over cap | DEV | Both | T02 | `448:15704` |
| E15-T04 | Category statuses in 4A | DEV | Both | T02, E12-T03 | `448:6926` |
| E15-T05 | Settings row + 1L chip → 9A | DEV | Both | T02 | `448:29755`, `446:11256` |
| E15-T06 | QA | QA | Both | T02–T05 | — |
Key ACs: limits ฿32,500 of ฿40,000 → Save enabled; *edge:* ฿42,000 → "฿2,000 over", Save blocked. *security:* masked in Privacy Mode.

### E20 · tax-pro (unassigned, Q-44)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E20-T01 | Contract: #tax-deductible, Pro entitlement (Q-22) | LEAD | Both | E19 | — |
| E20-T02 | 9N Tags sheet | DEV | Both | T01, E08-T06 | `448:6546` |
| E20-T03 | 9M Tax deductions (Q-03) | DEV | Both | T01 | `448:16098` |
| E20-T04 | Paywall + StoreKit 2 / Play Billing (DG-14) | DEV | Both | T01 | DG-14 |
| E20-T05 | QA | QA | Both | T02–T04 | — |
Key ACs: 42 receipts ฿186,400; *edge:* non-Pro → paywall. *security:* the entitlement is store-verified.

### E24 · smart-banner (unassigned, Q-44)
| ID | Task | Owner | Platform | Depends on | Figma |
|---|---|---|---|---|---|
| E24-T01 | Detect a recent slip screenshot on-device | DEV | Both | E08 | `448:5942` |
| E24-T02 | 2A Smart Banner with × | DEV | Both | T01 | `448:5942` |
| E24-T03 | QA | QA | Both | T01, T02 | — |
Key AC: a slip screenshot inside the detection window (set in the E24 plan) → banner; *edge:* × → chips return. *security:* no photo leaves the device.

### 6.1 Screen map delta — v5.1 audit fix pass (21 Nov 2026)
Frames whose content, copy or rule changed. Node ids from CLAUDE.md and the audit fix status table. Same node ids unless noted; feature specs must use the current frames.

| Screen state | Journey step | v5.1 Dark | v5.1 Light | What changed | Task(s) |
|---|---|---|---|---|---|
| Onboarding 3 | O6·3 (journey 01) | `448:5106` | `448:5210` | Now "Know every bill before it lands" (Fixed costs hero `615:37399` / `615:37479`, rows `615:37436` / `615:37516`, chip `615:37462` / `615:37542`); motion not designed | E04-T02, T03, DG-47 |
| Onboarding 3 (old, household) | — | `614:37371` | `614:37475` | **Do not build** ("v5.1 — replaced 21 Nov 2026"); household is V2.0 | — |
| Onboarding 1, 2 | O6·1, O6·2 | `448:4716`, `448:4808` | twins | Copy: chip "On track for payday"; "Scan a slip. / We log it.", pill "QR read on this iPhone"; hero tile labels `text-on-light` | E04-T02, DG-49 |
| Sign in | journey 01 | `448:5314` (text `448:5327`) | `448:5344` (text `448:5357`) | "Encrypted on this iPhone · back up to your private iCloud"; Light "Continue as Guest" `text-primary` | E04-T04, T11, DG-41, DG-49 |
| Home heroes (all states) | H1, 1B–1M | `448:6722`, `448:6790`, `446:10784`, … | twins | "6 days left", per day = left ÷ 6 (**wrong vs Ton Q-16 / Q-48**: must read "7 days left · ฿921/day", DG-48); `on-primary-soft` 88%; Over budget detail "of ฿40,000 · ฿41,200 spent" | E03-T03, T04, DG-48 |
| Home 1H | 1H | `446:10152` | twin | "Reads the QR code on Thai bank e-slips, right on this iPhone." | E03-T12, DG-49 |
| Home 1I (Dec cycle) | 1I | `446:11062` | twin | "29 days left", ฿1,379 (**wrong vs Q-16 / Q-48**: "30 days left · ฿1,333/day") | E03-T12, DG-48 |
| Wallet KBank Credit | W-A (journey 07) | `448:11831` | twin | "Due in 22 days" (payment due 10 Dec), cut-off 25 Nov as statement date only | E10-T03, T13 |
| Fixed costs ✓ Paid badge | 5A (journey 08) | `448:13650` (section `448:13649`) | twins | Solid `tint-mint` + `text-on-light` | E11-T03, T15 (done) |
| Fixed costs 5B callout | 5B | `448:13712` | `448:13743` (text `I448:13752;287:965`) | Light callout ink `text-on-inverse` | E11-T04 |
| Subscription detail 5F | 5F | `448:13988` (button `448:14043`) | button `448:14099` | "Cancel subscription" on `night/bg` + `glass-stroke` | E11-T06 |
| Restore confirm 7F | 7F (journey 12) | `448:30157` (row `448:30220`) | row `448:30290` | Data-loss row on `night/bg` + `glass-stroke` | E05-T07 |
| Settings 7A / 7B | 7A, 7B | `448:29581`, `448:29755` | twins | "Budget & Cycle · ฿40,000 · 25th"; footer "Caffeine 1.0 (2026.11) · Made in Bangkok" | E05-T02 |
| Budget & Cycle 9A | 9A (journeys 02, 09, 11, 12) | `448:15578` (segments `448:15605` / `448:15606`) | segments `448:15668` / `448:15669` | 25th selected, "set by your payday" | E15-T02 (unassigned, Q-44) |
| Export 9I | 9I | `448:30297` | twin | "Full ledger · opens in Excel and Numbers" | E19-T02, DG-49 |
| Sync & devices 6A | 6A (journey 13) | `448:30549` | `448:30604` | Renamed "(V2.0 — not in V1.0)", web app row removed, "Live on both" | E23-T01 |
| Forecast 9J / 9K | 9J, 9K (journey 11) | `448:15814`, `448:15956` | twins | **Not changed yet**: "Balance on 30 Nov", card line dated 25 Nov (cut-off), "฿586/day × 11 days". Must become "Balance on 24 Nov", no card line inside the horizon, "฿921/day × 7 days" (Ton Q-47; DG-48, DG-51) | E18-T01, T02, T03 |
| Trips 11F / 11G | 11F, 11G (journey 16) | `580:35739`, `580:35915` | twins | "Scan it, or pick it from Photos"; repayment-slip copy (no share extension) | E27-T03, T05 |
| 2C batch | 2C (journey 06) | `446:10383` | twin | "Type the amount" | E09-T06 |

Copies of these frames on Feature Journeys (re-cloned: `615:63581`, `615:63700`, `615:63877`, `615:63993`, `615:64041`, `615:64202`, `615:64363`, `615:64524`, `615:64685`, `615:64789`, `615:65066`) and on the App Prototype (edited in place: O6·3 `540:22150`, 9A `540:23197`, 6A `540:40864`, 5F `540:35062`, 7F `540:40749`) carry the same changes. The ux-ui-designer inventory `docs/design/figma-inventory-v5.1.md` still names `448:5106` "One wallet for the whole home" (owner: ux-ui-designer, to refresh).

---

## 7. Design gaps (route to `ux-ui-designer`)
DG-01 to DG-21: Figma journey 14. DG-22 to DG-38: found by `ba` (revision 1). DG-39 to DG-46: created by Ton's decisions (revision 2).

| ID | Gap | Blocks | Status / Ton input |
|---|---|---|---|
| DG-01 | **Splash** (under 0.5 s, while the store initialises) | E00-T20 | Ton Q-04 defines the behaviour |
| DG-02 | Lock on launch = privacy shield + automatic Face ID / fingerprint prompt (same shield as DG-26) | E06-T03 | Ton Q-04 defines the behaviour |
| DG-03 | Notifications list (bell) | E13-T04, E03-T13 | Q-05 open |
| DG-04 | Settings › Saved Favorites | E02-T12 | — |
| DG-05 | **Add Account sheet**: one bottom sheet; fields Account Name, Account Type (Cash / Bank Account / Credit Card / E-Wallet), Initial Balance, Card Colour / Icon, Include in Net Worth (default on); Credit Card adds Credit Limit, Statement Cut-off Day (1–31), Payment Due Day (1–31); entry points Wallet "+ Add Account" and Dashboard empty state | E01-T10, E10-T08, E03-T12 | **Spec from Ton Q-13** (decisions file) |
| DG-06 | Edit / reorder category | E01-T11 | Q-09 open |
| DG-07 | Net worth detail | E10-T11 | — |
| DG-08 | Manage accounts · Archived | E10-T11 | — |
| DG-09 | Reconnect account | E10-T11 | Q-35 open |
| DG-10 | Payoff calculator | E11-T11 | — |
| DG-11 | Add subscription form | E11-T11 | — |
| DG-12 | Duplicate (pre-filled keypad) | E07-T10 | Q-07 open |
| DG-13 | Details edit mode | E07-T13 | Q-07 open |
| DG-14 | Pro paywall | E20-T04 | Q-22 / Q-44 open |
| DG-15 | Primary Currency | E05-T09 | — |
| DG-16 | Default Accounts & Slip Mapping | E05-T09 | — |
| DG-17 | App Lock / Privacy / Help / Legal pages | E05-T09, E06-T02 | — |
| DG-18 | Sync & devices entry point | E23-T01 | Q-01 open (V2.0) |
| DG-19 | Invite flow | E22-T06 | V2.0 |
| DG-20 | Import Money Manager backup | E23-T04 | V2.0 |
| DG-21 | Widget deep links | E28-T03 | Q-06 open (V1.1) |
| DG-22 | Secure store failure screen | E00-T10 | — |
| DG-23 | Tab placeholders: confirm scaffold only | E00-T06 | — |
| DG-24 | Camera permission denied / restricted | E08-T09 | — |
| DG-25 | Photos access fully denied | E09-T07, E01-T09 | — |
| DG-26 | **Privacy shield** (app switcher, always on; also the background of the App Lock prompt) | E00-T21, E06-T03 | Ton Q-04 |
| DG-27 | Delete my data (PDPA) | E05-T10 | — |
| DG-28 | Android variants: Photo Picker, BiometricPrompt, back behaviour, **Google Drive backup** on 7C / 7D / 7F, `.caffeine` export / import entry | E05-T08, E05-T13, E06-T02, E09-T02 | Ton Q-12 |
| DG-29 | Notification permission pre-prompt | E13-T01 | — |
| DG-30 | Duplicate slip warning (bank code + transaction reference match) | E08-T12, E09-T04 | Ton Q-14 |
| DG-31 | New category: keyboard, duplicate name, Income variant, crop, Remove photo | E01-T08, E01-T09 | — |
| DG-32 | Sign-in failure / cancel states (Apple and Google) | E04-T04, E04-T11 | — |
| DG-33 | Budget edit in V1.0 (9A is unassigned) | E03-T07 | Q-44 open (Q-15 answered) |
| DG-34 | ✓ Paid badge mint on mint (section F) | E11-T15 | **Closed 21 Nov 2026** (solid `tint-mint` + `text-on-light`) |
| DG-35 | Goals / Trips / Profile States boards only on draft pages | E25–E27 G2 | — |
| DG-36 | Seed categories: 2E grid (11) vs `caffeine-domain` (8) | E01-T02, E01-T07 | Q-38 open |
| DG-37 | Thai layouts / font | E14-T06 | Q-19 open |
| DG-38 | Glass fallback on Android API 28–30 | Android UI tasks | — |
| DG-39 | **Dashboard empty state "Add Account" button** (1H) | E03-T12 | Ton Q-13 |
| DG-40 | **+ long-press context menu**: Scan Slip (camera), Pick Slip from Photos, Add Transfer. This differs from the current 1N grid (5 tiles) `446:10311`, which is no longer the + target | E02-T10 | Ton Q-17 |
| DG-41 | **Sign in screen**: add **Continue with Google** on iOS (with Apple and Guest), and Google (primary) + Sign in with Apple + Guest on Android; update `448:5314` | E04-T04, E04-T11, E04-T12 | Ton Q-11 |
| DG-42 | **Mark paid confirmation sheet**: amount, paying account, payment date, Confirm / Cancel | E11-T17 | Ton Q-21 |
| DG-43 | **"Link this transaction to your upcoming <bill> bill?"** prompt in 2B and 2D | E11-T18 | Ton Q-21 |
| DG-44 | **Privacy-safe notification copy** set (no amounts, no account names); Ton's approved examples are the style | E13-T02, E13-T03 | Ton Q-18 (+ Q-40) |
| DG-45 | 2D badge / tag copy when amount, date and recipient come from OCR (today "QR parsed (local)" implies the QR holds them, which Ton Q-14 says it doesn't) | E08-T06 | Ton Q-14 |
| DG-46 | **App Prototype fix**: + tap goes to 1N today, which is wrong; tap → 2A Expense, long-press → the DG-40 menu | prototype only | Ton Q-17 |
| DG-47 (rev 3) | **Onboarding page 3 motion**: the new Fixed costs vignette (`448:5106` / `448:5210`) has no keyframes (the orbit motion went with the old children); timings, order and Reduce Motion final state needed in the spec | E04-T03 | — |
| DG-48 (rev 3, rev 4) | **Hero and forecast derived figures contradict Ton Q-16 / Q-48 / Q-47.** Every Home hero must read **"7 days left · ฿921/day"** on 18 Nov (now "6 days left · ฿1,075/day"); 1I "30 days left · ฿1,333/day" (now "29 days left · ฿1,379"); the other per-day figures left ÷ 6 (฿241 goals, ฿6,666, ฿2,533, ฿533, ฿1,966, ฿207,633) are recomputed ÷ 7. **9J / 9K:** "Balance on 24 Nov", daily-spending line "฿921/day × 7 days" (now "฿586/day × 11 days"), and no KBank card line (due 10 Dec, outside the horizon). 1B (80% used on day 25 of 31) shows Over pace but computes On track: change 1B's data or its status (audit Q-A3; design choice only). The Budget hero v5 main component on Home v5 still defaults to "spending paused". Simplest path: re-sync to the golden sheet (DG-51) | E03-T03, E03-T12, E18-T02, T03 (spec screenshots) | Ton Q-16, Q-48, Q-47 (all binding) |
| DG-49 (rev 3) | **Android copy for platform-named strings**: "Encrypted on this iPhone · back up to your private iCloud" (Sign in; Android backs up to Google Drive, Ton Q-12), "QR read on this iPhone" (O6·2), "right on this iPhone" (1H), "opens in Excel and Numbers" (9I) | E04-T02, T11, E03-T12, E19-T02 (Android lanes) | Ton Q-12 |
| DG-50 (rev 3) | **Status-bar "9:41" contrast** on 42 v5.1 frames (bound to `Labels/Primary`: 1.23:1 Dark, 1.05:1 Light; re-theme rule says `text-primary`). Figma-only: the real status bar is drawn by the OS and foundation T-05 already follows `night/text-primary` | none in code | **Closed, won't fix (design), Ton Q-49.** Handoff note: builds use the native OS status bar (§5 rule 13); every spec says so |
| DG-51 (rev 4) | **Re-sync frames to the golden sample-data sheet and glossary** (findings 14, 15): one "today" (Wed 18 Nov 2026), one set of accounts and masked numbers (Savings ··4410, Credit ··7731), the figures in `golden-sample-data.md`, the terms in `glossary.md` (9A footnote "Left to spend"); Thai strings only after Ton reviews the Thai column. Finding 13 (category budgets) waits for Q-44 | every feature spec from now on; QA screenshot checks | Ton, findings 13–15 |
| DG-52 (rev 4) | **DS values on Home v5 become the global standard** (Ton Q-50): no page-level overrides or pins on Home v5; check that the global variables and main components (Picker tile label `68:478`, `night/income-text` in Date header, Chart callout, Fixed cost row, Ledger row, History summary row, the v5.1 DS-sync defaults) carry these values, so every screen inherits them | E00-T01 token diff, every spec | Ton Q-50 |

### 7.1 Audit findings 13–15 (deferred in the fix pass; **scheduled by Ton on 21 Nov for the next handoff package**)
Ton's decision: a golden sample-data sheet and a bilingual EN / TH glossary. BA drafts: [`golden-sample-data.md`](golden-sample-data.md), [`glossary.md`](glossary.md) (Thai column "draft — Ton to review"). ux-ui-designer re-syncs the frames under DG-51. These do not change what code computes (every figure comes from state, §5 rule 6), but they make frames and screenshots disagree with each other. Until DG-51 is done, **QA compares layout, tokens and copy patterns against the spec, never sample numbers across screens**, and feature plans take strings from the frame of the screen being built.
| Finding | What is inconsistent | Affects | Needed |
|---|---|---|---|
| 13 | One category, two budgets in one month: Home 1F "Food & Drink over budget by ฿710 · ฿2,710 of ฿2,000" vs Reports "฿5,715 of ฿5,000 · Over by ฿715"; Reports ฿36,600 vs 9A "฿32,500 allocated"; different category lists | E03-T09, E12-T03, E12-T05, E15 | Category-budget model decision (part of Q-44: where category limits live) and one sample set |
| 14 | Sample data: "today" 18 Nov vs 16 Nov vs "MON Today"; ··4410 used for two accounts and 4417 for one card; iPhone 16 vs iPhone 17 Pro plans; Sofa ends Mar vs Feb 2027; net worth ฿438,030 vs ฿412,850; Fixed costs income vs History income; 10F / 11B / 11C goal-trip timing | every QA screenshot check, E10, E11, E12, E26, E27 | `golden-sample-data.md` (draft) → DG-51. Goals / Trips data (V1.2) is added to the sheet when E26 / E27 are planned |
| 15 | Naming drift: "Left to spend" vs "Safe to Spend" (9A footnote); tab "Analytics" vs title "Reports"; Space named Family / Household / Shared / Family split / Household wallet; "Ton Raweephat" vs "Raweephat S."; partner Nui vs Fon; 4D "Debts" vs "Liabilities" | string ACs in E03, E12, E15, E22, E23 | `glossary.md` (draft): "Safe to Spend" = UI "Left to spend"; Total Cash Balance, Net Cash Flow, Net Worth defined. Still for Ton: glossary G-7 (Debts vs Liabilities), G-8 (Analytics vs Reports), G-9 (space names, V2.0) |

---

## 8. Open questions
37 questions were raised in revision 1 (Q-01 to Q-38; Q-37 not used). **11 answered by Ton on 2026-11-21** (see the [decisions file](../decisions/2026-11-21-ton-answers.md)). Revision 2 adds 8 new questions (Q-39 to Q-46). Revision 3 adds 4 (Q-47 to Q-50) and narrows Q-15. **Revision 4: Ton answered Q-15, Q-47, Q-48, Q-49 and Q-50** (decisions file Part 3) and BA adds Q-51 to Q-53. **36 are open.**

### 8.0b Answered by Ton, second round (21 Nov 2026; binding text in the decisions file, Part 3)
| # | Topic | Ton's answer, in short | Applied in |
|---|---|---|---|
| A1 | Budget cycle | Payday drives the cycle (copied from CLAUDE.md into the decisions file) | §5 rule 10, foundation T-02 / T-14 |
| A2 | Card due date | Payment due date drives badge, reminders, forecast; cut-off = statement date only (copied from CLAUDE.md) | §5 rule 11, E10-T13 |
| Q-48 | Days-left badge | (cycle end − today) + 1, today included: "7 days left · ฿921/day" on 18 Nov; last day "1 day left" | §5 rule 9, E03-T03 + ACs, foundation T-14 / AC-53, DG-48 |
| Q-15 | Payday 29–31 | Clamp to the last valid day of shorter months, never roll into the next month; plus "Last day of the month" | §5 rule 10, foundation T-02 / T-09 / T-14, AC-19, AC-38a–e, E04-T05, golden §6 |
| Q-47 | Forecast horizon | Current cycle end (24 Nov / 30 Nov); daily line = Home per day (฿921); next-cycle salary excluded; card due 10 Dec outside | E18-T01–T03 + ACs, DG-48 |
| Q-49 | Figma "9:41" | Leave it; builds use the native status bar | §5 rule 13, DG-50 closed |
| Q-50 | DS changes on Home v5 | Keep; they are the global standard; no pins on Home v5 | DG-52 |
| 13–15 | Sample data, naming | Golden sample-data sheet + bilingual EN / TH glossary in the next handoff package | §5 rule 14, §7.1, DG-51, `golden-sample-data.md`, `glossary.md` |

### 8.0a Settled by the 21 Nov 2026 audit fix pass (now also in the decisions file, Part 3 A1 / A2)
| Topic | Rule | Applied in |
|---|---|---|
| Budget cycle (audit 11) | Payday drives the cycle (sample 25th–24th) | §5 rule 10, E03, E04, E05, E16-T01, foundation AC-37a / AC-43a / AC-51a |
| Card due date (audit 12, "Ton's default") | Payment due date drives badge, reminders, forecast; cut-off = statement date only | §5 rule 11, E10-T13, E10-T03, E13-T03, E18-T01 |
| Onboarding page 3 (audit 01) | Fixed costs, not household | E04-T02 |
| Per day divisor (audit Q-A2) | **Already answered by Ton Q-16** (today counts, ÷ 7 on 18 Nov → ฿921). The Figma ÷ 6 figures are a design error, not an open question | DG-48 |
Done in revision 4: the first two rows are copied into the decisions file (Part 3, A1 and A2).

### 8.0 Answered (2026-11-21)
| # | Topic | Ton's answer, in short (binding text is in the decisions file) | Applied in |
|---|---|---|---|
| Q-04 | Launch | Splash under 0.5 s; App Lock off → Dashboard; on → shield + auto biometric prompt; app-switcher always shielded | E00-T20–T22, E06-T03, DG-01, DG-02, DG-26 |
| Q-10 | Roadmap | V1.0 / V1.1 / V1.2 / V2.0 as in §2 | §2–§4 |
| Q-11 | Sign in | Identity for the backup key + future sync; iOS Apple + Google + Guest; Android Google + Apple (web OAuth) + Guest | E04-T04, T09–T12, DG-41 |
| Q-12 | Android backup | One Cloud Backup interface: iCloud Drive private container / Google Drive `drive.appdata`, client-encrypted; plus a `.caffeine` encrypted export | E05-T01, T05, T08, T13, DG-28 |
| Q-13 | First account | Auto-create ฿0 Cash at onboarding end; Add Account sheet (fields as DG-05) | E01-T01, T03, T10, E04-T07, E03-T12, E10-T08 |
| Q-14 | E-slip | QR = bank code + transaction ref only; hybrid barcode + OCR on-device; spike with 6 banks | E08-T00–T02, T11, T12, DG-45 |
| Q-16 | Rounding | Per day floors and counts today; budget % half-up with the 99% rule; % vs previous month integer, ">999%" | E00-T18, T19, E03-T02, E12, §5 rule 9 |
| Q-17 | + button | Tap → 2A; long-press → Scan Slip / Pick Slip from Photos / Add Transfer; the prototype is wrong | E02-T09, T10, DG-40, DG-46 |
| Q-18 | Notifications | No amounts and no account names; approved generic copy | E13, §5 rule 8, DG-44 |
| Q-21 | Mark paid | Creates an expense via a confirmation sheet; dedup prompt in 2B / 2D | E11-T05, T17, T18, DG-42, DG-43 |
| Q-30 | Widgets vs protection | Split storage; widget snapshot exception (EX-001) | E00-T02, T09, E28-T01, T05, T06, `docs/security/exceptions.md` |

### 8.1 Open blockers to answer next (Ton)
| # | Question | Blocks |
|---|---|---|
| **Q-39** (new) | **Backup key recovery** (security-standard §4): Ton Q-11 ties the backup key to sign-in, but restoring on a new phone needs the key there. Options: a key synced via the platform keychain (iCloud Keychain; Android has no direct equivalent), a user recovery passphrase, or a second device. Also: can a Guest back up? How is a `.caffeine` file protected (passphrase?) so it can be opened on another device? | E04-T09, E04-T10, E05-T05, T08, T13, E21-T02 |
| **Q-40** (new) | **Category names in notifications**: Ton's approved example "Your Food & Drink spending is nearing its monthly limit" names a category, and category is **Confidential** in `security-standard` §2 ("never in notifications in clear" applies to Restricted; §6 says no Confidential in notifications). Approve category names as an exception (adding it to `exceptions.md`), or use fully generic copy ("One of your categories is nearing its limit")? | E13-T02, DG-44 |
| **Q-46** (new) | **Sign in with Apple on Android** via web OAuth needs a registered return URL and a server-signed client secret, which means a small backend in a local-first V1. Build a minimal auth endpoint in V1.0, or move Android Apple sign-in to V2.0 with the sync backend? | E04-T12 |
| **Q-43** (new) | **"Link to bill" match rule** (Ton Q-21): what counts as a match? Exact amount? Name / merchant? Within how many days of the due date? What if two bills match? | E11-T01, E11-T18, DG-43 |
| **Q-44** (new) | Not in the roadmap: **Budget & Cycle category limits (9A / 9B)**, **Tax deductions (9M, Pro)** and **Smart Banner**. Which release? And where does a V1.0 user edit the monthly budget after O5? | E15, E20, E24, E03-T07, E12-T05, DG-33 |
| **Q-45** (new) | **"Core achievements"** for V1.0: which of the 10 badges ship? | E25-T01 |
| Q-07 | History Duplicate and Edit: open 2A or 2B, in which mode? | E07-T10, E07-T13 (V1.0) |
| **Q-52** (rev 4) | **Period labels under a payday cycle.** The cycle 25 Oct–24 Nov is labelled "PERSONAL BUDGET · NOV" on Home, while the Home month pill, 1J month sheet, History period picker and Analytics "vs Oct" use calendar months. Golden data shows the gap: cycle-to-date Out ฿33,550 vs calendar-November Out ฿29,350 (and November has no income, so History would read "Total outflow ฿29,350"). Do History, Analytics and the Home month pill follow the budget cycle or the calendar month, and which month name labels a cycle? | E03-T03, T11, E07-T05, E12-T01, foundation (a possible `BudgetCycle.label`) |
| **Q-53** (rev 4) | **Card cut-off / due days 29–31.** The old Q-15 asked this too, but Ton's clamping answer names payday only. Do card cut-off and due days clamp the same way (31 → 28 Feb)? | E01-T10, E10-T13 |

### 8.2 Other open questions
| # | Question | Blocks |
|---|---|---|
| Q-01 | Where does 6A open from? | E23-T01 (V2.0) |
| Q-02 | Is Fixed costs pushed from Wallet or only from the Bills alert? | E11-T13 |
| Q-03 | Where does 9M live? | E20-T03 |
| Q-05 | What does the bell open? | E03-T13, E13-T04 |
| Q-06 | Widget deep links | E28-T03 (V1.1) |
| Q-08 | O5: payday required? Does Guest see O5? | E04-T05, E16 |
| Q-09 | Categories & Tags: reuse 2E? | E01-T11, E05 |
| Q-19 | V1 languages (Thai?) | E05-T04, E14-T06 |
| Q-20 | Space pill in single-user V1 | E03-T13, E10 |
| Q-22 | Pro tier details | E20 |
| Q-23 | Analytics / crash SDK in V1? | E14-T07 |
| Q-24 | Android font (Roboto default, non-blocking) | E00-T01 |
| Q-25 | Bundle id, team, Play account | E14-T01 |
| Q-26 | App icon A / B / C | E14-T02 |
| Q-27 | Trips FX rate source and THB conversion | E27 (V1.2) |
| Q-28 | Profile open items (weekly amount, hide mission, freelance, Apple ID merge) | E25-T01 |
| Q-29 | 5 Goals & Trips questions in Figma `578:3174` | E26, E27 |
| Q-31 | Android API 28–32: "always shield" needs FLAG_SECURE (blocks user screenshots everywhere). Accept, or best effort? | E00-T22 |
| Q-32 | App Lock re-lock timeout after backgrounding | E06-T01, E06-T03 |
| Q-33 | E2E sync key recovery (align with Q-39) | E21-T02 |
| Q-34 | Keypad max amount and calculator precedence | E02-T03 |
| Q-35 | Is any bank connection ("Reconnect") in scope? | E10-T11 |
| Q-36 | PDPA export: now covered by E19 export + E05-T13 `.caffeine` in V1.0; Ton to confirm this meets data portability | E05, E19 |
| Q-38 | Seed categories: 8 (domain) or 11 (Figma) | E01-T02 |
| Q-41 (new) | "% vs previous month" when the previous month is ฿0: show "—", "New", or hide? | E12-T01 (domain returns `.notComparable`) |
| Q-42 (new) | EX-001 Android equivalent (open point in `exceptions.md`) | E28-T06 (V1.1) |
| **Q-51** (rev 4) | **Forecast line totals** (after Ton Q-47). (a) The daily-spending line shows "฿921/day × 7 days": is its amount the exact Left to spend (−฿6,450) or 921 × 7 (−฿6,447)? (b) An upcoming bill paid from the bank (AIS ฿599, 22 Nov) is a Fixed bills line **and** comes out of the same ฿6,450 budget once paid, so the lines count it twice. Count it twice (golden: ฿49,849) or once (฿50,448)? Counting it once would mean the daily line no longer equals Home's ฿921, which Ton's Q-47 requires | E18-T01 (V1.1); golden §4.5 marked provisional |
| Glossary (rev 4) | Glossary G-7 "Debts" vs "Liabilities", G-8 tab "Analytics" vs title "Reports", G-9 shared space names (V2.0), and the Thai column (draft) | E12, E22, E14-T06 (Q-19) |

---

## 9. Risks
| ID | Risk | Owner | Mitigation |
|---|---|---|---|
| R-1 | OCR accuracy differs per bank and per slip layout | LEAD | Ton Q-14: spike E08-T00 on 6 banks before locking the parser; the unreadable path (P4) is always available |
| R-2 | Search over field-encrypted memo / merchant can't use SQL LIKE | LEAD | E07-T01: in-memory scan or keyed blind index, in the threat model |
| R-3 | Widget data while locked | LEAD | Resolved by EX-001 (iOS); Android point Q-42 |
| R-4 | Backup restore on a new device needs the key there | LEAD | Q-39 |
| R-5 | Figma sample numbers copied into code / ACs | BA, DEV | Lesson; compute from `caffeine-domain` + Q-16 |
| R-6 | SF Pro vs Roboto metrics | UX, DEV | Re-check wraps per spec |
| R-7 | Glass / blur missing on Android API 28–30 | UX | DG-38 |
| R-8 | The App Prototype contradicts the decisions (+ tap) | UX | DG-46 |
| R-9 | Google sign-in on iOS and Drive `appdata` add OAuth scopes and store-review privacy labels | LEAD | E14-T05 |
| R-10 | Redesigned frames recompute derived figures with a rule that differs from Ton's decisions (21 Nov: per day ÷ 6, forecast ÷ 11) | BA, UX | DG-48, DG-51; golden sheet is the single source of figures; lesson logged |
| R-11 | iOS-named copy ships on Android | UX, AND | §5 rule 12, DG-49 |
| R-12 | Token changes live only in Figma and `tokens-changelog.md` until the pipeline exists | UX | Foundation T-01 builds the pipeline; AC-01a / AC-01b cover the 21 Nov values; DG-52 puts the Home v5 values into the global variables first |
| R-13 | The payday cycle and calendar-month screens (History, Analytics, month pill) show different totals for "November" | BA | Q-52; golden sheet shows both figures |
| R-14 | Month-end clamping bugs differ per platform (Feb, leap years, 30-day months) | DEV, QA | Foundation AC-38a–e as shared case rows; golden §6 |

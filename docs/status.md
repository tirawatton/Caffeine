# Pipeline Status (role team)

current_feature: foundation
platform_scope: both
mode: team
status: PLAN_READY

## What next (read this first)
- **Stage (2026-11-21):** the whole-app backlog exists: `docs/plan/caffeine-app-master-plan.md` (revision 7, after Ton's fifth-round answers Q-59 to Q-62: 29 epics E00–E28, 273 tasks, 56 design gaps, 33 open questions). The first feature plan is `docs/plan/foundation-plan.md` (E00, revision 7, PLAN_READY, 24 tasks). Handoff package: `docs/plan/golden-sample-data.md` revision 4 (all values final) and `docs/plan/glossary.md` revision 4 (Debts, Analytics, **Fixed costs (UI) / Commitments (internal)** locked; 9 Thai labels approved, incl. Fixed costs = รายการประจำ). `caffeine-domain` was updated with Ton's approval (Left to spend formula, Mark paid variance, negative state, cycle label, shared clamp, worked examples). Code is still scaffold only in `ios-app/` and `android-app/`.
- **Foundation revisions 3–5 for the agents now in stage 2:**
  - ux-ui-designer T-01: build the token pipeline with `night/income-text` and the 21 Nov token values (AC-01a, AC-01b), after DG-52 puts the Home v5 values into the global variables.
  - backend-lead T-02: `AppSettings` has 9 fields: `cycleStartDay` 1–31 (the payday) + `cycleStartIsLastDay`. Case rows for AC-19, AC-37a, AC-38–AC-38e, AC-43a, AC-44a, AC-51a, AC-51b and **revision 5: AC-43b, AC-46a, AC-51c (Safe to Spend 5,851 → ฿835/day), AC-65–AC-68 (`DayClamp`), AC-69–AC-71 (cycle label "Nov cycle · 25 Oct – 24 Nov")**, from golden revision 2.
  - Golden Home on 18 Nov: **"Nov cycle · 25 Oct – 24 Nov", ฿5,851 left, 84%, Over pace, 7 days left, ฿835/day** (Left to spend = Budget − Actual expenses − upcoming & overdue unpaid fixed costs of every kind due in the cycle, Ton Q-51 B / Q-55 / Q-58). Before E11 exists (no fixed costs) the same data reads ฿6,450 / ฿921. Never Figma's "6 days left · ฿1,075". Dec cycle (25 Nov): ฿25,553 · ฿851/day.
  - **Revision 6 for backend-lead T-02 cases:** new rows AC-43c (committed 14,447 → 25,553), AC-46a (now returns `billsExceedBy` 399), AC-46b (spent 40,000 / 41,200 with 599 committed), AC-51d (฿851/day), AC-54a (−399 → ฿0/day). T-16 gains the output `billsExceedBy`.
  - **Revision 7 for backend-lead T-02 cases:** AC-46b changed: spent 41,200 with 599 committed now gives **overBy = 1,799** (= −leftToSpend, Ton Q-61; was 1,200). New rows AC-46c (committed 15,046 incl. a carried Nov charge → 24,954, Ton Q-60) and AC-51e (฿831/day on 25 Nov, ฿860/day on 26 Nov).
- **Team change (2026-11-21):** new agent `local-data-engineer` (backend team) runs in stage 2 beside ux-ui-designer and hands tables + queries to backend-lead (stage 2b). Foundation has only `AppSettings` (no money query), so it can run in a light pass: tables + schema only. Dry run on the golden data: `docs/data-model/sql/dryrun/` (7 queries, 0 failures).
- **Next agents:** `/caffeine-pipeline foundation both` → stage 2: **ux-ui-designer** (foundation T-01 tokens, DG-01 splash, DG-22 store error screen, DG-23 confirm placeholders, DG-26 privacy shield) **∥ backend-lead** Phase A (T-02 `docs/data-model/foundation-model.md`, `foundation-cases.md`, `docs/security/foundation-threats.md`). Then GATE 1 (Ton), then ios-developer ∥ android-developer.
- **After foundation (V1.0 order, master plan §4):** `accounts-categories` → `add-transaction` → `home-dashboard` → `first-run` → `settings-backup` → `app-lock-privacy` → `history` → `scan-slip` → `batch-import` → `wallet` → `reconcile` → `fixed-costs` → `payday-recurring-income` → `analytics` → `export` → `profile-rewards` → `notifications` → `release-readiness`. `ba` writes each feature plan when the conductor starts it.
- **Ton's decisions (2026-11-21):** `docs/decisions/2026-11-21-ton-answers.md`. Roadmap: V1.0 core MVP (19 epics) · V1.1 widgets + forecast · V1.2 goals + trips · V2.0 household sync.
- **Ton, please answer next (master plan §8.1):**
  - Q-39 backup key recovery / Guest backup / `.caffeine` protection
  - Q-40 category names in notifications vs security-standard
  - Q-46 Android Sign in with Apple needs a server
  - Q-43 "Link to bill" match rule
  - Q-44 release for 9A Budget & Cycle, 9M Tax, Smart Banner, and where V1.0 edits the budget
  - Q-45 core achievements
  - Q-07 Duplicate / Edit mode
  - (Answered 21 Nov: Part 3 Q-15, Q-47, Q-48, Q-49, Q-50, findings 13–15, A1 / A2; Part 4 Q-51, Q-52, Q-53, G-7 Debts, G-8 Analytics, 8 Thai labels; Part 5 Q-54, Q-55, Q-56 (supersedes Q-21 wording), Q-57, Q-58; **Part 6 Q-59 (alert = `night/accent`), Q-60 (carry overdue forward), Q-61 (caption = full deficit), Q-62 (Fixed costs = รายการประจำ)**.)
- **ux-ui-designer, please design before runs 2–5, 8 and 13:**
  - DG-05 Add Account sheet (spec in the decisions file)
  - DG-40 + long-press context menu
  - DG-39 Dashboard empty-state "Add Account"
  - DG-41 Sign in with Google
  - DG-12 / DG-13 Duplicate / Edit
  - DG-42 Mark paid sheet, DG-43 Link-to-bill prompt
  - DG-11 Add subscription
  - DG-46: fix the App Prototype + tap link
  - DG-48 (rev 6): heroes "฿5,851 · 7 days left · ฿835/day"; 1I "Dec cycle · 25 Nov – 24 Dec", ฿25,553, "30 days left", ฿851/day; 9J "Balance on 24 Nov", Fixed bills −฿599, "฿835/day × 7 days" −฿5,851, ฿50,448 (9K −฿1,450), no card line; 1B status vs data
  - DG-53 History calendar-month filter · DG-54 cycle labels on Home / 1J / History / Analytics, "vs Oct cycle", title "Analytics", 4D "Assets / Debts" · DG-55 show the set-aside on the hero (now up to ฿14,447 on day one)?
  - **DG-56 (rev 6):** negative hero state "−฿399" + "฿0/day" + "Bills exceed budget by ฿399" (coral on periwinkle is ~1.1:1, needs a passing placement; Privacy Mode variant); "Overdue" status on Fixed cost row + Bills alert + Skip this cycle; 9J line label "Fixed bills" → "Fixed costs"; no "Commitments" in UI. **Rev 7 additions:** (5) 1K Over budget hero shows "฿0" + "OVER BUDGET BY ฿1,200"; must show "−฿1,799", "฿0/day", "Over budget by ฿1,799" with AIS unpaid ("−฿1,200" / "฿1,200" with nothing set aside), Privacy variant, and the Budget hero v5 main component default; (6) carried overdue row: on 25 Nov 5A lists Nov AIS (Overdue, carried) + Dec AIS (upcoming); a label that tells them apart, Bills alert copy, Skip / Mark paid on the carried row; Thai Fixed costs = "รายการประจำ", never "บิลล่วงหน้า"
  - DG-51: re-sync frames to `golden-sample-data.md` and `glossary.md` · DG-52: Home v5 DS values into the global variables / components (no pins on Home v5)
  - DG-47: onboarding page 3 motion · DG-49: Android copy for "iPhone" / "iCloud" / "Excel and Numbers" strings · DG-50 closed (native status bar note in every spec)
  - Refresh `docs/design/figma-inventory-v5.1.md` (still names `448:5106` "One wallet for the whole home")
  - Full list in master plan §7 (deferred audit findings 13–15 in §7.1).

## Status values (set by agents unless marked HUMAN)
- IDLE: no feature in progress
- PLAN_READY: `ba` done; `ux-ui-designer` and `local-data-engineer` next (parallel), then `backend-lead` Phase A
- PLAN_RETURNED: ux-ui-designer or backend-lead sent the plan back to `ba` (Feedback in Notes)
- DATA_DESIGN_READY: recorded in Notes by `local-data-engineer` (tables + queries proven); `backend-lead` Phase A next
- DATA_RETURNED: recorded in Notes by `backend-lead`; Feedback for `local-data-engineer`
- DESIGN_READY / CONTRACT_READY: recorded in Notes; GATE 1 when both are set
- DESIGN_RETURNED / CONTRACT_RETURNED: a developer sent work back (owner + Feedback in Notes)
- DESIGN_APPROVED: **HUMAN** (Ton says "design approved"); developers next
- BACKEND_DONE: recorded in Notes by `backend-lead` Phase C (Phase 2 sync/API tasks only)
- DEV_COMPLETE: every in-scope lane is `IOS_DONE` / `ANDROID_DONE` (and BACKEND_DONE when Phase C ran); `qa-engineer` next
- QA_PASSED: `backend-lead` review next
- REVIEW_PASSED: lead review clean; beta next
- RELEASED_TO_BETA: TestFlight / Play internal uploaded; production only on Ton's explicit confirmation (**HUMAN**)
- BLOCKED: see Notes for owner and platform

Lane state: `docs/pipeline/ios-status.md`, `docs/pipeline/android-status.md` (written by the developers).
Retry budget: 3 attempts per gate (`.claude/skills/loop-engineering/SKILL.md`).

## Paused features

## Notes
(agents append dated notes: gate results, `<gate> attempt n/3`, BLOCKED owner + platform)
- 2026-11-21 [ba]: Master plan written: `docs/plan/caffeine-app-master-plan.md` (from Figma v5.1 `446:10036` + Feature Journeys `482:29722` via `docs/design/figma-inventory-v5.1.md`). Master checklist 9/9 PASS on pass 2 (pass 1 had an unmapped 9O frame, an untestable E03 AC and a wrong task count; fixed).
- 2026-11-21 [ba] (foundation): PLAN_READY. `docs/plan/foundation-plan.md`, 17 tasks, 50+ ACs, readiness checklist 9/9 PASS on pass 2. No KPI, so no analytics file. No `docs/briefs/foundation-brief.md`: the brief source is Ton's 2026-11-21 master-plan request; the conductor may write the brief from plan §1–§2 for Ton to confirm. Non-blocking open items: Q-24 Android font (Roboto default), Q-15 cycle start day 29–31 (1–28 only for now), DG-22 store error copy.
- 2026-11-21 [ba]: **Decisions received**: Ton answered Q-04, Q-10, Q-11, Q-12, Q-13, Q-14, Q-16, Q-17, Q-18, Q-21, Q-30 (`docs/decisions/2026-11-21-ton-answers.md`).
  - **Plans updated:** master plan revision 2 (re-phased to V1.0 / V1.1 / V1.2 / V2.0; new and changed tasks; DG-39 to DG-46; checklist 9/9 PASS on pass 2) and foundation-plan revision 2 (T-18 per-day floor, T-19 budget % 99% rule and % change >999%, T-20 splash + launch gate hook, T-21 app-switcher shield, T-22 Android API 28–32 shield blocked by Q-31, storage layout in T-02 / T-09; checklist 9/9 PASS on pass 2).
  - Created `docs/security/exceptions.md` with EX-001 (iOS widget snapshot, approved by Ton 2026-11-21) and the Android equivalent as an open point (Q-42). From now on the file belongs to backend-lead.
  - **Still open (34):** new Q-39 to Q-46, plus Q-01–03, 05–09, 15, 19, 20, 22–29, 31–36, 38. Answers that conflict with the security standard became questions, not decisions: Q-40 (category name in notification copy), Q-39 (backup key recovery), Q-46 (Apple web OAuth needs a server).
  - Status stays **PLAN_READY** for foundation. The revision keeps it buildable, because the only blocked task (T-22) is a Should.
- 2026-11-21 [ba]: **Ton's second-round answers recorded** (relayed by the main session): decisions file Part 3 (A1 payday cycle, A2 card due date, Q-48, Q-15, Q-47, Q-49, Q-50, findings 13–15). Master plan revision 4 (checklist 9/9 PASS on pass 2; pass 1: a golden row first showed 87% instead of 85%, and card days 29–31 became Q-53 instead of an assumption). Foundation plan revision 4 (9/9 PASS on pass 1). New drafts: `docs/plan/golden-sample-data.md`, `docs/plan/glossary.md`. New questions Q-51–Q-53. Foundation stays **PLAN_READY**.
- 2026-11-21 [ba]: **Re-plan after the v5.1 UX/UI audit fix pass** (CLAUDE.md "v5.1 — UX/UI audit fix pass", `docs/design/ux-audit-v5.1-2026-11-21.md`, `tokens-changelog.md`).
  - Master plan revision 3: §5 rules 3–4 (income-text, contrast, destructive-on-raised, hit areas) and new rules 10–12 (payday cycle, card due-date rule, platform-named copy); E03 / E04 / E05 / E10 / E11 / E13 / E18 / E19 / E23 updated; new E10-T13 card due-date domain task; §6.1 screen map delta; DG-34 closed; DG-47–DG-50 new; §7.1 deferred findings 13–15; Q-15 narrowed; Q-47–Q-50 new. Checklist 9/9 PASS on pass 2 (pass 1: the Figma ÷ 6 per-day figures failed check 6; the days-left count failed check 8 and became Q-48).
  - Foundation plan revision 3: T-01 (token pipeline + 21 Nov token values, AC-01a / AC-01b), T-02 (`cycleStartDay` = payday), AC-37a, AC-43a, AC-44a, AC-51a, AC-51b. Checklist 9/9 PASS on pass 1. No task added; status stays **PLAN_READY**.
  - Payday = cycle and the card due-date rule are recorded only in CLAUDE.md; recommend copying them into `docs/decisions/`.
  - Read-only Figma check (same day): `448:5106` is "Know every bill before it lands";
- 2026-11-21 [ba]: **Ton's third-round answers recorded** (decisions file Part 4: Q-51, Q-52, Q-53, naming locks, Thai labels). Golden sheet revision 2, glossary revision 2, master plan revision 5 (checklist 9/9 PASS on pass 2; pass 1: E11 Mark paid AC double-counted a ring-fenced bill → Q-56; 25 Nov figure assumed all fixed-cost kinds → ‡ + Q-55), foundation plan revision 5 (new T-23 `DayClamp`, T-24 cycle label, T-16 `committedUnpaid`; checklist 9/9 PASS on pass 2; pass 1: T-17 did not depend on T-23 / T-24). Days left on 18 Nov = 7 (golden "today" 18 Nov), matching Ton's example. New Q-54–Q-58, DG-53–DG-55. Read-only Figma check: H1 `448:6722`, 4A `448:6926`, 8A `448:14381`. None of the new questions blocks foundation; foundation stays **PLAN_READY**. `448:30549` is "Sync & devices (V2.0 — not in V1.0)" with only iPhone and iPad devices; H1 `448:6722` shows "6 days left" and "฿1,075/day" (DG-48 confirmed); 9J `448:15814` still has "KBank Credit · 25 Nov" and a third per-day figure "฿586/day × 11 days", added to Q-47.
- 2026-11-21 [ba]: **Ton's fourth-round answers recorded** (decisions file Part 5: Q-54, Q-55, Q-56, Q-57, Q-58; Q-21 marked superseded on the Left to spend wording). `caffeine-domain` updated with Ton's approval (`.claude/skills/` and the `.agents/skills/` mirror). Golden sheet revision 3 (‡ removed: Dec cycle ฿25,553 · ฿851/day; new rows Mark paid ฿500 → ฿5,950, Overdue 23 Nov ฿2,925/day, Skip → ฿6,450, negative −฿399 → ฿0/day), glossary revision 3 (Fixed costs UI / Commitments internal, Set aside, Overdue, Skip this cycle), master plan revision 6 (+2 tasks E03-T15, E11-T20; DG-56; Q-59–Q-62; checklist 9/9 PASS on pass 2: pass 1 failed check 6 on the E18-T01 "bills" wording and check 8 on merging "฿0/day" with the helper text), foundation plan revision 6 (T-16 `billsExceedBy`, T-18 max(0, …), AC-43c, AC-46b, AC-51d, AC-54a; 9/9 PASS on pass 1). Foundation stays **PLAN_READY**. Downstream: local-data-engineer's dry-run comment "Left to spend (budget - spent)" in `docs/data-model/sql/dryrun/ledger-draft-queries.sql` is stale (owner: local-data-engineer).
- 2026-11-21 [ba]: **Ton's fifth-round answers recorded** (decisions file Part 6: Q-59 alert colour = `night/accent` confirmed, Q-60 overdue fixed costs carried into the next cycle's set-aside, Q-61 deficit caption = abs(Left to spend) (State A "Bills exceed budget by ฿399", State B "Over budget by ฿1,799"), Q-62 Thai UI label for Fixed costs = รายการประจำ). `caffeine-domain` updated with Ton's approval (`night/income-text` for income amount text, plus the Q-59 to Q-61 rules and worked examples; `.claude/skills/` and the `.agents/skills/` mirror kept identical). **Unblocked: E11-T19, E11-T20 (Q-60) and E03-T04 (Q-61).** Golden sheet revision 4 (carry-forward rows 25 / 26 Nov: ฿24,954 · ฿831/day, Skip ฿25,553 · ฿851/day, Mark paid ฿24,954 · ฿860/day, back-dated ฿25,553 · ฿881/day; State B −฿1,799 / −฿1,200), glossary revision 4, master plan revision 7 (no task added; DG-56 items 5–6; 33 open questions; checklist 9/9 PASS on pass 2: pass 1 failed check 6 on a double-rounded % and check 2 on an E03 AC that did not state the set-aside), foundation plan revision 7 (T-16 `overBy` = −leftToSpend, AC-46b amended, new AC-46c / AC-51e; 9/9 PASS on pass 1). Read-only Figma check: 1K `448:6790` shows "฿0" and "OVER BUDGET BY ฿1,200" (DG-56 (5)). Foundation stays **PLAN_READY**.
- 2026-11-21 [ux-ui-designer] (foundation): **DESIGN_READY.** Plan review: no blocker (no PLAN_RETURNED); non-blocking items in `docs/design/foundation-spec.md` §0/§6 and the designer report. Built: v5.1 section N `620:37505` (F1 Splash `620:37506`/`620:37602`, F2 Store error `620:37527`/`620:37611`, F3 Retrying `620:37561`/`620:37625`, F4 Privacy shield `620:37593`/`620:37639`); DG-23 confirmed scaffold only; journey 01 splash step `625:26698`; App Prototype flow 01 starts on the splash `625:44449`. DG-52: Stat tile + Wallet card (legacy) labels → `on-primary-soft` (DS page only, no Home v5 pins). T-01 token pipeline `scripts/tokens/`: AC-01, AC-01a, AC-01b, AC-02 (diff = 0, plus a fresh Figma re-read), AC-03 (negative run) PASS; iOS build PASS; Android compile PASS only with the cached Gradle and `-Pandroid.useAndroidX=true` (T-04 must add the wrapper and `gradle.properties`). A11y: all checks PASS (`docs/design/foundation-a11y.md`). Design gate attempt 1/3 (two fixes inside the loop). Spec: `docs/design/foundation-spec.md`. Inventory refreshed (`448:5106` = "Know every bill before it lands"). Next for ux-ui-designer: DG-48 / DG-56 heroes, DG-05, DG-39, DG-40, DG-41, DG-12/13, DG-42/43, DG-11, DG-46, DG-51, DG-53–55, DG-47, DG-49.
- 2026-11-21 [main] (foundation): Ton answered the four foundation design questions (`docs/decisions/2026-11-21-ton-answers.md` Part 7): D-1 app icon not chosen yet (leave it); D-2 keep `night/hero*` + `Caffeine / Bento` as deprecated until zero frames reference them, then delete (owner ux-ui-designer); D-3 store error copy approved; D-4 solid privacy shield approved. GATE 1 (design approved) still waits for backend-lead CONTRACT_READY.

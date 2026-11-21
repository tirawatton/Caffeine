# Pipeline Status (role team)

current_feature: foundation
platform_scope: both
mode: team
status: PLAN_READY

## What next (read this first)
- **Stage (2026-11-21):** the whole-app backlog exists: `docs/plan/caffeine-app-master-plan.md` (revision 4, after Ton's second-round answers: 29 epics E00–E28, 267 tasks, release roadmap from Ton, build order, 52 design gaps, 36 open questions). The first feature plan is `docs/plan/foundation-plan.md` (E00, revision 4, PLAN_READY). Handoff drafts: `docs/plan/golden-sample-data.md`, `docs/plan/glossary.md` (Thai column: draft, Ton to review). Code is still scaffold only in `ios-app/` and `android-app/`.
- **Foundation revisions 3–4 for the agents now in stage 2:**
  - ux-ui-designer T-01: build the token pipeline with `night/income-text` and the 21 Nov token values (AC-01a, AC-01b), after DG-52 puts the Home v5 values into the global variables.
  - backend-lead T-02: `AppSettings` now has 9 fields: `cycleStartDay` 1–31 (the payday) + `cycleStartIsLastDay`. Add case rows for AC-19, AC-37a, AC-38–AC-38e (clamping), AC-43a, AC-44a, AC-51a, AC-51b, using the golden sheet.
  - Home reads "7 days left · ฿921/day" on 18 Nov (Ton Q-16 / Q-48), **not** Figma's "6 days left · ฿1,075".
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
  - Q-52 period labels under a payday cycle: do History, Analytics and the month pill follow the cycle or the calendar month (blocks home-dashboard, history, analytics)
  - Q-53 card cut-off / due days 29–31: clamp like payday?
  - Q-51 forecast line totals (V1.1): ฿6,450 vs ฿6,447; a bank-paid bill counted twice or once
  - Review the drafts: golden sample-data sheet and glossary (Thai column; G-7 Debts vs Liabilities; G-8 Analytics vs Reports)
  - (Answered 21 Nov, decisions file Part 3: Q-15, Q-47, Q-48, Q-49, Q-50, findings 13–15; A1 / A2 copied in.)
- **ux-ui-designer, please design before runs 2–5, 8 and 13:**
  - DG-05 Add Account sheet (spec in the decisions file)
  - DG-40 + long-press context menu
  - DG-39 Dashboard empty-state "Add Account"
  - DG-41 Sign in with Google
  - DG-12 / DG-13 Duplicate / Edit
  - DG-42 Mark paid sheet, DG-43 Link-to-bill prompt
  - DG-11 Add subscription
  - DG-46: fix the App Prototype + tap link
  - DG-48: heroes "7 days left · ฿921/day" (1I "30 days left · ฿1,333/day"); 9J / 9K "Balance on 24 Nov", "฿921/day × 7 days", no card line in the horizon; 1B status vs data
  - DG-51: re-sync frames to `golden-sample-data.md` and `glossary.md` · DG-52: Home v5 DS values into the global variables / components (no pins on Home v5)
  - DG-47: onboarding page 3 motion · DG-49: Android copy for "iPhone" / "iCloud" / "Excel and Numbers" strings · DG-50 closed (native status bar note in every spec)
  - Refresh `docs/design/figma-inventory-v5.1.md` (still names `448:5106` "One wallet for the whole home")
  - Full list in master plan §7 (deferred audit findings 13–15 in §7.1).

## Status values (set by agents unless marked HUMAN)
- IDLE: no feature in progress
- PLAN_READY: `ba` done; `ux-ui-designer` and `backend-lead` next (parallel)
- PLAN_RETURNED: ux-ui-designer or backend-lead sent the plan back to `ba` (Feedback in Notes)
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
  - Read-only Figma check (same day): `448:5106` is "Know every bill before it lands"; `448:30549` is "Sync & devices (V2.0 — not in V1.0)" with only iPhone and iPad devices; H1 `448:6722` shows "6 days left" and "฿1,075/day" (DG-48 confirmed); 9J `448:15814` still has "KBank Credit · 25 Nov" and a third per-day figure "฿586/day × 11 days", added to Q-47.

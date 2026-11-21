# Pipeline Status (role team)

current_feature: foundation
platform_scope: both
mode: team
status: PLAN_READY

## What next (read this first)
- **Stage (2026-11-21):** the whole-app backlog exists: `docs/plan/caffeine-app-master-plan.md` (revision 2: 29 epics E00–E28, 266 tasks, release roadmap from Ton, build order, 46 design gaps, 34 open questions). The first feature plan is `docs/plan/foundation-plan.md` (E00, PLAN_READY). Code is still scaffold only in `ios-app/` and `android-app/`.
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
  - Q-15 days 29–31 (cycle and card cut-off / due)
- **ux-ui-designer, please design before runs 2–5, 8 and 13:**
  - DG-05 Add Account sheet (spec in the decisions file)
  - DG-40 + long-press context menu
  - DG-39 Dashboard empty-state "Add Account"
  - DG-41 Sign in with Google
  - DG-12 / DG-13 Duplicate / Edit
  - DG-42 Mark paid sheet, DG-43 Link-to-bill prompt
  - DG-11 Add subscription
  - DG-46: fix the App Prototype + tap link
  - Full list in master plan §7.

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

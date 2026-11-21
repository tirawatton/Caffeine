# Pipeline Status (role team)

current_feature: none
platform_scope: none
mode: team
status: IDLE

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

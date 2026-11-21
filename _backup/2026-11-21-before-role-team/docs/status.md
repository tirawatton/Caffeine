# Pipeline Status (Team Mode)

current_feature: none
platform_scope: none
status: IDLE

## Status values (set by agents unless marked HUMAN)
- IDLE: no feature in progress
- PLAN_DRAFTED: product-planner done, plan-validator next
- PLAN_READY: plan validated; data-architect and design-spec-extractor next (parallel)
- DATA_MODEL_READY / DESIGN_SPEC_DRAFTED: recorded in Notes; design-governor runs when both are set
- DESIGN_VALIDATED: governor passed; token-sync-engineer next
- DESIGN_READY: tokens in sync; waiting for Ton to review the spec and Figma
- DESIGN_APPROVED: **HUMAN** (Ton says "design approved"); iOS and/or Android lanes next
- DEV_COMPLETE: every in-scope lane is *_REVIEW_DONE; qa-parity-tester next
- QA_PASSED: parity tests green; release-engineer next
- RELEASED_TO_BETA: TestFlight / Play internal uploaded; production only on Ton's explicit confirmation
- BLOCKED: see Notes for the owner and platform

Lane state lives in `docs/pipeline/ios-status.md` and `docs/pipeline/android-status.md`.
Retry budget: 3 attempts per gate (see `.claude/skills/loop-engineering/SKILL.md`).

## Paused features

## Notes
(agents append dated notes: gate results, attempt counters `<gate> attempt n/3`, BLOCKED owner + platform)

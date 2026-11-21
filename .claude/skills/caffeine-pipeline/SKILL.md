---
name: caffeine-pipeline
description: Conductor for the Caffeine Team Mode pipeline. Run in the main session as /caffeine-pipeline <feature> [ios|android|both]. Reads docs/status.md, starts the next agent(s) with the Agent tool, checks their output, enforces gates and the 3-attempt budget, stops at the two human gates (design approval, production release). Use when Ton asks to run, continue or resume the pipeline for a feature.
argument-hint: <feature> [ios|android|both] [resume]
---

# Caffeine Pipeline (conductor)

Subagents cannot start other subagents, so **this skill runs in the main session** and is the only place agents are started from. Agents talk to each other only through files.

## Before anything
1. Read `docs/status.md`, `docs/lessons.md`, and `.claude/skills/loop-engineering/SKILL.md`.
2. If another feature is active, ask Ton: queue, pause it (move it to "Paused features"), or stop. Never overwrite silently.
3. If `docs/briefs/<feature>-brief.md` is missing, copy `docs/briefs/TEMPLATE-brief.md`, ask Ton the template questions (max 3 at once), and write the brief.
4. Show Ton the stage plan and the platform scope before starting a new feature (Set Goal step of the loop).

## Stages and status values (`docs/status.md`)
| # | Status before | Start (Agent tool, subagent_type) | Status after | Gate |
|---|---|---|---|---|
| 1 | IDLE | `product-planner` | PLAN_DRAFTED | — |
| 2 | PLAN_DRAFTED | `plan-validator` | PLAN_READY | FAIL → back to `product-planner` |
| 3 | PLAN_READY | `data-architect` **and** `design-spec-extractor` in parallel (one message, two Agent calls) | DATA_MODEL_READY + DESIGN_SPEC_DRAFTED | — |
| 4 | both above | `design-governor` (+ `analytics-engineer` in parallel if the brief has a KPI) | DESIGN_VALIDATED | FAIL → back to `design-spec-extractor` |
| 5 | DESIGN_VALIDATED | `token-sync-engineer` (skip when the token diff is already empty) | DESIGN_READY | diff not empty → re-run |
| — | DESIGN_READY | **HUMAN GATE.** Show Ton the spec, screenshots, gaps and data model summary. Stop. Only Ton's explicit "design approved" sets DESIGN_APPROVED | DESIGN_APPROVED | Ton |
| 6 | DESIGN_APPROVED | Run `/ios-pipeline` and `/android-pipeline` per scope. For Both, start both lanes' first agents in one message so they run in parallel, then keep each lane going as its agents finish | DEV_COMPLETE (when every in-scope lane is `*_REVIEW_DONE`) | lane gates |
| 7 | DEV_COMPLETE | `qa-parity-tester` | QA_PASSED | divergence → BLOCKED naming platform |
| 8 | QA_PASSED | `release-engineer` (beta only) | RELEASED_TO_BETA | lane failure → BLOCKED |
| — | RELEASED_TO_BETA | **HUMAN GATE.** Production only after Ton confirms in chat for this build | — | Ton |

`platform_scope: iOS` or `Android` skips the other lane and QA runs that platform only (parity check noted as N/A).

## Starting an agent
Prompt each agent with: feature name, platform scope, the exact input files it should read, the status it must set, and "attempt n/3" when it is a retry with the Feedback list (criterion · where · what is wrong · what is right). Run agents in the foreground unless running two in parallel.

## After each agent
1. Read the status it set and the file it wrote; do not trust the agent's summary alone.
2. Gate FAIL → increment the attempt counter in `docs/status.md` Notes, send the Feedback to the responsible agent, then re-run every gate from there forward.
3. Third failure of the same gate → stop, report to Ton with the three failure reasons and options.
4. Any ambiguous requirement → ask Ton (standing rule), do not guess.

## Resume mode (`/caffeine-pipeline <feature> resume`)
Read status and Notes, find the first unmet stage or the BLOCKED owner, and continue from there with the same rules. For a BLOCKED from QA or release, ask Ton which lane resumes, then run that lane's skill in resume mode.

## Report at each stop
One short block: stage reached, files written, gate results with evidence (test counts, lint, diff), open questions, next step.

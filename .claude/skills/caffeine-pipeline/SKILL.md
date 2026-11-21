---
name: caffeine-pipeline
description: Conductor for the Caffeine role team. Run in the main session as /caffeine-pipeline <feature> [ios|android|both] [--solo] [resume]. Reads docs/status.md, starts the next role agent(s) (ba, ux-ui-designer, local-data-engineer, backend-lead, ios-developer, android-developer, qa-engineer) with the Agent tool, routes Feedback to the owner, enforces the 3-attempt budget, and stops at Ton's two gates (design approval, production release). Use when Ton asks to start, continue or resume a feature.
argument-hint: <feature> [ios|android|both] [--solo] [resume]
---

# Caffeine Pipeline (conductor)

Subagents cannot start other subagents, so **this skill runs in the main session** and is the only place agents are started. Agents talk only through files and status values. The conductor never does an agent's work itself — and **never edits Figma**: any Figma change goes to `ux-ui-designer` as Feedback.

## The team
| Role | Agent | One responsibility |
|---|---|---|
| Product Owner & CEO | **Ton** (human) | Brief, design approval, production release, open questions |
| BA | `ba` | The plan (tasks, ACs, screen map, analytics) |
| UX/UI | `ux-ui-designer` | Figma (only writer) + spec + accessibility + tokens |
| Backend Engineer, Team Lead | `backend-lead` | Contract before build; review + beta after QA; `backend/` in Phase 2 |
| Local Data Engineer (backend team) | `local-data-engineer` | On-device tables + queries (SwiftData / Room), proven on the golden data; personal statements tie-out |
| iOS | `ios-developer` | The iOS app |
| Android | `android-developer` | The Android app |
| QA | `qa-engineer` | Independent verification of both apps |

## Before anything
1. Read `docs/status.md`, `docs/lessons.md`, `.claude/skills/loop-engineering/SKILL.md`.
2. Another feature active → ask Ton: queue, pause (move to "Paused features") or stop. Never overwrite silently.
3. `docs/briefs/<feature>-brief.md` missing → copy `TEMPLATE-brief.md`, ask Ton the template questions (max 3 at once), write the brief.
4. **Set Goal**: show Ton the stages and the platform scope before starting a new feature.

## Stages (`docs/status.md`)
| # | Status before | Start (Agent tool, subagent_type) | Status after | Ton |
|---|---|---|---|---|
| 1 | IDLE / PLAN_RETURNED | `ba` | PLAN_READY | answers open questions |
| 2 | PLAN_READY | `ux-ui-designer` **and** `local-data-engineer` — one message, two Agent calls | Notes: DESIGN_READY, DATA_DESIGN_READY | — |
| 2b | Note DATA_DESIGN_READY (designer may still be running) | `backend-lead` (Phase A) | Note: CONTRACT_READY | — |
| — | both READY | **GATE 1.** Show Ton: spec + Dark/Light screenshots, a11y result, gaps, Figma changes, contract summary (tables, queries and the verify script result). Stop. Only Ton's explicit "design approved" sets DESIGN_APPROVED | DESIGN_APPROVED | **approves** |
| 3 | DESIGN_APPROVED | `ios-developer` ∥ `android-developer` per scope (one message). `backend-lead` Phase C too if the plan has a sync/API task | `IOS_DONE` / `ANDROID_DONE` in the lane files (+ Note `BACKEND_DONE` when Phase C ran) → set DEV_COMPLETE. A lane at `IOS_BLOCKED` / `ANDROID_BLOCKED` after 3 passes → report to Ton | — |
| 4 | DEV_COMPLETE | `qa-engineer` | QA_PASSED | — |
| 5 | QA_PASSED | `backend-lead` (Phase B: review, then beta) | REVIEW_PASSED → RELEASED_TO_BETA | — |
| — | RELEASED_TO_BETA | **GATE 2.** Production only after Ton confirms in chat for this exact build | — | **releases** |

Scope `ios` or `android` skips the other developer; QA marks parity N/A.

## Solo mode (`--solo`, one platform, Ton working alone)
`ba` (same checklist) → `ux-ui-designer` only if the plan lists Design gaps → Ton approves → one developer → Ton reviews the developer's report. Skips local-data-engineer and backend-lead Phase A (the developer follows the existing model and `caffeine-domain`; a new entity, a new query on a money total, or a migration ends solo mode and runs `local-data-engineer` → Phase A), QA and beta. Switch to the full team when a second person joins, features ship faster than Ton can review, or an iOS/Android difference reaches a user.

## Feedback routing (who fixes what)
| Found by | Problem | Status set | Goes to | Then re-run |
|---|---|---|---|---|
| ux-ui-designer / local-data-engineer / backend-lead | Plan can't be designed or modelled | PLAN_RETURNED | `ba` | stage 1 → 2 |
| backend-lead (A) | Table, index or query wrong; verify script fails | Note DATA_RETURNED | `local-data-engineer` | 2 → 2b |
| developer | Missing state, wrong copy, unbuildable layout | DESIGN_RETURNED | `ux-ui-designer` | GATE 1 if Figma changed, then that developer |
| developer | Contract missing or contradicts plan | CONTRACT_RETURNED | `backend-lead` (A); a missing query → DATA_RETURNED to `local-data-engineer` first | that developer |
| qa-engineer | Build/test/lint/coverage/id on one platform | BLOCKED (owner) | that developer | QA → lead |
| qa-engineer | Spec/Figma wrong | BLOCKED (owner ux-ui-designer) | `ux-ui-designer` | GATE 1, developer(s), QA |
| qa-engineer | Platforms differ, both match contract | BLOCKED (owner backend-lead) | `backend-lead` (A); a query or reduce-step cause → `local-data-engineer` | developers, QA |
| backend-lead (B) | CRITICAL/HIGH finding | BLOCKED (owner) | that developer | QA → lead |

## Starting an agent
Prompt: feature name, platform scope, the exact input files, the status it must set, and on a retry "attempt n/3" plus the Feedback list (criterion · where · what is wrong · what is right). Foreground unless two run in parallel.

## After each agent
1. Read the status it set and the file it wrote; never trust the summary alone.
2. Gate failure → increment `<gate> attempt n/3` in Notes, route by the table above, re-run every gate from the fixed stage forward.
3. Third failure of the same gate → stop, report to Ton with the three reasons and options.
4. Ambiguous requirement → ask Ton (standing rule).

## Resume (`/caffeine-pipeline <feature> resume`)
Read status and Notes, find the first unmet stage or the BLOCKED owner, continue with the same rules.

## Report at each stop
One short block: stage reached, files written, gate results with evidence, open questions, next step.

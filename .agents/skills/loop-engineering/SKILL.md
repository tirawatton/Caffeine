---
name: loop-engineering
description: How every Caffeine agent and pipeline runs as a closed loop - objective gates, the 3-attempt retry budget, re-running gates forward after a fix, and writing lessons to docs/lessons.md. Read by every gate agent and by the pipeline skills. Use whenever an agent sets FAIL/BLOCKED, or when adding a new stage.
---

# Loop Engineering

Every stage is the same loop as the design loop in `AGENTS.md`:

```
Start -> Set Goal -> Reason -> Verify -> Pass? --YES--> Exit (hand off)
                       ^                  |
                       |                  NO
                       +----- Fix <--- Feedback
```

## 1. Objective gate first, judgment second

A gate fails if any mechanical check fails. No reasoning can override a red build, a failing test, a lint error or a missing required field. Only when every mechanical check passes does judgment apply.

| Agent | Mechanical check inside its own loop (cannot be argued with) | Judgment on top |
|---|---|---|
| `ba` | Every task has all 8 fields; every AC is Given/When/Then with concrete values; every flow branch covered; no cycles | Is the task atomic enough |
| `ux-ui-designer` | Every interactive element has a label and id; every text/background pair meets 4.5:1 (3:1 large text and icons) in Dark and Light; hit targets >= 44pt / 48dp; token diff = 0 | Is the copy clear, does it look right |
| `backend-lead` (contract) | Every plan entity modelled; every calculation AC has a case row; migration path defined | Naming, sync shape |
| `ios-developer` / `android-developer` | Build, unit tests and lint exit 0; every AC maps to a passing test | Which warnings are debt |
| `qa-engineer` | Same battery re-run independently; every `-cases.md` row equal on both platforms; same Appium test passes on both; screenshots match the spec | Whether a difference is a real divergence |
| `backend-lead` (review + beta) | Grep: no `!` / `try!` / `!!` in production code; no `Double`/`Float` money; no persistence imports in UI; fastlane `test` + `beta` exit 0 | Severity calls |

**Builder ≠ verifier.** Each agent verifies its own work (Level 1), and the next gate re-verifies independently: developers are checked by QA, QA-passed code is reviewed by the lead. No agent grades its own work as the final gate.

## 2. Retry budget: 3 attempts per gate

- A gate failing and sending work back is one attempt. **Maximum 3 attempts per gate, per feature, per platform.**
- After the 3rd failure of the same gate, stop and report to Ton: which gate, what failed each time, what you think is wrong (usually the requirement, the design or the architecture, not the code).
- Record the counter in `docs/status.md` Notes: `attempt 2/3 on QA (ios) — <reason>`.

## 3. Re-run gates forward, not just the one that failed

After a fix, re-run every gate from the fixed layer onward. A lead review finding fixed by a developer goes back through QA, then the lead. A persistence fix can break a UI test that already passed.

## 4. Three loop levels

- **Level 1, inside one agent.** Every role agent runs Set Goal → Reason → Verify → Fix on its own output (max 3 passes) before it sets a status: BA readiness checklist, designer criteria + a11y + token diff, contract criteria, developer TDD + battery, QA matrix.
- **Level 2, the conductor re-running a gate chain.** `/caffeine-pipeline` routes Feedback to the owner (routing table in that skill) and re-runs every gate forward, within the retry budget.
- **Level 3, human.** Third failure of one gate, a contract ambiguity, or a design change that alters the product → Ton decides.

## 5. Lessons are written at the moment of failure

The agent that finds the problem appends one line to `docs/lessons.md` **before** setting FAIL/BLOCKED:

```
- YYYY-MM-DD [agent-name] (feature): what went wrong -> rule that would have prevented it
```

Every agent reads `docs/lessons.md` before working. A lesson repeated across 3 features gets folded into the relevant SKILL.md and removed from the lessons file.

## 6. Parallel work and ownership

Parallel pairs never share files: `ux-ui-designer` (Figma, `docs/design/`, generated token files) ∥ `backend-lead` (`docs/data-model/`); `ios-developer` (`ios-app/`) ∥ `android-developer` (`android-app/`). QA owns `qa-automation/` and the `QA` test folders. If a collision happens anyway, run each parallel agent with `isolation: "worktree"` and merge after both finish.

## 7. Honest verification

If a tool is missing (no Xcode, no Gradle, no emulator, no Appium server), say so in the status file ("Tier 2 unverified: no emulator") and do not report the gate as passed.

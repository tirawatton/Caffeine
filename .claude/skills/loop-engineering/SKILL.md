---
name: loop-engineering
description: How every Caffeine agent and pipeline runs as a closed loop - objective gates, the 3-attempt retry budget, re-running gates forward after a fix, and writing lessons to docs/lessons.md. Read by every gate agent and by the pipeline skills. Use whenever an agent sets FAIL/BLOCKED, or when adding a new stage.
---

# Loop Engineering

Every stage is the same loop as the design loop in `CLAUDE.md`:

```
Start -> Set Goal -> Reason -> Verify -> Pass? --YES--> Exit (hand off)
                       ^                  |
                       |                  NO
                       +----- Fix <--- Feedback
```

## 1. Objective gate first, judgment second

A gate fails if any mechanical check fails. No reasoning can override a red build, a failing test, a lint error or a missing required field. Only when every mechanical check passes does judgment apply.

| Gate agent | Mechanical check (cannot be argued with) | Judgment on top |
|---|---|---|
| `plan-validator` | Every task has all 7 required fields; every criterion is Given/When/Then | Is the task atomic enough |
| `design-governor` | Every interactive element in the spec has an accessibility label and id; every text/background pair in the spec meets 4.5:1 (3:1 for large text and icons) in Dark and Light; hit targets >= 44pt / 48dp | Is the copy clear |
| `token-sync-engineer` | Token diff between Figma variables and both platforms' token files is empty | — |
| `ios-verifier` / `android-verifier` | Build, unit tests and lint exit 0; every acceptance criterion maps to a passing test | Which warnings are debt |
| `ios-reviewer` / `android-reviewer` | Grep: no `!` force unwrap / `try!` / `!!` in production code; no `Double`/`Float` money fields; no persistence imports in Views/Stores | Severity calls |
| `qa-parity-tester` | Same Appium test passes on both platforms | Whether a difference is a real divergence |
| `release-engineer` | fastlane `test` then `beta` exit 0 | — |

## 2. Retry budget: 3 attempts per gate

- A gate failing and sending work back is one attempt. **Maximum 3 attempts per gate, per feature, per platform.**
- After the 3rd failure of the same gate, stop and report to Ton: which gate, what failed each time, what you think is wrong (usually the requirement, the design or the architecture, not the code).
- Record the counter in the lane's status file Notes: `attempt 2/3 on IOS_VERIFY — <reason>`.

## 3. Re-run gates forward, not just the one that failed

After a fix, re-run every gate from the fixed layer onward. A reviewer finding fixed in the UI layer goes back through the verifier, then the reviewer. A persistence fix can break a UI test that already passed.

## 4. Three loop levels

- **Level 1, inside one agent.** TDD red → green → refactor (engineers), atomicity checklist (planner), own checklist pass (spec extractor). Never touches a status file.
- **Level 2, the pipeline skill re-running a gate chain.** Run automatically by `/ios-pipeline`, `/android-pipeline`, `/caffeine-pipeline` within the retry budget.
- **Level 3, across lanes, human-chosen.** When `qa-parity-tester` finds a divergence or `release-engineer` fails, status becomes `BLOCKED` naming the platform. Ton decides which lane resumes; the lane then runs in Resume mode (Level 2 rules).

## 5. Lessons are written at the moment of failure

The agent that finds the problem appends one line to `docs/lessons.md` **before** setting FAIL/BLOCKED:

```
- YYYY-MM-DD [agent-name] (feature): what went wrong -> rule that would have prevented it
```

Every agent reads `docs/lessons.md` before working. A lesson repeated across 3 features gets folded into the relevant SKILL.md and removed from the lessons file.

## 6. Parallel lanes and worktrees

The iOS and Android lanes write to different folders (`ios-app/`, `android-app/`) and different status files, so they can run at the same time. Inside a lane, data and UI engineers own different folders (see the lane skill). If collisions happen anyway, run each parallel agent with `isolation: "worktree"` and merge after both finish.

## 7. Honest verification

If a tool is missing (no Xcode, no Gradle, no emulator, no Appium server), say so in the status file ("Tier 2 unverified: no emulator") and do not report the gate as passed.

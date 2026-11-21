---
name: ios-pipeline
description: Runs the Caffeine iOS lane in the main session as /ios-pipeline <feature> [resume] - ios-architect, then ios-data-engineer and ios-ui-engineer in parallel, then ios-verifier and ios-reviewer, with the 3-attempt gate loop. Requires docs/status.md DESIGN_APPROVED. Called by caffeine-pipeline or directly by Ton.
argument-hint: <feature> [resume]
---

# iOS Lane

State file: `docs/pipeline/ios-status.md` (lane status, attempt counters, AC coverage, artefact paths).

## Preconditions
`docs/status.md` is DESIGN_APPROVED and scope includes iOS. Otherwise stop and report.

## Sequence
| Step | Agent | Waits for | Sets | Owns |
|---|---|---|---|---|
| 1 | `ios-architect` | IOS_IDLE | IOS_ARCH_DONE | `docs/pipeline/ios-arch-<feature>.md` |
| 2a | `ios-data-engineer` (parallel) | IOS_ARCH_DONE | IOS_DATA_DONE | `ios-app/Sources/Models/`, `Sources/Repositories/`, their tests |
| 2b | `ios-ui-engineer` (parallel) | IOS_ARCH_DONE | IOS_UI_DONE | `ios-app/Sources/Features/<Feature>/`, `Sources/Shared/Components/`, Store tests |
| 3 | `ios-verifier` | IOS_DATA_DONE and IOS_UI_DONE | IOS_VERIFIED | test gap-fill only |
| 4 | `ios-reviewer` | IOS_VERIFIED | IOS_REVIEW_DONE | `docs/review/<feature>-ios-review.md` |

Start 2a and 2b in the same message. The UI engineer codes against the repository protocols the architect defined and uses mock repositories until the data layer lands; it must not edit data-layer folders.

## Gate loop
- Verifier or reviewer sets IOS_BLOCKED with an owner (`ios-data-engineer` or `ios-ui-engineer`): send the owner the findings, then re-run verifier → reviewer. Count attempts per gate; stop at 3/3 and report to Ton.
- Architect sets IOS_BLOCKED (spec or model insufficient): stop the lane and report; this goes back to the design or data stage.

## Finish
On IOS_REVIEW_DONE, write `docs/pipeline/ios-feedback-<feature>.md` yourself: what was built per layer, tests and AC coverage N/N, lint debt, review findings left as debt, app artefact path for QA. If the Android lane is also done (or out of scope), set `docs/status.md` to DEV_COMPLETE.

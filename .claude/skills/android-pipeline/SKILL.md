---
name: android-pipeline
description: Runs the Caffeine Android lane in the main session as /android-pipeline <feature> [resume] - android-architect, then android-data-engineer and android-ui-engineer in parallel, then android-verifier and android-reviewer, with the 3-attempt gate loop. Requires docs/status.md DESIGN_APPROVED. Called by caffeine-pipeline or directly by Ton.
argument-hint: <feature> [resume]
---

# Android Lane

State file: `docs/pipeline/android-status.md`.

## Preconditions
`docs/status.md` is DESIGN_APPROVED and scope includes Android. Otherwise stop and report.

## Sequence
| Step | Agent | Waits for | Sets | Owns |
|---|---|---|---|---|
| 1 | `android-architect` | ANDROID_IDLE | ANDROID_ARCH_DONE | `docs/pipeline/android-arch-<feature>.md` |
| 2a | `android-data-engineer` (parallel) | ANDROID_ARCH_DONE | ANDROID_DATA_DONE | `.../caffeine/model/`, `repository/`, `data/room/`, schemas, their tests |
| 2b | `android-ui-engineer` (parallel) | ANDROID_ARCH_DONE | ANDROID_UI_DONE | `.../caffeine/features/<feature>/`, `shared/components/`, ViewModel tests |
| 3 | `android-verifier` | ANDROID_DATA_DONE and ANDROID_UI_DONE | ANDROID_VERIFIED | test gap-fill only |
| 4 | `android-reviewer` | ANDROID_VERIFIED | ANDROID_REVIEW_DONE | `docs/review/<feature>-android-review.md` |

Start 2a and 2b in the same message.

## Gate loop
Same as the iOS lane: owner fixes, re-run verifier → reviewer, 3 attempts per gate, then stop and report. Architect BLOCKED stops the lane.

## Finish
On ANDROID_REVIEW_DONE, write `docs/pipeline/android-feedback-<feature>.md` (built per layer, tests and AC coverage, lint debt, findings, APK path). If the iOS lane is also done (or out of scope), set `docs/status.md` to DEV_COMPLETE.

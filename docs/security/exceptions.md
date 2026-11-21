# Security exceptions

Exceptions to `.claude/skills/security-standard/SKILL.md`. Each one needs Ton's written approval. `backend-lead` owns this file (`docs/security/`), keeps it current and checks it in every review. This file was created by `ba` on 2026-11-21 at the main session's request, to record Ton's approval of Q-30.

| ID | Rule it departs from | Exception | Scope and limits | Approved by / date | Source | Review |
|---|---|---|---|---|---|---|
| EX-001 | §5 "Whole local store at rest: SwiftData file under Data Protection `complete`"; §6 "no Confidential data in widgets" | **Widget snapshot (iOS)**: a small JSON file in the App Group shared container, protected with `NSFileProtectionCompleteUntilFirstUserAuthentication`, so Home Screen widgets can read it while the device is locked after first unlock | Holds **only** two values: `SafeToSpendAmount` (left to spend) and `BudgetPercentage`. No account names, no transactions, no Restricted data. Rewritten by the app whenever the data changes. With **Privacy Mode on**, both values are overwritten with `"••••••"`. The main ledger stays in `NSFileProtectionComplete` and is never placed in the App Group. Built in V1.1 (epic E28 widgets) | **Ton, 2026-11-21** | `docs/decisions/2026-11-21-ton-answers.md` Q-30 | Re-check when E28 is planned and at every release review |

## Open points
- **EX-001 Android equivalent (open, owner backend-lead, for Ton):** Android has no file-protection classes like iOS. A Glance widget reads through the app process, and app-private files sit in credential-encrypted storage, which is readable after the first unlock (comparable to `CompleteUntilFirstUserAuthentication`). The main ledger stays on SQLCipher with a hardware-backed Keystore KEK. To decide when E28 is planned:
  - Does the Android widget get a matching snapshot (same two values, the same Privacy Mode overwrite, stored as an encrypted file in credential-encrypted app storage)?
  - Is that covered by EX-001, or does it need its own approval?

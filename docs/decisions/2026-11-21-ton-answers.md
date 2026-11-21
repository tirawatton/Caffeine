# Ton's decisions — 21 Nov 2026

Source: Ton (Product Owner & CEO), answers to the top blockers in `docs/plan/caffeine-app-master-plan.md` §8. Recorded by the main session as given. These are binding. Where they conflict with Figma or earlier plans, these win; the design changes they need go to `ux-ui-designer`.

## Part 1 — Product and logic

### Q-13 · First account
1. **Auto-create a default Cash account** (฿0 starting balance) when onboarding completes, so the user can tap + or scan a slip at once.
2. **Add Account form**: one bottom sheet (design gap for `ux-ui-designer`).
   - Fields: Account Name (e.g. KBank Savings), Account Type (Cash | Bank Account | Credit Card | E-Wallet), Initial Balance, Card Color/Icon, Include in Net Worth toggle (default ON).
   - Credit Card adds: Credit Limit, Statement Cut-off Day (1–31), Payment Due Day (1–31).
   - Entry points: "+ Add Account" on Wallet (Screen 3) and an "Add Account" button in the Dashboard empty state.

### Q-17 · The + button
- **Tap**: opens the Keypad (2A) directly (Screen 2 spec v1.3).
- **Long-press**: opens the quick context menu with direct shortcuts: Scan Slip (camera), Pick Slip from Photos, Add Transfer.
- The App Prototype (tap → 1N) is wrong on this point.

### Q-16 · Rounding
- **Per day left**: remaining days = (cycle end − today) + 1 (today counts; last day divisor = 1). Amount is **floored** to whole baht (฿496.80 → ฿496/day).
- **Budget %**: round half-up to an integer, except 99.1–99.9% shows **99%**; never show 100% until spend actually reaches or exceeds the budget.
- **% vs previous month**: round to an integer; above 999% shows **>999%**.

### Q-11 · Sign in in a local-first V1
- Purpose: establish identity to (1) generate the backup encryption key and bind the private cloud backup container (iCloud / Google Drive), (2) prepare for future multi-device sync and device transfer without losing history, (3) Continue as Guest stays available.
- **iOS**: Sign in with Apple + Continue with Google + Guest.
- **Android**: Continue with Google (primary) + Sign in with Apple (web OAuth, for iOS → Android migration) + Guest.

### Q-14 · Reading Thai e-slips
- Confirmed: Thai e-slip QR (EMVCo / Thai QR Payment) carries only the sending bank code and transaction reference, not amount, time or recipient.
- **V1 pipeline (on-device hybrid)**:
  1. Barcode detection (iOS `VNDetectBarcodesRequest`, Android ML Kit Barcode): verify it is a bank slip; extract sending bank code and transaction reference (used for duplicate-slip prevention).
  2. OCR on the same image at the same time (iOS `VNRecognizeTextRequest`, Android ML Kit Text Recognition): parse Amount, Date/Time, Merchant/Recipient.
  3. Run spike **E08-T00** with sample slips from KBank, SCB, BBL, KTB, Krungsri, TTB to validate extraction accuracy before locking the parser.

### Q-04 · Launch
- Splash < 0.5 s while local storage initialises, then:
  - App Lock OFF → Dashboard.
  - App Lock ON → privacy shield overlay + automatic Face ID / fingerprint prompt.
- Always blur / shield the app-switcher snapshot when the app goes to the background.

### Q-21 · Mark paid
- **Yes, creates an Expense**, through a short confirmation sheet (amount, paying account, payment date). Confirm posts the expense and reduces Left to spend.
- **Dedup**: if a matching expense was already logged or scanned, 2D and 2B detect matching amount/name and ask "Link this transaction to your upcoming Netflix bill?" and link instead of duplicating.

### Q-10 · Release roadmap
- **V1.0 (core MVP)**: Dashboard (Left to spend + quick actions), Add Transaction (keypad, camera/photo e-slip, installments), Wallet (multi-account, card cycle, reconcile), History (search & filter), Fixed Costs & Recurring Income, Core Analytics (Spending, Cash Flow, Net Worth), Settings (Privacy Mode, App Lock, Backup/Export), User Profile (financial baseline + core achievements).
- **V1.1**: Home Screen widgets (Left to spend, Quick Scan) and Month-End Cash Flow Forecast.
- **V1.2**: Financial Goals (ring-fenced savings) and Trip & Party Budget (multi-currency, split engine).
- **V2.0**: Shared Household / Family Space (real-time multi-user sync).

## Part 2 — Security conflicts

### Q-12 · Android backup
- One **Cloud Backup & Restore** interface, provider per platform:
  - iOS: iCloud Drive private container, client-side encrypted snapshots.
  - Android: Google Drive AppData folder (`drive.appdata`), client-side encrypted.
  - Both: export an encrypted local backup file (`.caffeine`).

### Q-18 · Notifications
- **No amounts and no account names** in push or local notifications.
- Approved copy style: "You have a credit card bill due tomorrow. Tap to review details." / "Your Food & Drink spending is nearing its monthly limit. Tap to check status."

### Q-30 · Widgets vs strict file protection
- **Split storage**:
  1. Main ledger: strictest class (iOS `NSFileProtectionComplete`; Android hardware-backed Keystore).
  2. Widget snapshot (App Group shared container): small JSON with only `SafeToSpendAmount` and `BudgetPercentage`, protected with `NSFileProtectionCompleteUntilFirstUserAuthentication`, refreshed when the app updates data.
  3. Privacy Mode on → snapshot values overwritten with "••••••".
- This is a security exception approved by Ton; record it in `docs/security/exceptions.md`.

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

## Part 3 — After the v5.1 UX/UI audit fix pass (21 Nov 2026, second round)

Source: Ton's answers pasted in the main session and relayed to `ba` by the main session on 21 Nov 2026, recorded here by `ba` as given. A1 and A2 were applied by ux-ui-designer in the audit fix pass and are recorded in CLAUDE.md ("v5.1 — UX/UI audit fix pass"); they are copied here so this file stays the one binding record.

### A1 · Budget cycle follows payday (audit finding 11)
- The budget cycle starts on the user's payday (sample: 25th → cycle 25th–24th). Settings shows "Budget & Cycle · ฿40,000 · 25th"; 9A shows "Current cycle: 25 Oct – 24 Nov 2026, set by your payday."

### A2 · Card due date (audit finding 12, Ton's default)
- The **payment due date** drives the due badge, reminders and the forecast. The **statement cut-off date** is only the statement date. Sample: KBank Credit, cut-off 25, due 10, today 18 Nov → "Due in 22 days".

### Q-48 · Days-left badge
- Days left = (cycle end − today) + 1, today included: the same divisor as the Q-16 per-day figure.
- On 18 Nov with payday 25th (cycle ends 24 Nov) the Home hero reads **"7 days left · ฿921/day"**.
- The last day of a cycle reads **"1 day left"**.

### Q-15 · Payday on the 29th–31st
- **Month-end clamping:** a payday of 29, 30 or 31 snaps back to the last valid day of a shorter month (31st → 28 Feb, or 29 Feb in a leap year; 31st → 30 Apr). It never rolls into the 1st of the next month.
- An explicit **"Last day of the month"** option resolves to each month's final day.

### Q-47 · Forecast horizon
- The forecast ends on the **current budget cycle's end date** (24 Nov for payday 25th; 30 Nov for a 1st-of-month cycle). Not rolling 30 days.
- The forecast daily-spending line uses the same divisor as Home (days left including today, to cycle end), so it matches the Home per-day figure. The three figures in Figma (฿1,075 / ฿586 / ฿921) resolve to **฿921**.
- Next-cycle salary is not included. The card payment due 10 Dec falls outside a 24 Nov horizon.

### Q-49 · Status-bar "9:41" in Figma
- Leave the Figma "9:41" as it is. Handoff note: the builds use the native OS status bar (iOS adapts to Light / Dark; Android the same through the system bars). DG-50 is closed as won't-fix (design).

### Q-50 · DS changes showing on the Home v5 page
- Keep them. They become the global standard. No page-level overrides or pins on Home v5. ux-ui-designer makes sure the global variables and components carry these values, so every screen inherits them.

### Audit findings 13–15 · Sample data and naming
- A golden sample-data sheet and a bilingual EN / TH glossary go in the next handoff package.
- Ton's examples for the sheet: ฿52,000 salary on the 25th, ฿40,000 monthly budget, a ฿1,290 / month 0% installment, credit card cut-off and due dates.
- The glossary must distinguish **Total Cash Balance**, **Net Cash Flow**, **Safe to Spend** (UI term "Left to spend") and **Net Worth**.
- Drafts: `docs/plan/golden-sample-data.md`, `docs/plan/glossary.md`.

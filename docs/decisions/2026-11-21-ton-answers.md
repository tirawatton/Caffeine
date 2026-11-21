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
- **Yes, creates an Expense**, through a short confirmation sheet (amount, paying account, payment date). ~~Confirm posts the expense and reduces Left to spend.~~ **Superseded by Q-56 (Part 5, 21 Nov 2026):** Confirm posts the expense and moves the fixed cost from Reserved to Actual; Left to spend changes only by the variance (Scheduled − Actual paid). The confirmation sheet and the dedup rule below still stand.
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

## Part 4 — Period, clamping, forecast maths and naming (21 Nov 2026, third round)

Source: Ton's answers relayed to `ba` by the main session on 21 Nov 2026, recorded by `ba` as given. Applied in `golden-sample-data.md` revision 2, `glossary.md` revision 2, master plan revision 5 and foundation plan revision 5.

### Q-52 · One period: the budget cycle
- Home, Analytics and the **default** period in History follow the **budget cycle**, not the calendar month.
- Label by the closing month with explicit dates, e.g. `NOV CYCLE · 25 OCT – 24 NOV`. Comparisons read "vs prev cycle" (or "vs Oct cycle").
- The calendar month stays available only as a **secondary filter inside History** (tax and calendar lookups).
- Reason: ฿33,550 on Home vs ฿29,350 under the same label elsewhere looks broken; bills paid just after payday (rent) belong to the next cycle.

### Q-53 · Card date clamping
- Card statement cut-off and payment due days on the 29th–31st use the same month-end clamp as payday: `min(targetDay, daysInMonth)`, always snapping **back** to the last valid day (28/29 Feb, 30 Apr).
- **One shared clamping function** for payday, recurring commitments and card cycles.
- Reason: Thai issuers snap back; rolling forward would make users miss due dates.

### Q-51 · Forecast maths (V1.1) and Safe to Spend
- **A:** the forecast's variable-spending line uses the **exact remaining variable budget**, not the floored daily figure × days (no ฿921 × 7 = ฿6,447). The daily figure is floored only as a display pacing guide.
- **B:** **ring-fence upcoming unpaid fixed bills** in the current cycle. One formula shared by Home and Forecast: `Safe to Spend (remaining variable budget) = monthly budget − actual spent − upcoming unpaid fixed bills in this cycle`.
- Golden example: ฿40,000 − ฿33,550 − ฿599 (AIS, due 22 Nov, unpaid) = **฿5,851**, shown as **฿835/day** floored over 7 remaining days. Forecast deducts −฿599 upcoming fixed bills and −฿5,851 remaining variable budget (= ฿6,450 total), so AIS is counted once and the daily pace matches Home exactly (keeps the Q-47 requirement).

### Naming and glossary
- Lock **Debts** (paired with Assets), not Liabilities. Lock **Analytics**, not Reports.
- Thai labels (short, for the Bento cards): Safe to Spend → เงินที่ใช้ได้ · Per day left → ใช้ได้วันละ · Net Cash Flow → กระแสเงินสดสุทธิ · Assets / Debts → ทรัพย์สิน / หนี้สิน · Net Worth → ความมั่งคั่งสุทธิ · Reconcile / Adjust Balance → ปรับยอดให้ตรงบัญชี · Installments → รายการผ่อนชำระ · Commitments → รายการประจำ / บิลล่วงหน้า.

### Consequences recorded by `ba` (not new decisions; open points are questions Q-54 to Q-58 in the master plan)
- `caffeine-domain` still says "Left to spend = budget − sum(expenses in cycle)" and has no cycle label or shared clamp. Q-51 B and Q-52 / Q-53 override it; the skill owner should update it (master plan §5 rules 9, 10, 15).
- Q-21 says Mark paid "reduces Left to spend". With Q-51 B a bill that was ring-fenced is already out of Left to spend, so paying it at the expected amount leaves Left to spend unchanged. Confirmation asked as Q-56. *(Both points resolved in Part 5: Ton answered Q-54 to Q-58 and approved the `caffeine-domain` edit, made the same day.)*

## Part 5 — Fixed costs set aside, Mark paid, negative Left to spend, naming (21 Nov 2026, fourth round)

Source: Ton's answers to Q-54 to Q-58 relayed to `ba` by the main session on 21 Nov 2026, recorded by `ba` as given. Ton also approved the `caffeine-domain` skill edit, which `ba` made the same day (`.claude/skills/caffeine-domain/SKILL.md` and the mirror in `.agents/skills/`). Applied in `golden-sample-data.md` revision 3, `glossary.md` revision 3, master plan revision 6 and foundation plan revision 6.

### Q-55 · Every kind of fixed cost is set aside (unblocks the Dec-cycle figure)
- Bills, subscriptions **and** monthly installments due within the active budget cycle are all set aside from day one of the cycle, whatever the paying account.
- Reason: subscriptions and 0% card installments are 100% committed. Leaving them unreserved inflates Left to spend early and makes it drop on the auto-charge date.
- Left to spend = money genuinely available for discretionary variable spending.
- **Formula (binding, replaces the Q-51 B wording "upcoming unpaid fixed bills"):** `Left to spend = Budget − Actual expenses in the cycle − Upcoming & overdue unpaid fixed costs (bills + subscriptions + installments) due in the active cycle`.
- Golden 25 Nov 2026 (first day of the Dec cycle, nothing spent): 40,000 − 14,447 = **฿25,553**, **฿851/day** over 30 days.

### Q-56 · Mark paid moves Reserved to Actual (supersedes the Q-21 wording)
- Because fixed costs are already set aside, Mark paid moves the entry from **Reserved** to **Actual**: the expense is deducted from the payment account's balance and added to actual Spent. Total budget consumption is unchanged.
- Left to spend changes only by the **variance (Scheduled − Actual paid)**.
- AIS ฿599 scheduled: pay ฿599 → **฿5,851** unchanged; pay ฿650 → −฿51 → **฿5,800**; pay ฿500 → +฿99 → **฿5,950**.
- Q-21 (Part 1) is marked superseded on this point.

### Q-54 · Negative Left to spend
- Show the **exact negative figure** (e.g. −฿399) in alert red.
- Per day left = **max(0, floor(LeftToSpend / RemainingDays))**, so it reads ฿0/day.
- Replace the daily pacing helper text with **"Bills exceed budget by ฿399"**.
- Never mask a deficit as ฿0.
- **Colour (BA recording note, confirm-item Q-59):** Ton wrote "Alert Red (#FF3B30)". Every earlier design decision maps the spec's #FF3B30 to coral (`night/accent`, plus an icon and a label), and the design rules forbid hard-coded colours. Recorded as **alert / accent red = `night/accent` coral, per the established mapping**, until Ton says otherwise. Coral text on the periwinkle Budget hero is about 1.1:1, so the designer must place the negative figure where it passes contrast (DG-56).

### Q-57 · Naming
- **"Fixed costs"** stays the user-facing label on every screen.
- **"Commitments"** is an internal domain / engineering term only (glossary).

### Q-58 · Overdue unpaid fixed costs
- An overdue unpaid fixed cost stays set aside in the current cycle until the user taps **Mark paid** or **Skip this cycle**.
- Its badge becomes **Overdue** (alert red → coral, per the Q-54 colour note); the amount stays deducted from Left to spend.
- Golden 23 Nov 2026, AIS still unpaid: Left to spend ฿5,851, "2 days left", ฿2,925/day, AIS badge "Overdue".

### Consequences recorded by `ba` (open points are questions Q-59 to Q-62 in the master plan)
- Q-59: confirm `night/accent` coral for "alert red" (negative Left to spend, Overdue badge).
- Q-60: an overdue fixed cost still unpaid when the cycle ends: carried into the next cycle's set-aside, or released?
- Q-61: Over budget while fixed costs are still set aside: does the Over budget caption read spent − budget (฿1,200) or include the set-aside (฿1,799)?
- Q-62: Ton's approved Thai label for "Commitments" (รายการประจำ / บิลล่วงหน้า) now names an internal term; is it also the Thai UI label for "Fixed costs"?

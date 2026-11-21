---
name: caffeine-domain
description: Platform-neutral business rules for Caffeine (money, signs and colours, budget and pace maths, cycles, validation, categories, transfers). Both iOS and Android must produce identical results. Read by every role agent.
---

# Caffeine Domain Rules

Both apps must give the same result for the same input. A difference in validation, rounding or calculation between platforms is a blocking bug.

## Money
- Type: `Decimal` (iOS), `BigDecimal` (Android). Never `Double`/`Float`. Always paired with an ISO 4217 code (default `THB`).
- Storage: Room stores money as a `String` via `toPlainString()`; SwiftData stores `Decimal`.
- Rounding: banker's rounding is NOT used; use half-up to 2 decimals (`.plain` on iOS `NSDecimalNumber` behaviour / `RoundingMode.HALF_UP`).
- Display: one shared formatter per platform (`ios-app/Sources/Shared/Formatting/CurrencyFormatter.swift`, `android-app/.../shared/format/CurrencyFormatter.kt`). Whole baht in lists and heroes (`฿6,450`); 2 decimals in detail, edit and slip review (`฿320.00`).
- Every amount is signed: expense `−฿320`, income `+฿52,000`.

## Amount colour rule (from the design rules)
- Expense amounts: coral (`night/accent`). Income: mint (`night/income`). Transfers and card payments: `text-primary`.
- Summary totals (day nets, Net cash flow, History net) are signed and neutral: `text-secondary` for day nets, `text-primary` for headline totals.
- Never rely on colour alone: the sign is always shown.

## Transactions
- Types: `expense`, `income`, `transfer` (transfer includes credit-card payment).
- Amount entered must be > 0; the sign comes from the type.
- Date may be at most 1 day in the future (timezone tolerance).
- Expense and income require a category; transfer requires a from-account and a to-account that differ.
- Transfers and card payments are never counted in In / Out / Net or budgets.

## Budget, cycle and pace (Home Budget hero v5)
Source: Ton's binding decisions in `docs/decisions/2026-11-21-ton-answers.md` (Q-15, Q-16, Q-48, Q-51, Q-52, Q-53, Q-54 to Q-58). Where an older plan or Figma frame disagrees, these rules win.

**Cycle**
- Cycle: monthly, starting on the user's payday (`cycleStartDay` 1–31, or "Last day of the month") and ending the day before the next payday. No payday set = 1st of the month. Month boundaries use the device timezone, not UTC.
- **Shared clamp**: every "day N of the month" rule (payday anchors, recurring fixed costs and recurring income, credit-card statement cut-off and payment due days) uses one function: `clampDay(year, month, N) = min(N, daysInMonth(year, month))`. It always snaps **back** (31 → 28 Feb 2027, 29 Feb 2028, 30 Apr 2027), never rolls into the next month, and the stored N never changes.
- **Cycle label**: a cycle is named after its closing month (the month of its last day) plus its dates: "Nov cycle · 25 Oct – 24 Nov", rendered in Caption Upper as `NOV CYCLE · 25 OCT – 24 NOV`. Home, Analytics and the default History period use it. Comparisons read "vs Oct cycle" (short form "vs prev cycle"). Never label a cycle "Nov" or "Nov 2026" alone, and never compare by calendar month. The calendar month exists only as a secondary History filter.
- Days left = (cycle end − today) + 1, so today counts and the last day reads "1 day left".
- Elapsed = days elapsed / days in cycle (inclusive of today).

**Left to spend (concept name "Safe to Spend")**
- **Left to spend = Budget − Actual expenses in the cycle − Upcoming & overdue unpaid fixed costs (bills + subscriptions + installments) due in the active cycle.** One formula for the Home hero, the widget snapshot and the forecast. Income never raises it.
- Set aside ("Reserved"): every unpaid fixed cost of every kind, whatever the paying account (cash, bank or credit card), whose charge date falls in the active cycle, from the first day of the cycle. A fixed cost due in the next cycle is not set aside.
- Overdue: an unpaid fixed cost whose due date has passed stays set aside in the current cycle until the user taps **Mark paid** or **Skip this cycle**. Its badge reads "Overdue". Skip releases the amount and creates no expense.
- **Mark paid** moves the fixed cost from Reserved to Actual: the linked expense is deducted from the paying account's balance and added to actual spent, so total budget consumption does not change. **Left to spend changes only by the variance: Scheduled amount − Actual paid amount.** The same rule applies when an expense is linked to a bill instead of a new one being posted. This supersedes the Q-21 wording "Confirm reduces Left to spend".

**% used, status, per day**
- % used = actual spent / budget. Reserved fixed costs are not added. Display is half-up to an integer, but never 100% while spent < budget (99.1–99.9% shows 99%).
- Status (on actual spent): **On track** when % used <= elapsed; **Over pace** when % used > elapsed and <= 100%; **Over budget** when > 100% (caption "Over budget by ฿x", x = spent − budget). **No budget** shows Net cash flow instead. Open: what the Over budget caption shows while fixed costs are still set aside (Q-61).
- **Per day left = max(0, floor(Left to spend / Days left))**, whole baht. It is a display pacing guide only: never multiply it back into an amount (the forecast uses the exact Left to spend).
- **Negative Left to spend** (set-aside fixed costs are more than what is left, spent still <= budget): show the exact negative figure (e.g. `−฿399`) in the alert colour, per day reads `฿0/day`, and the daily pacing helper text reads "Bills exceed budget by ฿399". Never show ฿0 for a deficit. % used and status stay on actual spent. Alert colour = `night/accent` (coral) with an icon and a label, the established mapping for the spec's #FF3B30 (Ton to confirm, Q-59); never a hard-coded hex.
- Budget alerts notify at 90% and 100% of actual spent.

**Worked examples** (golden data: budget ฿40,000, payday 25th, cycle 25 Oct – 24 Nov 2026, spent ฿33,550, AIS mobile bill ฿599 due 22 Nov)
| Date and situation | Left to spend | Days left | Per day | % used | Status |
|---|---|---|---|---|---|
| 18 Nov, AIS unpaid (set aside) | 40,000 − 33,550 − 599 = **฿5,851** | 7 | floor(5,851 / 7) = **฿835** | 84% | Over pace (83.9% > 80.6%) |
| 22 Nov, Mark paid ฿599 (variance 0) | spent 34,149, reserved 0 → **฿5,851** (unchanged) | 3 | ฿1,950 | 85% | On track |
| 22 Nov, Mark paid ฿650 (variance −51) | **฿5,800** | 3 | ฿1,933 | 86% | On track |
| 22 Nov, Mark paid ฿500 (variance +99) | **฿5,950** | 3 | ฿1,983 | 85% | On track |
| 23 Nov, AIS still unpaid (Overdue, still set aside) | **฿5,851** | 2 | ฿2,925 | 84% | On track (84% <= 96.8%) |
| 18 Nov, spent ฿39,800, AIS unpaid | 40,000 − 39,800 − 599 = **−฿399** | 7 | max(0, floor(−399 / 7)) = **฿0** | 99% | Over pace; helper "Bills exceed budget by ฿399" |
| 25 Nov (first day of "Dec cycle · 25 Nov – 24 Dec"), nothing spent, all 5 fixed costs set aside (Rent ฿12,000, Spotify ฿139, iPhone installment ฿1,290, Netflix ฿419, AIS ฿599 = ฿14,447) | 40,000 − 0 − 14,447 = **฿25,553** | 30 | **฿851** | 0% | On track |

Clamp examples: payday 31, today 15 Feb 2027 → cycle "Feb cycle · 31 Jan – 27 Feb", 13 days left. Card cut-off 31 / due 30, today 15 Feb 2027 → the open statement closes 28 Feb (31 → 28); the January statement's payment is due 28 Feb 2027 (30 → 28), "Due in 13 days" (days until due = due date − today, no +1). Full tables: `docs/plan/golden-sample-data.md`.

## Categories
- Seed expense: Food & Drink, Transport, Bills & Utilities, Shopping, Health, Entertainment, Subscriptions, Other. Seed income: Salary, Business, Investment, Gift, Other.
- Seed categories can be hidden, not deleted. Custom categories may use a tint + icon or a photo thumbnail.

## E-slip
- QR decoding is on-device only. Fields read from the slip are tagged "From slip"; inferred fields are "Suggested". "Bank verified" appears only after a bank API confirms (not in Phase 1).

## Privacy
- Never log amounts, notes, merchant names, account numbers or slip images to analytics, crash reporting or console.

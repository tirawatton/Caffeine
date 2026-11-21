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
- Cycle: monthly, starting on the user's cycle start day (default 1st). Month boundaries use the device timezone, not UTC.
- Left to spend = budget − sum(expenses in cycle). Income never reduces spend.
- % used = spent / budget. Elapsed = days elapsed / days in cycle (inclusive of today).
- Status: **On track** when % used <= elapsed; **Over pace** when % used > elapsed and <= 100%; **Over budget** when > 100% (caption "Over budget by ฿x"). **No budget** shows Net cash flow instead.
- Per-day allowance = left to spend / days remaining (including today), whole baht, floored at 0.
- Budget alerts notify at 90% and 100%.

## Categories
- Seed expense: Food & Drink, Transport, Bills & Utilities, Shopping, Health, Entertainment, Subscriptions, Other. Seed income: Salary, Business, Investment, Gift, Other.
- Seed categories can be hidden, not deleted. Custom categories may use a tint + icon or a photo thumbnail.

## E-slip
- QR decoding is on-device only. Fields read from the slip are tagged "From slip"; inferred fields are "Suggested". "Bank verified" appears only after a bank API confirms (not in Phase 1).

## Privacy
- Never log amounts, notes, merchant names, account numbers or slip images to analytics, crash reporting or console.

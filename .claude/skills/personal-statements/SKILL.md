---
name: personal-statements
description: How Caffeine turns the on-device ledger into personal financial statements - the /finance:financial-statements method mapped to one person's money - a Cash flow statement (income statement), a Net worth statement (balance sheet) and an Account movement statement (cash flow statement), with cycle-over-cycle and budget comparison, variance and drivers, key ratios and the tie-out checks that prove the data design is complete. Use when a feature shows totals, balances, reports, forecasts or exports. Loaded by local-data-engineer; read by backend-lead and ba.
---

# Personal Financial Statements

Method adapted from `/finance:financial-statements` (if the `finance:financial-statements` or `finance:variance-analysis` plugin skill is available, you may load it with the Skill tool; this file wins where they differ). These are product calculations for one person, not GAAP reporting and not financial advice.

**Why the data engineer owns this:** if the tables can produce all three statements and every tie-out balances on the golden data, the data design is complete. A screen figure that no statement line explains is a missing query; a tie-out that does not balance is a missing column or a wrong rule.

## 1. Basis (fixed rules, from `caffeine-domain`)
- **Cash basis with one exception:** an expense counts on the day it happens, even on a credit card. Paying the card later is a **transfer**, never an expense (no double count).
- Transfers and card payments never enter income, expenses, budgets or Net.
- Period = the **budget cycle** (payday to the day before next payday, `cycleStartDay`), dates by `localDate`. Comparison periods: previous cycle, and the same cycle last year when 12 months of data exist.
- Money: Decimal, half-up 2 dp; whole baht in lists and heroes; every amount signed.
- Installments: each monthly charge is the expense; the remaining balance is a **note** under Net worth until the E10/E11 contract decides (glossary G-5).

## 2. The three statements (mapping)
| Company statement | Caffeine statement | Screens it feeds |
|---|---|---|
| Income statement | **Cash flow statement** — Income by category, Expenses by category, Net cash flow | Home hero (spent, left), Analytics Spending / Cash Flow, History In/Out/Net, Export |
| Balance sheet | **Net worth statement** — Assets (cash, bank, e-wallet; most liquid first) − Liabilities (credit cards owed) = Net worth | Wallet, Analytics Trends, Profile baseline |
| Cash flow statement (direct) | **Account movement statement** — per account: opening + money in − money out ± transfers = closing | Wallet card balances, Reconcile, Forecast "Cash & bank" |

### Cash flow statement layout
```
CASH FLOW STATEMENT · cycle 25 Oct – 24 Nov 2026 · THB
                       This cycle   Prev cycle   Var ฿     Var %    Budget    Budget var
INCOME
  Salary               +52,000      …
TOTAL INCOME           +52,000
EXPENSES (largest first)
  Bills & Utilities    −13,850
  Food & Drink         −12,115
  …
TOTAL EXPENSES         −33,550                                       40,000    6,450 left
NET CASH FLOW          +18,450
  Savings rate          35.5%       (net ÷ income)
```
### Net worth statement layout
```
NET WORTH · as of 18 Nov 2026
ASSETS        Cash 3,248 · KBank Savings 53,650 · Total assets 56,898
LIABILITIES   KBank Credit −13,948 · Total liabilities −13,948
NET WORTH     42,950
Note: installments not yet charged ฿10,320 (not in liabilities, G-5)
```

## 3. Comparison and variance
For every line: **Var ฿** = this − comparison; **Var %** = (this − comparison) ÷ |comparison| × 100, half-up 1 dp, "—" when the comparison is 0; ratios change in percentage points.
**Material** (worth a flag or an insight) when |Var ฿| ≥ ฿1,000 **and** |Var %| ≥ 15% — a default for Ton to confirm; keep it in one place (`caffeine-domain`) when confirmed.
**Drivers** for a material expense line (each needs a query or the line can't be explained):
- **Count effect** (more purchases): (n₁ − n₀) × avg₀
- **Ticket effect** (bigger purchases): n₁ × (avg₁ − avg₀)  — the two add up to Var ฿
- **New / stopped** category (present in one period only)
- **One-off vs fixed** (fixed-cost rows vs everything else)
- **Timing** (a bill paid in the next or previous cycle)

## 4. Key ratios
Savings rate = Net ÷ Income · Budget used % = spent ÷ budget · Credit used % = owed ÷ limit · Category share = line ÷ total expenses · Per-day allowance and pace come from `caffeine-domain` (not re-derived here).

## 5. Tie-out checks (each becomes an `-- expect:` and a `-cases.md` row)
1. Σ category lines = Total expenses (golden: ฿33,550).
2. Income − Expenses = Net cash flow (฿18,450).
3. Σ account closings = Total assets + Total liabilities = Net worth (฿42,950).
4. **Articulation:** opening Net worth + Net cash flow = closing Net worth (24,500 + 18,450 = 42,950) — proves no money appears or vanishes.
5. Transfer legs sum to 0 across accounts.
6. Card owed = previous owed + charges − payments (฿13,948).
7. Budget left = budget − Total expenses (฿6,450).

## 6. What to write (`docs/data-model/<feature>-statements.md`, only when the feature shows money totals)
1. Which statement lines the feature shows, and on which screen.
2. Each line → the query in `<feature>-queries.md` that produces it + its reduce step.
3. The comparison columns the feature needs (prev cycle, budget, last year) and the queries for them.
4. Tie-outs from §5 that apply, each with its query name and golden value (they must PASS in `verify_queries.py`).
5. Gaps: a line the tables can't produce yet → a column or table request in `<feature>-tables.md`, or an open question.

## 7. Readiness checklist
1. Every money figure on the feature's screens maps to a statement line and a query.
2. Every applicable tie-out is an `-- expect:` that passes.
3. No transfer or card payment reaches income, expense, budget or Net (grep the queries for the type filter).
4. Variance and driver queries exist for every comparison the plan shows.

# Golden sample data

Author: `ba` · 2026-11-21 · **Revision 3** (Ton's answers to Q-54 to Q-58, decisions file Part 5; revision 2 applied Q-51, Q-52, Q-53 and the glossary review)
Status: **rules approved by Ton; every value final.** Revision 3 removed the ‡ marks: Ton Q-55 sets aside every kind of fixed cost, so the Dec-cycle figure is **฿25,553 · ฿851/day**. New §5 rows: Mark paid at ฿500, Overdue (23 Nov), negative Left to spend (−฿399).

One deterministic dataset for designers (frame copy), backend-lead (`*-cases.md` rows), developers (previews, seed data in debug builds only) and QA (screenshot and parity checks). Every derived figure below is computed from `caffeine-domain` (updated 21 Nov 2026 with Ton's approval to carry these rules) and master plan §5. **Figma numbers that disagree with this sheet are sample errors to re-sync (DG-51), not rules.** Terms follow `docs/plan/glossary.md`.

Rules used:
- Money is Decimal, half-up to 2 dp; whole baht in lists and heroes; every amount signed; transfers and card payments never count in In / Out / Net or budgets.
- **Period = budget cycle everywhere** (Home, Analytics, History default; Ton Q-52). Calendar month exists only as a secondary History filter.
- **Safe to Spend (UI "Left to spend") = Budget − Actual expenses in the cycle − Upcoming & overdue unpaid fixed costs (bills + subscriptions + installments) due in the active cycle** (Ton Q-51 B as widened by Q-55, overdue by Q-58), one formula for Home, the widget snapshot and Forecast.
- **Mark paid** moves a fixed cost from Reserved to Actual; Left to spend changes only by Scheduled − Actual paid (Ton Q-56, supersedes the Q-21 wording).
- Days left and per day count today; **per day = max(0, floor(Safe to Spend / days left))**, a display pacing guide only (Ton Q-16, Q-48, Q-51 A, Q-54).
- Budget % and pace status use **actual spent only**. A negative Safe to Spend shows the exact figure and "Bills exceed budget by ฿x" (Ton Q-54).
- One clamp for every day-of-month rule: `min(targetDay, daysInMonth)`, always snapping back (Ton Q-15, Q-53).

## 1. Fixed context
| Item | Value |
|---|---|
| Today | **Wednesday 18 Nov 2026**, time zone Asia/Bangkok |
| User | Ton Raweephat (signed in with Apple), Personal space only (single-user V1.0) |
| Payday / cycle start | **25th** (`cycleStartDay` = 25, not "Last day of the month") |
| Current budget cycle | **25 Oct 2026 – 24 Nov 2026** (31 days) · label **"Nov cycle · 25 Oct – 24 Nov"** (shown in Caption Upper as `NOV CYCLE · 25 OCT – 24 NOV`) |
| Previous cycle | 25 Sep 2026 – 24 Oct 2026 · label "Oct cycle · 25 Sep – 24 Oct" · **aggregates only**: In +฿52,000, Out −฿35,700, Net +฿16,300 (no line items; used for "vs Oct cycle") |
| Monthly budget | **฿40,000** |
| Salary | **+฿52,000** on the 25th, recurring income, into KBank Savings |
| Privacy Mode / App Lock | off / off (masked variants: every amount reads `฿••••••`) |

**Cycle label rule (Ton Q-52):** a cycle is named after the month of its **last day** (the closing month), followed by its first and last dates: `<Mon> cycle · <d Mon> – <d Mon>`. Comparisons name the previous cycle the same way: "vs Oct cycle" ("vs prev cycle" is the approved short form where the month name does not fit).

## 2. Accounts (all Include in Net Worth = on)
| Account | Type | Masked no. | Balance on 25 Oct, before salary | Notes |
|---|---|---|---|---|
| Cash | Cash | — | ฿1,000 | Auto-created at onboarding (Ton Q-13), later topped up |
| KBank Savings | Bank Account | ··4410 | ฿30,000 | Salary account |
| KBank Credit | Credit Card | ··7731 | owes ฿6,500 | Limit ฿50,000 · statement cut-off day **25** · payment due day **10** |

The ฿6,500 owed on 25 Oct is the statement 26 Sep–25 Oct, due 10 Nov (it includes installment 1 of 10, charged 10 Oct).

## 3. Transactions in the current cycle (25 Oct – 18 Nov 2026)
| # | Date | Type | Category | Memo / merchant | Account | Amount |
|---|---|---|---|---|---|---|
| I1 | 25 Oct | income | Salary | Monthly salary | KBank Savings | +฿52,000 |
| T1 | 26 Oct | transfer | — | ATM withdrawal | KBank Savings → Cash | ฿3,000 |
| E1 | 26 Oct | expense | Food & Drink | Makro groceries | KBank Credit | −฿4,200 |
| E2 | 01 Nov | expense | Bills & Utilities | Rent (fixed cost, marked paid) | KBank Savings | −฿12,000 |
| E13 | 02 Nov | expense | Shopping | Uniqlo | KBank Credit | −฿3,030 |
| E3 | 03 Nov | expense | Subscriptions | Spotify (fixed cost) | KBank Credit | −฿139 |
| E4 | 05 Nov | expense | Bills & Utilities | Electricity (MEA) | KBank Savings | −฿1,850 |
| E5 | 08 Nov | expense | Transport | PTT fuel | KBank Credit | −฿1,500 |
| E14 | 09 Nov | expense | Food & Drink | Tops Market | KBank Savings | −฿5,000 |
| T2 | 10 Nov | transfer (card payment) | — | Pay KBank Credit statement | KBank Savings → KBank Credit | ฿6,500 |
| E6 | 10 Nov | expense | Shopping | iPhone 17 Pro 0% installment 2 of 10 | KBank Credit | −฿1,290 |
| E7 | 12 Nov | expense | Health | Pharmacy | Cash | −฿640 |
| E8 | 14 Nov | expense | Entertainment | Cinema | KBank Credit | −฿520 |
| E9 | 15 Nov | expense | Food & Drink | Restaurant dinner | KBank Credit | −฿2,850 |
| E10 | 17 Nov | expense | Subscriptions | Netflix (fixed cost) | KBank Credit | −฿419 |
| E11 | 18 Nov | expense | Food & Drink | Iced latte, Café Amazon | Cash | −฿65 |
| E12 | 18 Nov | expense | Transport | BTS Asok → Siam | Cash | −฿47 |

17 entries: 14 expenses, 1 income, 2 transfers.

Category totals: Bills & Utilities ฿13,850 · Food & Drink ฿12,115 · Shopping ฿4,320 · Transport ฿1,547 · Health ฿640 · Subscriptions ฿558 · Entertainment ฿520 · **Total ฿33,550**.

## 4. Derived figures on 18 Nov 2026

### 4.1 Home (Budget hero v5)
| Figure | Calculation | Shown |
|---|---|---|
| Hero label | cycle 25 Oct – 24 Nov, closing month Nov (Ton Q-52) | **"Nov cycle · 25 Oct – 24 Nov"** (Caption Upper: `NOV CYCLE · 25 OCT – 24 NOV`) |
| Spent (expenses in cycle) | sum of E1–E14 | ฿33,550 |
| Upcoming & overdue unpaid fixed costs in cycle (set aside) | AIS mobile ฿599, due 22 Nov, not paid (§4.6); the other 4 are paid | ฿599 |
| **Left to spend (Safe to Spend)** | 40,000 − 33,550 − 599 (Ton Q-51 B, Q-55) | **฿5,851** |
| Budget % | 33,550 / 40,000 = 83.875%, half-up (actual spent only) | **84%** |
| Days left | (24 Nov − 18 Nov) + 1 (Ton Q-48) | **7 days left** |
| Elapsed | 25 / 31 = 80.6% | (pace marker) |
| Pace status | 83.875% > 80.6% and ≤ 100% | **Over pace** |
| **Per day** | floor(5,851 / 7) = floor(835.86) (Ton Q-16, Q-51 A) | **฿835/day** |
| Hero detail line | — | "of ฿40,000 · ฿835/day" (whether the ฿599 set aside is shown on the hero is a design choice, DG-55) |
| Spent today | E11 + E12 | ฿112 |
| Alert slot | budget 84% < 90%, so the Bills alert shows | Bills alert: 1 unpaid bill left this cycle (AIS ฿599, 22 Nov) |

**"Days left" is 7, not 6.** The golden "today" is 18 Nov and the cycle ends 24 Nov, so (24 − 18) + 1 = 7 (Ton Q-48), which is also the divisor in Ton's Q-51 example (฿5,851 → ฿835/day over 7 days). The Figma heroes' "6 days left · ฿1,075/day" are wrong (DG-48).

### 4.2 Cash, cash flow and net worth
| Figure | Calculation | Shown |
|---|---|---|
| Cash balance | 1,000 + 3,000 − 640 − 65 − 47 | ฿3,248 |
| KBank Savings balance | 30,000 + 52,000 − 3,000 − 12,000 − 1,850 − 5,000 − 6,500 | ฿53,650 |
| KBank Credit owed | 6,500 + (4,200 + 3,030 + 139 + 1,500 + 1,290 + 520 + 2,850 + 419) − 6,500 | ฿13,948 (shown −฿13,948 under **Debts**) |
| **Total Cash Balance** | 3,248 + 53,650 (cash, bank, e-wallet; no cards) | **฿56,898** |
| **Net Cash Flow** (Nov cycle to date) | In 52,000 − Out 33,550 (T1, T2 excluded) | **+฿18,450** (In +฿52,000 · Out −฿33,550) |
| **Net Worth** | Assets 56,898 − Debts 13,948 | **฿42,950** |
| Available credit | 50,000 − 13,948 | ฿36,052 |
| Credit used | 13,948 / 50,000 = 27.896%, half-up | 28% |

Net Worth leaves out the 8 installment payments not yet charged (฿10,320). This is a dataset assumption for the E10 / E11 contract to confirm (glossary G-5).

### 4.3 History (Ton Q-52)
| View | Period | Entries | Summary row | In / Out |
|---|---|---|---|---|
| **Default** | "Nov cycle · 25 Oct – 24 Nov" (cycle to date: 25 Oct – 18 Nov) | 17 | "Net cash flow · 17 entries" **+฿18,450** | In +฿52,000 · Out −฿33,550 |
| Secondary filter **Calendar month: November 2026** | 1 Nov – 18 Nov | 14 (13 expenses + T2) | "Total outflow · 14 entries" **฿29,350** (In = ฿0, so the contextual label applies) | In ฿0 · Out −฿29,350 |
| Day header, today | Wed 18 Nov | 2 | day net −฿112 (neutral `text-secondary`) | — |

29,350 = 33,550 − 4,200 (E1, 26 Oct, belongs to the cycle but not to calendar November). The calendar month is a lookup filter (tax, calendar questions); it never changes Home, Analytics or the budget.

### 4.4 Analytics (Ton Q-52; Ton G-8: the screen is titled **Analytics**, not Reports)
| Figure | Calculation | Shown |
|---|---|---|
| Period row | current cycle vs previous cycle (full previous period, as the 4A design compares today) | "25 Oct – 24 Nov 2026 · Compared to 25 Sep – 24 Oct 2026" |
| Spending hero | expenses in the Nov cycle | "TOTAL SPENT · NOV CYCLE" **฿33,550** |
| Spending change | (33,550 − 35,700) / 35,700 = −6.02%, integer half-up (Ton Q-16) | **"↓ 6% vs Oct cycle"** (not "↓ 6.0% vs Oct") |
| Cash Flow hero | Net Cash Flow, Nov cycle | **+฿18,450**, "↑ ฿2,150 vs Oct cycle" (18,450 − 16,300) |
| Category rows | §3 category totals | sum ฿33,550 = hero |

### 4.5 Credit card (rule A2, E10-T13)
| Figure | Value |
|---|---|
| Open statement period | 26 Oct – 25 Nov 2026 |
| Statement balance at the 25 Nov cut-off (if nothing else goes on the card) | ฿13,948 |
| Next payment due | **10 Dec 2026** → "Due in 22 days" (strip: "Payment due 10 Dec · in 22 days", "Cut-off 25 Nov") |
| Previous statement | 26 Sep – 25 Oct, ฿6,500, due 10 Nov, paid in full on 10 Nov (T2) |
| Card reminder | "due tomorrow" notification on **9 Dec 2026**; none on 24 Nov |

Cut-off 25 and due 10 never need clamping; clamped card examples are in §6.3.

### 4.6 Fixed costs (Nov cycle 25 Oct – 24 Nov)
| Item | Kind | Day | Account | Amount | State on 18 Nov | Next charge | Reminder date |
|---|---|---|---|---|---|---|---|
| Rent | Bill | 1st | KBank Savings | ฿12,000 | Paid 1 Nov (E2) | 1 Dec | 30 Nov |
| Spotify | Subscription | 3rd | KBank Credit | ฿139 | Paid 3 Nov (E3) | 3 Dec | 2 Dec |
| iPhone 17 Pro | Installment | 10th | KBank Credit | ฿1,290 | Paid 10 Nov (E6) | 10 Dec | 9 Dec |
| Netflix | Subscription | 17th | KBank Credit | ฿419 | Paid 17 Nov (E10) | 17 Dec | 16 Dec |
| AIS mobile | Bill | 22nd | KBank Savings | ฿599 | **Upcoming, unpaid → set aside in Safe to Spend** | 22 Nov | **21 Nov** |

Totals: ฿14,447 this cycle (subscriptions ฿558 · bills ฿12,599 · installments ฿1,290); paid ฿13,848; remaining ฿599. Reminder dates assume the one-day lead in Ton's approved copy ("due tomorrow"); the E13 plan confirms the lead time. Every kind is set aside while unpaid (Ton Q-55); on 18 Nov only AIS is unpaid. If AIS is still unpaid on 23 Nov its badge reads **"Overdue"** and it stays set aside until Mark paid or Skip this cycle (Ton Q-58; §5).

Installment plan: iPhone 17 Pro, ฿12,900 at 0% over 10 months = ฿1,290 / month, charged to KBank Credit on the 10th from 10 Oct 2026. On 18 Nov: **"2 of 10"** paid, next 10 Dec 2026, last payment **10 Jul 2027**, remaining ฿10,320 (8 × 1,290). Each monthly charge is the expense; the ฿12,900 purchase is never expensed in one go (dataset assumption for the E11 contract).

### 4.7 Month-end forecast (Ton Q-47 + Q-51, final)
Horizon = the current cycle end, **24 Nov 2026** ("Balance on 24 Nov").
| Line | Rule | Amount |
|---|---|---|
| Cash & bank | Total Cash Balance now | ฿56,898 |
| Income | income dated 19–24 Nov; the 25 Nov salary is the next cycle, so it is excluded | ฿0 |
| Fixed bills | upcoming and overdue unpaid fixed costs of every kind paid from cash or bank, due up to 24 Nov: AIS on 22 Nov (card-charged fixed costs reach cash only at the card payment). Line label vs Ton Q-57 "Fixed costs": DG-56 | −฿599 |
| Card payments | card payments due 19–24 Nov; KBank Credit is due 10 Dec, outside the horizon | ฿0 |
| Daily spending | label "฿835/day × 7 days" (same per day and days left as Home); **amount = exact remaining variable budget (Safe to Spend), not 835 × 7** (Ton Q-51 A) | −฿5,851 |
| **Balance on 24 Nov** | 56,898 + 0 − 599 − 0 − 5,851 | **฿50,448 · On track** |

AIS is counted once: it is the Fixed bills line and is already excluded from the ฿5,851 (Ton Q-51 B). Fixed bills + daily spending = 599 + 5,851 = ฿6,450 = budget − spent. The label's 835 × 7 = ฿5,845 is never used as an amount.

Shortfall example (9K): Cash & bank ฿5,000 with the same lines → 5,000 − 599 − 5,851 = **−฿1,450 · Shortfall**.

## 5. Other dates in the same dataset
| Scenario | Inputs | Result |
|---|---|---|
| Day before AIS is due | 21 Nov 2026, nothing new spent, AIS still unpaid | Spent ฿33,550 · Left **฿5,851** · 84% · **"4 days left"** · **฿1,462/day** (5,851 / 4 = 1,462.75) · elapsed 28 / 31 = 90.3% → **On track** |
| AIS marked paid at the expected amount | 22 Nov 2026, Mark paid ฿599 from KBank Savings | Spent ฿34,149 · set aside ฿0 · variance 0 → Left **฿5,851 (unchanged)** · 85% (85.37%) · "3 days left" · **฿1,950/day** (1,950.33) · elapsed 29 / 31 = 93.5% → On track (Ton Q-56) |
| AIS paid more than scheduled | 22 Nov 2026, Mark paid ฿650 | Spent ฿34,200 · variance 599 − 650 = −฿51 → Left **฿5,800** · 86% (85.5% half-up) · "3 days left" · ฿1,933/day (1,933.33) · On track (Ton Q-56) |
| AIS paid less than scheduled | 22 Nov 2026, Mark paid ฿500 | Spent ฿34,050 · variance 599 − 500 = +฿99 → Left **฿5,950** · 85% (85.125%) · "3 days left" · ฿1,983/day (1,983.33) · On track (Ton Q-56) |
| AIS overdue | 23 Nov 2026, AIS still unpaid, nothing new spent | Spent ฿33,550 · set aside ฿599 (Overdue, Ton Q-58) · Left **฿5,851** · 84% · "2 days left" · **฿2,925/day** (2,925.5) · elapsed 30 / 31 = 96.8% → On track · AIS badge **"Overdue"** |
| AIS skipped | 23 Nov 2026, AIS overdue, user taps Skip this cycle | Set aside ฿0, no expense · Spent ฿33,550 · Left **฿6,450** · "2 days left" · ฿3,225/day · 84% · On track |
| Negative Left to spend (variant) | 18 Nov 2026, spent ฿39,800 (the dataset plus ฿6,250 more variable spending), AIS ฿599 unpaid | Left 40,000 − 39,800 − 599 = **−฿399** (exact, alert colour) · 99% (99.5%, 99% rule) · Over pace (99.5% > 80.6%) · "7 days left" · **฿0/day** (max(0, floor(−399 / 7))) · helper **"Bills exceed budget by ฿399"** (Ton Q-54) |
| Last day of the cycle | 24 Nov 2026; AIS ฿599 paid 22 Nov, nothing else spent | Left ฿5,851 · **"1 day left"** · ฿5,851/day · 85% · On track (elapsed 31 / 31 = 100%) |
| First day of the next cycle | 25 Nov 2026, salary +฿52,000 received, nothing spent, AIS for Nov paid on 22 Nov | Label **"Dec cycle · 25 Nov – 24 Dec"** (30 days) · 0% · **"30 days left"** · On track · set aside (every kind, Ton Q-55): Rent 1 Dec ฿12,000, Spotify 3 Dec ฿139, iPhone 10 Dec ฿1,290, Netflix 17 Dec ฿419, AIS 22 Dec ฿599 = ฿14,447 → Left **฿25,553** · **฿851/day** (851.77). (The Bills-only option ฿27,401 · ฿913/day and the old ฿40,000 · ฿1,333/day are superseded.) |
| No payday set (1st-of-month cycle), 18 Nov | Same Nov expenses on a 1–30 Nov cycle: E2–E14 = ฿29,350; AIS ฿599 unpaid (Rent, Spotify, iPhone, Netflix already paid in Nov) | Label "Nov cycle · 1 Nov – 30 Nov" · Left 40,000 − 29,350 − 599 = **฿10,051** · 73% (73.375%) · 13 days left · **฿773/day** (773.15) · elapsed 18 / 30 = 60% → Over pace · forecast horizon 30 Nov, daily line "฿773/day × 13 days" −฿10,051 |
| New user | O5 budget ฿40,000, payday 25, onboarding finished 18 Nov, no fixed costs | Left ฿40,000 · 0% · 7 days left · **฿5,714/day** · On track · Wallet holds Cash ฿0 |

## 6. Month-day clamping (Ton Q-15 payday, Ton Q-53 cards; one shared function)
`clampDay(year, month, targetDay) = min(targetDay, daysInMonth(year, month))`. Used for **payday / budget cycles, recurring commitments (fixed costs, recurring income) and card cut-off and due days**. It always snaps **back** to the month's last valid day and never rolls into the next month. The stored anchor never changes (a 31st rule stays 31; February's 28 does not drift into March).

### 6.1 Payday cycles
| Payday rule | Cycle | Label | Days |
|---|---|---|---|
| 31st | 31 Jan 2027 – 27 Feb 2027 (Feb payday clamps to 28 Feb) | Feb cycle · 31 Jan – 27 Feb | 28 |
| 31st | 28 Feb 2027 – 30 Mar 2027 | Mar cycle · 28 Feb – 30 Mar | 31 |
| 31st | 31 Mar 2027 – 29 Apr 2027 (Apr payday clamps to 30 Apr) | Apr cycle · 31 Mar – 29 Apr | 30 |
| 31st, leap year | 31 Jan 2028 – 28 Feb 2028 (Feb payday 29 Feb) | Feb cycle · 31 Jan – 28 Feb | 29 |
| 30th | 30 Jan 2027 – 27 Feb 2027 | Feb cycle · 30 Jan – 27 Feb | 29 |
| 30th | 28 Feb 2027 – 29 Mar 2027 (Mar payday stays 30 Mar) | Mar cycle · 28 Feb – 29 Mar | 30 |
| 29th | 29 Jan 2027 – 27 Feb 2027 | Feb cycle · 29 Jan – 27 Feb | 30 |
| Last day of the month | 31 Jan 2027 – 27 Feb 2027, then 28 Feb – 30 Mar 2027 | as 31st | 28, 31 |
| 25th, year boundary | 25 Dec 2026 – 24 Jan 2027 | Jan cycle · 25 Dec – 24 Jan | 31 |
| 1st (default, no payday) | 1 Nov 2026 – 30 Nov 2026 | Nov cycle · 1 Nov – 30 Nov | 30 |

Payday 31 and "Last day of the month" give the same dates in every month. They differ only in the label the user chose ("31st" vs "Last day"); see glossary G-6.

Example: payday 31, today 15 Feb 2027 → cycle 31 Jan – 27 Feb 2027, days left (27 − 15) + 1 = **13**; previous cycle "Jan cycle · 31 Dec – 30 Jan".

### 6.2 Recurring commitments (fixed costs, recurring income)
| Rule | Next 5 charge dates from Jan 2027 | Reminder ("due tomorrow") for Feb |
|---|---|---|
| Monthly on the 31st | 31 Jan, **28 Feb**, 31 Mar, **30 Apr**, 31 May 2027 (leap year: **29 Feb 2028**) | 27 Feb 2027 |
| Monthly on the 30th | 30 Jan, **28 Feb**, 30 Mar, 30 Apr, 30 May 2027 | 27 Feb 2027 |
| Monthly on the 29th | 29 Jan, **28 Feb**, 29 Mar, 29 Apr, 29 May 2027 (leap year: 29 Feb 2028) | 27 Feb 2027 |

### 6.3 Credit card cut-off and due days (Ton Q-53)
Sample card for clamping only (not in the §2 dataset): **cut-off day 31, payment due day 30**. Each statement runs from the day after the previous cut-off to this cut-off; its payment is due on the first clamped due day after the cut-off.
| Statement period | Cut-off (statement date) | Payment due |
|---|---|---|
| 1 Jan – 31 Jan 2027 | 31 Jan 2027 | **28 Feb 2027** (30 → 28) |
| 1 Feb – 28 Feb 2027 | **28 Feb 2027** (31 → 28) | 30 Mar 2027 |
| 1 Mar – 31 Mar 2027 | 31 Mar 2027 | 30 Apr 2027 |
| 1 Apr – 30 Apr 2027 | **30 Apr 2027** (31 → 30) | 30 May 2027 |
| 1 Jan – 31 Jan 2028 | 31 Jan 2028 | **29 Feb 2028** (leap year) |
| 1 Feb – 29 Feb 2028 | **29 Feb 2028** | 30 Mar 2028 |

Example: today 15 Feb 2027 → open statement 1 Feb – 28 Feb 2027; next payment due **28 Feb 2027**, **"Due in 13 days"**, paying the statement 1 Jan – 31 Jan 2027; "due tomorrow" reminder on **27 Feb 2027**. (Days until due = due date − today, with no +1, as "Due in 22 days" from 18 Nov to 10 Dec.)

## 7. Masked and empty variants
- Privacy Mode on: every amount above reads `฿••••••`; counts ("7 days left", "2 of 10", "17 entries", "84%") and cycle labels ("Nov cycle · 25 Oct – 24 Nov") stay visible. Whether the budget % is masked is decided in E06.
- New user: see §5.

## 8. Reconciliation checks (all pass)
- Expenses: category totals = ฿33,550 = sum of E1–E14 = Home spent = History cycle Out = Analytics hero.
- Calendar November: 33,550 − 4,200 (E1) = ฿29,350 = sum of E2–E14.
- Safe to Spend: 40,000 − 33,550 − 599 = ฿5,851; per day floor(5,851 / 7) = ฿835 (835 × 7 = 5,845, display only).
- Mark paid variance (Ton Q-56): 5,851 + (599 − 599) = 5,851; 5,851 + (599 − 650) = 5,800; 5,851 + (599 − 500) = 5,950. Each equals 40,000 − new spent − 0 set aside.
- Dec cycle (Ton Q-55): 12,000 + 139 + 1,290 + 419 + 599 = 14,447; 40,000 − 14,447 = 25,553; floor(25,553 / 30) = 851.
- Negative (Ton Q-54): 40,000 − 39,800 − 599 = −399; max(0, floor(−399 / 7)) = 0.
- Accounts: 3,248 + 53,650 − 13,948 = ฿42,950 = Net Worth; opening worth 1,000 + 30,000 − 6,500 = 24,500, + Net Cash Flow 18,450 = 42,950 ✓ (transfers move value between accounts only).
- Card: 13,948 = statement-to-date charges (4,200 + 3,030 + 139 + 1,500 + 1,290 + 520 + 2,850 + 419).
- Fixed costs: 12,000 + 139 + 1,290 + 419 + 599 = ฿14,447; paid 13,848 + unpaid 599 = 14,447.
- Forecast: 56,898 − 599 − 5,851 = ฿50,448; 599 + 5,851 = 6,450 = budget − spent (AIS counted once).
- Analytics: −6.02% → "↓ 6%"; 18,450 − 16,300 = +฿2,150.
- Clamps: every §6 date = min(target, days in month); no date falls on the 1st of a following month.

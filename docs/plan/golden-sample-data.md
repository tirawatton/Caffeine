# Golden sample data (draft for the next handoff package)

Author: `ba` · 2026-11-21 · Status: **draft, Ton to review** · Decision: Ton, audit findings 13–15 (`docs/decisions/2026-11-21-ton-answers.md` Part 3)

One deterministic dataset for designers (frame copy), backend-lead (`*-cases.md` rows), developers (previews, seed data in debug builds only) and QA (screenshot and parity checks). Every derived figure below is computed from `caffeine-domain`, Ton's decisions (Q-16, Q-48, Q-15, Q-47, A1, A2) and master plan §5. **Figma numbers that disagree with this sheet are sample errors to re-sync (DG-51), not rules.** Terms follow `docs/plan/glossary.md`.

Rules used: money is Decimal, half-up to 2 dp; whole baht in lists and heroes; every amount signed; transfers and card payments never count in In / Out / Net or budgets; days left and per day count today; per day is floored.

## 1. Fixed context
| Item | Value |
|---|---|
| Today | **Wednesday 18 Nov 2026**, time zone Asia/Bangkok |
| User | Ton Raweephat (signed in with Apple), Personal space only (single-user V1.0) |
| Payday / cycle start | **25th** (`cycleStartDay` = 25, not "Last day of the month") |
| Current budget cycle | **25 Oct 2026 – 24 Nov 2026** (31 days) |
| Monthly budget | **฿40,000** |
| Salary | **+฿52,000** on the 25th, recurring income, into KBank Savings |
| Privacy Mode / App Lock | off / off (masked variants: every amount reads `฿••••••`) |

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
| Spent (expenses in cycle) | sum of E1–E14 | ฿33,550 |
| Left to spend (Safe to Spend) | 40,000 − 33,550 | **฿6,450** |
| Budget % | 33,550 / 40,000 = 83.875%, half-up | **84%** |
| Days left | (24 Nov − 18 Nov) + 1 (Ton Q-48) | **7 days left** |
| Elapsed | 25 / 31 = 80.6% | (pace marker) |
| Pace status | 83.875% > 80.6% and ≤ 100% | **Over pace** |
| Per day | floor(6,450 / 7) = floor(921.43) (Ton Q-16) | **฿921/day** |
| Hero detail line | — | "of ฿40,000 · ฿921/day" |
| Spent today | E11 + E12 | ฿112 |
| Alert slot | budget 84% < 90%, so the Bills alert shows | Bills alert (next bill AIS ฿599, 22 Nov) |

### 4.2 Cash, cash flow and net worth
| Figure | Calculation | Shown |
|---|---|---|
| Cash balance | 1,000 + 3,000 − 640 − 65 − 47 | ฿3,248 |
| KBank Savings balance | 30,000 + 52,000 − 3,000 − 12,000 − 1,850 − 5,000 − 6,500 | ฿53,650 |
| KBank Credit owed | 6,500 + (4,200 + 3,030 + 139 + 1,500 + 1,290 + 520 + 2,850 + 419) − 6,500 | ฿13,948 (shown −฿13,948 as a liability) |
| **Total Cash Balance** | 3,248 + 53,650 (cash, bank, e-wallet; no cards) | **฿56,898** |
| **Net Cash Flow** (cycle to date) | In 52,000 − Out 33,550 (T1, T2 excluded) | **+฿18,450** (In +฿52,000 · Out −฿33,550) |
| **Net Worth** | assets 56,898 − liabilities 13,948 | **฿42,950** |
| Available credit | 50,000 − 13,948 | ฿36,052 |
| Credit used | 13,948 / 50,000 = 27.896%, half-up | 28% |

Net Worth leaves out the 8 installment payments not yet charged (฿10,320). This is a dataset assumption for the E10 / E11 contract to confirm (glossary G-5).

### 4.3 Credit card (rule A2, E10-T13)
| Figure | Value |
|---|---|
| Open statement period | 26 Oct – 25 Nov 2026 |
| Statement balance at the 25 Nov cut-off (if nothing else goes on the card) | ฿13,948 |
| Next payment due | **10 Dec 2026** → "Due in 22 days" (strip: "Payment due 10 Dec · in 22 days", "Cut-off 25 Nov") |
| Previous statement | 26 Sep – 25 Oct, ฿6,500, due 10 Nov, paid in full on 10 Nov (T2) |
| Card reminder | "due tomorrow" notification on **9 Dec 2026**; none on 24 Nov |

### 4.4 Fixed costs (cycle 25 Oct – 24 Nov)
| Item | Kind | Day | Account | Amount | State on 18 Nov | Next charge | Reminder date |
|---|---|---|---|---|---|---|---|
| Rent | Bill | 1st | KBank Savings | ฿12,000 | Paid 1 Nov (E2) | 1 Dec | 30 Nov |
| Spotify | Subscription | 3rd | KBank Credit | ฿139 | Paid 3 Nov (E3) | 3 Dec | 2 Dec |
| iPhone 17 Pro | Installment | 10th | KBank Credit | ฿1,290 | Paid 10 Nov (E6) | 10 Dec | 9 Dec |
| Netflix | Subscription | 17th | KBank Credit | ฿419 | Paid 17 Nov (E10) | 17 Dec | 16 Dec |
| AIS mobile | Bill | 22nd | KBank Savings | ฿599 | **Upcoming** | 22 Nov | **21 Nov** |

Totals: ฿14,447 this cycle (subscriptions ฿558 · bills ฿12,599 · installments ฿1,290); paid ฿13,848; remaining ฿599. Reminder dates assume the one-day lead in Ton's approved copy ("due tomorrow"); the E13 plan confirms the lead time.

Installment plan: iPhone 17 Pro, ฿12,900 at 0% over 10 months = ฿1,290 / month, charged to KBank Credit on the 10th from 10 Oct 2026. On 18 Nov: **"2 of 10"** paid, next 10 Dec 2026, last payment **10 Jul 2027**, remaining ฿10,320 (8 × 1,290). Each monthly charge is the expense; the ฿12,900 purchase is never expensed in one go (dataset assumption for the E11 contract).

### 4.5 Month-end forecast (Ton Q-47; **line totals provisional until Q-51**)
Horizon = the current cycle end, **24 Nov 2026** ("Balance on 24 Nov").
| Line | Rule | Amount |
|---|---|---|
| Cash & bank | Total Cash Balance now | ฿56,898 |
| Income | income dated 19–24 Nov; the 25 Nov salary is the next cycle, so it is excluded | ฿0 |
| Fixed bills | bills paid from cash or bank, due 19–24 Nov: AIS on 22 Nov (card-charged bills reach cash only at the card payment) | −฿599 |
| Card payments | card payments due 19–24 Nov; KBank Credit is due 10 Dec, outside the horizon | ฿0 |
| Daily spending | "฿921/day × 7 days" (same per day and days left as Home); amount = left to spend | −฿6,450 |
| **Balance on 24 Nov** | 56,898 + 0 − 599 − 0 − 6,450 | **฿49,849 · On track** |

Open in Q-51: (a) the daily-spending amount is ฿6,450 (left to spend) or ฿6,447 (921 × 7); (b) AIS ฿599 also comes out of the same ฿6,450 budget once paid, so the lines may count it twice. If (b) is "count once", the balance would be ฿50,448.

## 5. Other dates in the same dataset
| Scenario | Inputs | Result |
|---|---|---|
| Last day of the cycle | 24 Nov 2026; AIS ฿599 paid 22 Nov, nothing else spent | Left ฿5,851 · **"1 day left"** · ฿5,851/day · 85% · On track — see note |
| First day of the next cycle | 25 Nov 2026, salary +฿52,000 received, nothing spent | Cycle 25 Nov – 24 Dec (30 days) · Left ฿40,000 · 0% · **"30 days left"** · **฿1,333/day** · On track |
| No payday set (1st-of-month cycle), 18 Nov | Same Nov expenses on a 1–30 Nov cycle: E2–E14 = ฿29,350 | Left ฿10,650 · 73% (73.375%) · 13 days left · ฿819/day · elapsed 18 / 30 = 60% → Over pace · forecast horizon 30 Nov |

Note on the first row: spent 33,550 + 599 = 34,149, so budget % = 85.37% → **85%** (half-up). Days left 1, per day floor(5,851 / 1) = ฿5,851. Elapsed 31 / 31 = 100% → On track (85% ≤ 100%).

## 6. Payday clamping (Ton Q-15)
| Payday rule | Cycle | Days |
|---|---|---|
| 31st | 31 Jan 2027 – 27 Feb 2027 (Feb payday clamps to 28 Feb) | 28 |
| 31st | 28 Feb 2027 – 30 Mar 2027 | 31 |
| 31st | 31 Mar 2027 – 29 Apr 2027 (Apr payday clamps to 30 Apr) | 30 |
| 31st, leap year | 31 Jan 2028 – 28 Feb 2028 (Feb payday 29 Feb) | 29 |
| 30th | 30 Jan 2027 – 27 Feb 2027 | 29 |
| 30th | 28 Feb 2027 – 29 Mar 2027 (Mar payday stays 30 Mar) | 30 |
| 29th | 29 Jan 2027 – 27 Feb 2027 | 30 |
| Last day of the month | 31 Jan 2027 – 27 Feb 2027, then 28 Feb – 30 Mar 2027 | 28, 31 |

Payday 31 and "Last day of the month" give the same dates in every month. They differ only in the label the user chose ("31st" vs "Last day"); see glossary G-6.

Example: payday 31, today 15 Feb 2027 → cycle 31 Jan – 27 Feb 2027, days left (27 − 15) + 1 = **13**.

## 7. Masked and empty variants
- Privacy Mode on: every amount above reads `฿••••••`; counts ("7 days left", "2 of 10", "17 entries", "84%") stay visible. Whether the budget % is masked is decided in E06.
- New user (O5 budget ฿40,000, payday 25, onboarding finished 18 Nov): Left ฿40,000 · 0% · 7 days left · ฿5,714/day · On track · Wallet holds Cash ฿0.

## 8. Reconciliation checks (all pass)
- Expenses: category totals = ฿33,550 = sum of E1–E14.
- Accounts: 3,248 + 53,650 − 13,948 = ฿42,950 = Net Worth; opening worth 1,000 + 30,000 − 6,500 = 24,500, + Net Cash Flow 18,450 = 42,950 ✓ (transfers move value between accounts only).
- Card: 13,948 = statement-to-date charges (4,200 + 3,030 + 139 + 1,500 + 1,290 + 520 + 2,850 + 419).
- Fixed costs: 12,000 + 139 + 1,290 + 419 + 599 = ฿14,447.
- Forecast: 56,898 − 599 − 6,450 = ฿49,849.

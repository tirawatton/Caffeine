# Glossary (EN / TH)

Author: `ba` · 2026-11-21 · **Revision 3** (Ton's answers Q-54 to Q-58, decisions file Part 5: every fixed-cost kind set aside, Mark paid variance, negative Left to spend, Overdue, **"Fixed costs" in the UI / "Commitments" internal only**; revision 2: naming and glossary review, Q-51, Q-52, Q-53)
**Thai column:** cells marked **(Ton)** are Ton's approved wording (21 Nov 2026), kept short for the Bento cards. Every other Thai cell is still **draft — Ton to review**. Whether Thai ships in V1.0 is still Q-19.

One name per concept, used in UI copy, specs, plans, contracts and tests. The worked numbers come from `docs/plan/golden-sample-data.md` (today 18 Nov 2026, payday 25th, Nov cycle 25 Oct – 24 Nov).

## 0. Naming locks (Ton, 21 Nov 2026)
| Lock | Use | Never use |
|---|---|---|
| G-7 | **Debts** (paired with **Assets**) for what is owed on credit cards in Net Worth | Liabilities |
| G-8 | **Analytics** as the tab name **and** the screen title | Reports |
| Period | **Cycle** wording for Home, Analytics and the History default ("Nov cycle · 25 Oct – 24 Nov", "vs Oct cycle") | "Nov" alone or "Nov 2026" for a cycle; "vs Oct" (calendar) |
| Q-57 | **Fixed costs** as the user-facing label on every screen (Screen 5, tab copy, onboarding page 3, alerts). **Commitments** only in domain code, contracts, specs and plans | "Commitments" in any UI string |

## 1. The four money figures Ton asked to keep apart
| # | EN term (UI label) | Definition | Formula / source | Golden value | Thai |
|---|---|---|---|---|---|
| G-1 | **Total Cash Balance** (UI: "Total cash & bank") | Money you hold now in cash, bank and e-wallet accounts. Credit cards are never included | sum of balances of Cash, Bank Account and E-Wallet accounts (not archived) | ฿56,898 | ยอดเงินสดและเงินฝากรวม (draft) |
| G-2 | **Net Cash Flow** | What came in minus what went out over a period (the budget cycle by default). Transfers and card payments are excluded | In (income) − Out (expenses) for the period (`CashFlow.totals`) | +฿18,450 for the Nov cycle to date | **กระแสเงินสดสุทธิ (Ton)** |
| G-3 | **Safe to Spend** (EN UI: **"Left to spend"**) | Money genuinely available for discretionary variable spending in this cycle, after every fixed cost still due (or overdue) this cycle. Income never raises it. May be negative: shown as the exact figure with "Bills exceed budget by ฿x" (Ton Q-54) | **Budget − Actual expenses in the cycle − Upcoming & overdue unpaid fixed costs (bills + subscriptions + installments) due in the active cycle** (Ton Q-51 B, Q-55, Q-58; one formula for Home, widget and Forecast) | ฿5,851 (40,000 − 33,550 − 599) | **เงินที่ใช้ได้ (Ton)** |
| G-4 | **Net Worth** | Everything you own minus everything you owe, over accounts with Include in Net Worth on | **Assets** (cash, bank, e-wallet balances) − **Debts** (credit card balances owed) | ฿42,950 | **ความมั่งคั่งสุทธิ (Ton)** |

"Safe to Spend" is the concept name in specs and contracts; the English UI says **"Left to spend"** (Home, Goals, Trips, Profile and, after re-sync, the 9A footnote); the Thai UI says **เงินที่ใช้ได้**.

## 2. Budget and cycle
| EN term | Definition | Formula / source | Thai |
|---|---|---|---|
| Monthly budget | The amount the user plans to spend per budget cycle | set in O5; editing after O5 is Q-44 | งบประมาณรายเดือน (draft) |
| Payday | The day of the month the salary arrives; it starts the budget cycle | `cycleStartDay` 1–31, or "Last day of the month" (Ton A1, Q-15) | วันเงินเดือนออก (draft) |
| Budget cycle | The period one budget covers: payday to the day before the next payday. **The period for Home, Analytics and the History default** (Ton Q-52) | clamped with the shared clamp (§4a); default 1st when no payday is set | รอบงบประมาณ (draft) |
| Cycle label | Names a cycle by its **closing month** (the month of its last day) plus its dates | "Nov cycle · 25 Oct – 24 Nov" (Caption Upper `NOV CYCLE · 25 OCT – 24 NOV`); 1st-of-month cycle "Nov cycle · 1 Nov – 30 Nov"; across a year "Jan cycle · 25 Dec – 24 Jan" | draft — Ton to review |
| vs prev cycle | Comparison with the previous cycle | "vs Oct cycle"; short form "vs prev cycle" where the month does not fit (Ton Q-52) | draft — Ton to review |
| Calendar month (History filter) | A secondary History filter for tax and calendar lookups (1st – last day of a month). Never used by Home, Analytics or the budget | "November 2026" → ฿29,350 out in the golden set | draft — Ton to review |
| Set aside (internal: **Reserved**) | Every unpaid fixed cost of every kind (bill, subscription, installment), whatever the paying account, whose charge date falls in the active cycle, from day one of the cycle; overdue ones stay set aside until Mark paid or Skip this cycle (Ton Q-55, Q-58). Taken out of Safe to Spend, not out of Budget % | AIS ฿599 due 22 Nov in the golden set; Dec cycle ฿14,447 (all 5) | draft — Ton to review |
| Overdue | Badge on an unpaid fixed cost after its due date; it stays set aside (Ton Q-58). Colour: `night/accent` coral + icon + label (Q-59 to confirm) | AIS on 23 Nov | draft — Ton to review |
| Bills exceed budget | Hero helper text when Safe to Spend is negative and spent is still within budget (Ton Q-54) | "Bills exceed budget by ฿399" | draft — Ton to review |
| Days left | Days remaining in the cycle, today included | (cycle end − today) + 1; "7 days left", last day "1 day left" (Ton Q-48) | เหลืออีก 7 วัน / เหลืออีก 1 วัน (draft) |
| **Per day left** | How much can be spent each remaining day; a **display pacing guide only** (never multiplied back into an amount) | max(0, floor(Safe to Spend / Days left)) (Ton Q-16, Q-51 A, Q-54): ฿835/day; ฿0/day when Safe to Spend is ≤ 0 | **ใช้ได้วันละ (Ton)** (e.g. "ใช้ได้วันละ ฿835") |
| Budget % (used) | Share of the budget actually spent (set-aside fixed costs not included) | spent / budget, half-up, 99% rule (Ton Q-16): 84% | ใช้ไปแล้ว (draft) |
| On track | Spending is at or below the time elapsed | % used ≤ elapsed | เป็นไปตามแผน (draft) |
| Over pace | Spending is ahead of the time elapsed, still within budget | elapsed < % used ≤ 100% | ใช้เร็วกว่าแผน (draft) |
| Over budget | Spending is above the budget | % used > 100%; caption "Over budget by ฿x" | เกินงบ (draft) |
| No budget | No monthly budget is set; Home shows Net Cash Flow instead | — | ยังไม่ตั้งงบ (draft) |

## 3. Transactions
| EN term | Definition | Thai |
|---|---|---|
| Expense | Money out; counts in Out and against the budget; amount shown −฿, coral | รายจ่าย (draft) |
| Income | Money in; counts in In, never changes Left to spend; shown +฿, `night/income-text` | รายรับ (draft) |
| Transfer | Money moved between your own accounts; never in In / Out / Net or budgets | โอนระหว่างบัญชี (draft) |
| Card payment | A transfer that pays a credit card; never in In / Out / Net or budgets | ชำระบัตรเครดิต (draft) |
| Category | Expense or income group (seed list in `caffeine-domain`) | หมวดหมู่ (draft) |
| Memo | The user's free-text note (Restricted data) | บันทึก (draft) |
| E-slip | A bank transfer slip image with a QR code | สลิปโอนเงิน (draft) |
| From slip / Suggested | Field tags: read from the slip / inferred by the app | จากสลิป / แนะนำ (draft) |

## 4. Accounts and cards
| EN term | Definition | Thai |
|---|---|---|
| Account | Cash, Bank Account, Credit Card or E-Wallet | บัญชี (draft) |
| **Assets** | Balances of cash, bank and e-wallet accounts with Include in Net Worth on | **ทรัพย์สิน (Ton)** |
| **Debts** | What is owed on credit cards (locked, G-7; replaces "Liabilities") | **หนี้สิน (Ton)** |
| Statement cut-off date | The day a card statement closes; shown only as the statement date (Ton A2); days 29–31 clamp (Ton Q-53) | วันตัดรอบบัญชี (draft) |
| Payment due date | The day the card payment is due; drives the due badge, reminders and forecast (Ton A2); days 29–31 clamp (Ton Q-53) | วันครบกำหนดชำระ (draft) |
| Available credit | credit limit − balance owed | วงเงินคงเหลือ (draft) |
| **Reconcile / Adjust Balance** | Set an account's balance to the real one; the difference is an adjustment, never counted in budgets or In / Out | **ปรับยอดให้ตรงบัญชี (Ton)** |

## 4a. Month-day clamping (Ton Q-15, Q-53)
| EN term | Definition | Formula |
|---|---|---|
| Clamped day | The day a "day N of the month" rule falls on in a given month | `min(N, daysInMonth)`; always snaps back (31 → 28 Feb / 29 Feb in a leap year / 30 Apr), never rolls into the next month; the stored N never changes. One shared function for payday, recurring commitments and card cut-off / due days |

## 5. Fixed costs and forecast
| EN term | Definition | Thai |
|---|---|---|
| **Fixed costs** | **The user-facing label on every screen** (Ton Q-57): Screen 5 and its list of recurring bills, subscriptions and installments, tab copy, onboarding page 3, alerts | ค่าใช้จ่ายประจำ (draft; Q-62) |
| **Commitments** | **Internal domain / engineering term only** (Ton Q-57): the concept and contract name for every recurring charge the user has committed to (bills, subscriptions, installments), e.g. `Commitments.unpaidDueInCycle`. Never shown in the UI | **รายการประจำ / บิลล่วงหน้า (Ton)**; whether this becomes the Thai UI label for Fixed costs: Q-62 |
| Subscription | A recurring service charge (e.g. Netflix) | ค่าสมาชิกรายเดือน (draft) |
| **Installments** | Purchases paid in equal monthly charges; "2 of 10" = 2 paid | **รายการผ่อนชำระ (Ton)** |
| Mark paid | Confirm a fixed cost was paid; creates the linked expense (Ton Q-21) and moves it from Reserved to Actual. Left to spend changes only by Scheduled − Actual paid (Ton Q-56, supersedes the Q-21 wording): AIS ฿599 paid ฿599 → ฿5,851, ฿650 → ฿5,800, ฿500 → ฿5,950 | ทำเครื่องหมายว่าจ่ายแล้ว (draft) |
| Skip this cycle | Release a fixed cost for the current cycle without an expense; it stops being set aside (Ton Q-58) | draft — Ton to review |
| Month-end forecast | Expected Total Cash Balance on the **current cycle end date** (Ton Q-47); daily-spending line amount = exact Safe to Spend (Ton Q-51 A) | คาดการณ์ยอดเงินสิ้นรอบ (draft) |
| Shortfall | The forecast balance is below ฿0 | เงินไม่พอ (draft) |

## 6. App
| EN term | Definition | Thai |
|---|---|---|
| Analytics | The tab and its screen (Spending, Cash Flow, Trends); locked G-8 | draft — Ton to review |
| Privacy Mode | Masks every amount as `฿••••••` | โหมดซ่อนยอดเงิน (draft) |
| App Lock | Face ID / fingerprint / passcode before the app opens | ล็อกแอป (draft) |
| Backup | Client-encrypted snapshot in iCloud Drive (iOS) or Google Drive app data (Android) | สำรองข้อมูล (draft) |
| Space | V2.0 only (Personal / shared household); V1.0 has the Personal space only | พื้นที่ (draft) |

## 7. Naming decisions
| # | Item | Status |
|---|---|---|
| G-5 | Does Net Worth include installment payments not yet charged (golden: ฿10,320 left out)? Does Total Cash Balance include accounts with Include in Net Worth off? | Open: backend-lead in the E10 / E11 contract, Ton if it changes the meaning |
| G-6 | Payday 31 and "Last day of the month" give identical dates; one stored rule with two labels, or two rules? | Open: backend-lead (E00 T-02 stores both) |
| G-7 | "Debts" vs "Liabilities" | **Locked by Ton 21 Nov: Debts** (with Assets) |
| G-8 | Tab "Analytics" vs screen title "Reports" | **Locked by Ton 21 Nov: Analytics** |
| G-9 | Shared space names: Family / Household / Shared / Family split / Household wallet | Open: Ton, before E22 (V2.0) |
| G-10 | User name "Ton Raweephat" vs "Raweephat S."; partner Nui vs Fon. This sheet uses "Ton Raweephat" | ux-ui-designer re-sync |
| G-11 | "Commitments" (Ton's Thai label) vs the screen name "Fixed costs" | **Locked by Ton 21 Nov (Q-57): "Fixed costs" in the UI, "Commitments" internal only.** Thai UI label for Fixed costs: open, **Q-62** |

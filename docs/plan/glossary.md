# Glossary (EN / TH) — draft for the next handoff package

Author: `ba` · 2026-11-21 · Status: **draft** · Decision: Ton, audit findings 13–15 (`docs/decisions/2026-11-21-ton-answers.md` Part 3)
**Thai column: draft — Ton to review.** Nothing in the Thai column is approved copy until Ton signs it off (Q-19 V1 languages is still open).

One name per concept, used in UI copy, specs, plans, contracts and tests. The worked numbers come from `docs/plan/golden-sample-data.md` (today 18 Nov 2026, payday 25th, cycle 25 Oct – 24 Nov).

## 1. The four money figures Ton asked to keep apart
| # | EN term (UI label) | Definition | Formula / source | Golden value | Thai (draft — Ton to review) |
|---|---|---|---|---|---|
| G-1 | **Total Cash Balance** (UI: "Total cash & bank") | Money you hold now in cash, bank and e-wallet accounts. Credit cards are never included | sum of balances of Cash, Bank Account and E-Wallet accounts (not archived) | ฿56,898 | ยอดเงินสดและเงินฝากรวม |
| G-2 | **Net Cash Flow** | What came in minus what went out over a period. Transfers and card payments are excluded | In (income) − Out (expenses) for the period (`CashFlow.totals`) | +฿18,450 for the cycle to date | กระแสเงินสดสุทธิ |
| G-3 | **Safe to Spend** (UI: **"Left to spend"**) | How much of this cycle's budget is still unspent. Income never raises it | monthly budget − expenses in the current budget cycle | ฿6,450 | เหลือใช้ได้ |
| G-4 | **Net Worth** | Everything you own minus everything you owe, over accounts with Include in Net Worth on | assets (cash, bank, e-wallet balances) − liabilities (credit card balances owed) | ฿42,950 | ความมั่งคั่งสุทธิ |

"Safe to Spend" is the concept name in specs and contracts; the UI always says **"Left to spend"** (Home, Goals, Trips, Profile and, after re-sync, the 9A footnote).

## 2. Budget and cycle
| EN term | Definition | Formula / source | Thai (draft — Ton to review) |
|---|---|---|---|
| Monthly budget | The amount the user plans to spend per budget cycle | set in O5; editing after O5 is Q-44 | งบประมาณรายเดือน |
| Payday | The day of the month the salary arrives; it starts the budget cycle | `cycleStartDay` 1–31, or "Last day of the month" (Ton A1, Q-15) | วันเงินเดือนออก |
| Budget cycle | The period one budget covers: payday to the day before the next payday | clamped to short months (Ton Q-15); default 1st when no payday is set | รอบงบประมาณ |
| Days left | Days remaining in the cycle, today included | (cycle end − today) + 1; "7 days left", last day "1 day left" (Ton Q-48) | เหลืออีก 7 วัน / เหลืออีก 1 วัน |
| Per day | How much can be spent each remaining day | floor(Left to spend / Days left), ฿0 when nothing is left (Ton Q-16) | ต่อวัน |
| Budget % (used) | Share of the budget spent | spent / budget, half-up, 99% rule (Ton Q-16) | ใช้ไปแล้ว |
| On track | Spending is at or below the time elapsed | % used ≤ elapsed | เป็นไปตามแผน |
| Over pace | Spending is ahead of the time elapsed, still within budget | elapsed < % used ≤ 100% | ใช้เร็วกว่าแผน |
| Over budget | Spending is above the budget | % used > 100%; caption "Over budget by ฿x" | เกินงบ |
| No budget | No monthly budget is set; Home shows Net Cash Flow instead | — | ยังไม่ตั้งงบ |

## 3. Transactions
| EN term | Definition | Thai (draft — Ton to review) |
|---|---|---|
| Expense | Money out; counts in Out and against the budget; amount shown −฿, coral | รายจ่าย |
| Income | Money in; counts in In, never changes Left to spend; shown +฿, `night/income-text` | รายรับ |
| Transfer | Money moved between your own accounts; never in In / Out / Net or budgets | โอนระหว่างบัญชี |
| Card payment | A transfer that pays a credit card; never in In / Out / Net or budgets | ชำระบัตรเครดิต |
| Category | Expense or income group (seed list in `caffeine-domain`) | หมวดหมู่ |
| Memo | The user's free-text note (Restricted data) | บันทึก |
| E-slip | A bank transfer slip image with a QR code | สลิปโอนเงิน |
| From slip / Suggested | Field tags: read from the slip / inferred by the app | จากสลิป / แนะนำ |

## 4. Accounts and cards
| EN term | Definition | Thai (draft — Ton to review) |
|---|---|---|
| Account | Cash, Bank Account, Credit Card or E-Wallet | บัญชี |
| Statement cut-off date | The day a card statement closes; shown only as the statement date (Ton A2) | วันตัดรอบบัญชี |
| Payment due date | The day the card payment is due; drives the due badge, reminders and forecast (Ton A2) | วันครบกำหนดชำระ |
| Available credit | credit limit − balance owed | วงเงินคงเหลือ |
| Liabilities | What is owed on credit cards (draft term; "Debts" vs "Liabilities" is G-7, Ton to decide) | หนี้สิน |

## 5. Fixed costs and forecast
| EN term | Definition | Thai (draft — Ton to review) |
|---|---|---|
| Fixed costs | Recurring bills, subscriptions and installments | ค่าใช้จ่ายประจำ |
| Subscription | A recurring service charge (e.g. Netflix) | ค่าสมาชิกรายเดือน |
| Installment | A purchase paid in equal monthly charges; "2 of 10" = 2 paid | ผ่อนชำระ (ผ่อน 0%) |
| Mark paid | Confirm a bill was paid; creates the linked expense (Ton Q-21) | ทำเครื่องหมายว่าจ่ายแล้ว |
| Month-end forecast | Expected Total Cash Balance on the **current cycle end date** (Ton Q-47) | คาดการณ์ยอดเงินสิ้นรอบ |
| Shortfall | The forecast balance is below ฿0 | เงินไม่พอ |

## 6. App
| EN term | Definition | Thai (draft — Ton to review) |
|---|---|---|
| Privacy Mode | Masks every amount as `฿••••••` | โหมดซ่อนยอดเงิน |
| App Lock | Face ID / fingerprint / passcode before the app opens | ล็อกแอป |
| Backup | Client-encrypted snapshot in iCloud Drive (iOS) or Google Drive app data (Android) | สำรองข้อมูล |
| Space | V2.0 only (Personal / shared household); V1.0 has the Personal space only | พื้นที่ |

## 7. Naming decisions still needed (audit 15; not guessed)
| # | Conflict in Figma | Needed from |
|---|---|---|
| G-5 | Does Net Worth include installment payments not yet charged (golden: ฿10,320 left out)? Does Total Cash Balance include accounts with Include in Net Worth off? | backend-lead in the E10 / E11 contract, Ton if it changes the meaning |
| G-6 | Payday 31 and "Last day of the month" give identical dates; is it one stored rule with two labels, or two rules? | backend-lead (E00 T-02 stores both, see foundation plan) |
| G-7 | 4D shows both "Debts" and "Liabilities"; this draft uses **Liabilities** | Ton |
| G-8 | Tab "Analytics" vs screen title "Reports" | Ton (asked in the E12 plan) |
| G-9 | Shared space names: Family / Household / Shared / Family split / Household wallet | Ton, before E22 (V2.0) |
| G-10 | User name "Ton Raweephat" vs "Raweephat S."; partner Nui vs Fon. This draft uses "Ton Raweephat"; the partner name matters only in V2.0 | ux-ui-designer re-sync |

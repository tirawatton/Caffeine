-- DRY RUN queries (local-data-engineer, 21 Nov 2026). Expected values = docs/plan/golden-sample-data.md §3-§4.
-- Run: python3 -I scripts/data/verify_queries.py docs/data-model/sql/dryrun/ledger-draft-schema.sql docs/data-model/sql/fixtures/golden.sql docs/data-model/sql/dryrun/ledger-draft-queries.sql

-- name: cycle_expenses
-- purpose: Home Budget hero "Spent" and Left to spend (budget - spent). Golden §4.1.
-- params: {"start": "2026-10-25", "end": "2026-11-24"}
-- expect: count = 14
-- expect: sum(amount) = 33550
SELECT t.id, t.amount
FROM transactions t
WHERE t.type = 'expense'
  AND t.localDate BETWEEN :start AND :end;

-- name: spent_on_day
-- purpose: "Spent today" for the spend wave. Golden §4.1.
-- params: {"day": "2026-11-18"}
-- expect: count = 2
-- expect: sum(amount) = 112
SELECT t.id, t.amount
FROM transactions t
WHERE t.type = 'expense'
  AND t.localDate = :day;

-- name: spent_by_category
-- purpose: Analytics Spending list. Golden §3 category totals.
-- params: {"start": "2026-10-25", "end": "2026-11-24"}
-- expect: sum(amount) by categoryName = {"Bills & Utilities": "13850", "Food & Drink": "12115", "Shopping": "4320", "Transport": "1547", "Health": "640", "Subscriptions": "558", "Entertainment": "520"}
SELECT c.name AS categoryName, t.amount
FROM transactions t
JOIN categories c ON c.id = t.categoryId
WHERE t.type = 'expense'
  AND t.localDate BETWEEN :start AND :end
ORDER BY c.sortOrder;

-- name: cash_flow_in_out
-- purpose: Cash flow statement In / Out / Net; transfers and card payments never count. Golden §4.2.
-- params: {"start": "2026-10-25", "end": "2026-11-24"}
-- expect: sum(amount) by type = {"income": "52000", "expense": "33550"}
-- expect: sum(signedAmount) = 18450
SELECT t.type,
       t.amount,
       CASE t.type WHEN 'expense' THEN '-' || t.amount ELSE t.amount END AS signedAmount
FROM transactions t
WHERE t.type IN ('income', 'expense')
  AND t.localDate BETWEEN :start AND :end;

-- name: account_balances
-- purpose: Wallet balances. Opening + money in - money out +/- transfers, up to a date. Golden §4.2.
-- params: {"asOf": "2026-11-18"}
-- expect: sum(delta) by accountName = {"Cash": "3248", "KBank Savings": "53650", "KBank Credit": "-13948"}
-- expect: sum(delta) = 42950
-- allow-scan: a balance needs every row up to asOf; idx_tx_localDate is used for the date bound where SQLite chooses it
WITH movements AS (
  SELECT a.id AS accountId, a.openingBalance AS delta
  FROM accounts a
  UNION ALL
  SELECT t.accountId,
         CASE t.type WHEN 'income' THEN t.amount ELSE '-' || t.amount END
  FROM transactions t
  WHERE t.localDate <= :asOf
  UNION ALL
  SELECT t.toAccountId, t.amount
  FROM transactions t
  WHERE t.type = 'transfer' AND t.localDate <= :asOf
)
SELECT a.name AS accountName, a.type AS accountType, m.delta
FROM movements m
JOIN accounts a ON a.id = m.accountId
WHERE a.isHidden = 0;

-- name: net_worth_sections
-- purpose: Net worth statement: assets (cash, bank, e-wallet) vs liabilities (cards). Golden §4.2.
-- params: {"asOf": "2026-11-18"}
-- expect: sum(delta) by section = {"assets": "56898", "liabilities": "-13948"}
-- expect: sum(delta) = 42950
-- allow-scan: same as account_balances
WITH movements AS (
  SELECT a.id AS accountId, a.openingBalance AS delta FROM accounts a
  UNION ALL
  SELECT t.accountId, CASE t.type WHEN 'income' THEN t.amount ELSE '-' || t.amount END
  FROM transactions t WHERE t.localDate <= :asOf
  UNION ALL
  SELECT t.toAccountId, t.amount
  FROM transactions t WHERE t.type = 'transfer' AND t.localDate <= :asOf
)
SELECT CASE a.type WHEN 'credit_card' THEN 'liabilities' ELSE 'assets' END AS section,
       a.name AS accountName, m.delta
FROM movements m
JOIN accounts a ON a.id = m.accountId
WHERE a.includeInNetWorth = 1;

-- name: transfers_net_zero
-- purpose: Tie-out: transfers move value between accounts only, so their legs sum to 0. Golden §8.
-- params: {"start": "2026-10-25", "end": "2026-11-24"}
-- expect: count = 4
-- expect: sum(leg) = 0
SELECT t.id, '-' || t.amount AS leg FROM transactions t
WHERE t.type = 'transfer' AND t.localDate BETWEEN :start AND :end
UNION ALL
SELECT t.id, t.amount FROM transactions t
WHERE t.type = 'transfer' AND t.localDate BETWEEN :start AND :end;

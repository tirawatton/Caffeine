-- Golden sample data (docs/plan/golden-sample-data.md, 21 Nov 2026) as rows.
-- Readable ids instead of uuids, fixture only. Today = 18 Nov 2026, Asia/Bangkok.
-- Times are 09:00 Bangkok = 02:00 UTC.

INSERT INTO accounts (id, name, type, openingBalance, creditLimit, statementCutoffDay, paymentDueDay, createdAt) VALUES
 ('acc-cash',    'Cash',          'cash',        '1000',  NULL,    NULL, NULL, strftime('%s','2026-10-24 02:00:00')*1000),
 ('acc-savings', 'KBank Savings', 'bank',        '30000', NULL,    NULL, NULL, strftime('%s','2026-10-24 02:00:00')*1000),
 ('acc-credit',  'KBank Credit',  'credit_card', '-6500', '50000', 25,   10,   strftime('%s','2026-10-24 02:00:00')*1000);

INSERT INTO categories (id, name, kind, isSeed, sortOrder) VALUES
 ('cat-food','Food & Drink','expense',1,1), ('cat-transport','Transport','expense',1,2),
 ('cat-bills','Bills & Utilities','expense',1,3), ('cat-shopping','Shopping','expense',1,4),
 ('cat-health','Health','expense',1,5), ('cat-entertainment','Entertainment','expense',1,6),
 ('cat-subscriptions','Subscriptions','expense',1,7), ('cat-other','Other','expense',1,8),
 ('cat-salary','Salary','income',1,1);

INSERT INTO transactions (id, type, amount, categoryId, accountId, toAccountId, isCardPayment, localDate, memo, occurredAt, createdAt)
SELECT id, type, amount, categoryId, accountId, toAccountId, isCardPayment, localDate, memo,
       strftime('%s', localDate || ' 02:00:00')*1000, strftime('%s', localDate || ' 02:00:00')*1000
FROM (
 SELECT 'I1' id,'income' type,'52000' amount,'cat-salary' categoryId,'acc-savings' accountId,NULL toAccountId,0 isCardPayment,'2026-10-25' localDate,'Monthly salary' memo
 UNION ALL SELECT 'T1','transfer','3000',NULL,'acc-savings','acc-cash',0,'2026-10-26','ATM withdrawal'
 UNION ALL SELECT 'E1','expense','4200','cat-food','acc-credit',NULL,0,'2026-10-26','Makro groceries'
 UNION ALL SELECT 'E2','expense','12000','cat-bills','acc-savings',NULL,0,'2026-11-01','Rent'
 UNION ALL SELECT 'E13','expense','3030','cat-shopping','acc-credit',NULL,0,'2026-11-02','Uniqlo'
 UNION ALL SELECT 'E3','expense','139','cat-subscriptions','acc-credit',NULL,0,'2026-11-03','Spotify'
 UNION ALL SELECT 'E4','expense','1850','cat-bills','acc-savings',NULL,0,'2026-11-05','Electricity (MEA)'
 UNION ALL SELECT 'E5','expense','1500','cat-transport','acc-credit',NULL,0,'2026-11-08','PTT fuel'
 UNION ALL SELECT 'E14','expense','5000','cat-food','acc-savings',NULL,0,'2026-11-09','Tops Market'
 UNION ALL SELECT 'T2','transfer','6500',NULL,'acc-savings','acc-credit',1,'2026-11-10','Pay KBank Credit statement'
 UNION ALL SELECT 'E6','expense','1290','cat-shopping','acc-credit',NULL,0,'2026-11-10','iPhone 17 Pro installment 2 of 10'
 UNION ALL SELECT 'E7','expense','640','cat-health','acc-cash',NULL,0,'2026-11-12','Pharmacy'
 UNION ALL SELECT 'E8','expense','520','cat-entertainment','acc-credit',NULL,0,'2026-11-14','Cinema'
 UNION ALL SELECT 'E9','expense','2850','cat-food','acc-credit',NULL,0,'2026-11-15','Restaurant dinner'
 UNION ALL SELECT 'E10','expense','419','cat-subscriptions','acc-credit',NULL,0,'2026-11-17','Netflix'
 UNION ALL SELECT 'E11','expense','65','cat-food','acc-cash',NULL,0,'2026-11-18','Iced latte, Cafe Amazon'
 UNION ALL SELECT 'E12','expense','47','cat-transport','acc-cash',NULL,0,'2026-11-18','BTS Asok - Siam'
);

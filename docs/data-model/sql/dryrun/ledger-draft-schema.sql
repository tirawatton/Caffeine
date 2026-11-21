-- DRY RUN of local-data-engineer (21 Nov 2026). NOT a contract.
-- Core ledger tables, drafted to test the agent against docs/plan/golden-sample-data.md.
-- backend-lead turns the real version into docs/data-model/<feature>-model.md.
-- SQLite = the Room engine. Money is TEXT decimal (BigDecimal.toPlainString), never REAL.

CREATE TABLE accounts (
  id                 TEXT PRIMARY KEY NOT NULL,         -- uuid
  name               TEXT NOT NULL,
  type               TEXT NOT NULL CHECK (type IN ('cash','bank','ewallet','credit_card')),
  currencyCode       TEXT NOT NULL DEFAULT 'THB',
  openingBalance     TEXT NOT NULL DEFAULT '0',         -- signed; a card that owes 6,500 opens at -6500
  creditLimit        TEXT,                              -- credit_card only
  statementCutoffDay INTEGER,                           -- credit_card only, 1-31
  paymentDueDay      INTEGER,                           -- credit_card only, 1-31
  includeInNetWorth  INTEGER NOT NULL DEFAULT 1,
  isHidden           INTEGER NOT NULL DEFAULT 0,
  createdAt          INTEGER NOT NULL                   -- epoch ms UTC
);

CREATE TABLE categories (
  id        TEXT PRIMARY KEY NOT NULL,
  name      TEXT NOT NULL,
  kind      TEXT NOT NULL CHECK (kind IN ('expense','income')),
  isSeed    INTEGER NOT NULL DEFAULT 0,
  isHidden  INTEGER NOT NULL DEFAULT 0,
  sortOrder INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE transactions (
  id           TEXT PRIMARY KEY NOT NULL,
  type         TEXT NOT NULL CHECK (type IN ('expense','income','transfer')),
  amount       TEXT NOT NULL,                           -- always > 0; the sign comes from type
  currencyCode TEXT NOT NULL DEFAULT 'THB',
  categoryId   TEXT REFERENCES categories(id),          -- required for expense / income
  accountId    TEXT NOT NULL REFERENCES accounts(id),   -- expense/income account, or transfer "from"
  toAccountId  TEXT REFERENCES accounts(id),            -- transfer "to" only
  isCardPayment INTEGER NOT NULL DEFAULT 0,
  occurredAt   INTEGER NOT NULL,                        -- epoch ms UTC (the instant)
  localDate    TEXT NOT NULL,                           -- 'YYYY-MM-DD' in Asia/Bangkok at entry; all cycle maths use this
  memo         TEXT,                                    -- Confidential
  createdAt    INTEGER NOT NULL
);

CREATE INDEX idx_tx_localDate        ON transactions(localDate);
CREATE INDEX idx_tx_type_localDate   ON transactions(type, localDate);
CREATE INDEX idx_tx_account          ON transactions(accountId);
CREATE INDEX idx_tx_toAccount        ON transactions(toAccountId);
CREATE INDEX idx_tx_category         ON transactions(categoryId);

#!/usr/bin/env python3
"""Caffeine local-data gate (owner: local-data-engineer).

Loads a SQLite schema (the same engine Room uses), a fixture, then runs every
named query in a queries file and checks its `-- expect:` lines.

Money never gets summed in SQL. SQL filters, joins and orders rows; the
"reduce" step (sum by a key) runs here with Python Decimal, the same way the
repositories do it with Swift Decimal / Kotlin BigDecimal.

Usage:
  python3 -I scripts/data/verify_queries.py SCHEMA.sql FIXTURE.sql QUERIES.sql [QUERIES2.sql ...]

Query block format (blocks start at a `-- name:` line):
  -- name: spent_by_category
  -- purpose: Analytics Spending list and donut          (free text)
  -- params: {"start": "2026-10-25", "end": "2026-11-24"}
  -- expect: count = 14
  -- expect: sum(amount) = 33550
  -- expect: sum(amount) by categoryName = {"Food & Drink": "12115"}
  -- allow-scan: balances need the whole ledger         (optional)
  SELECT ...;

Exit 0 = all PASS. Exit 1 = a FAIL. Full-table SCANs on `transactions`
without an allow-scan reason are reported as FAIL (index missing).
Also fails on: SELECT *, SUM/AVG/TOTAL in SQL, REAL/FLOAT/DOUBLE columns.
"""
import json
import re
import sqlite3
import sys
from decimal import Decimal, ROUND_HALF_UP

EXPECT_SUM = re.compile(r"^sum\((\w+)\)(?:\s+by\s+(\w+))?\s*=\s*(.+)$")
EXPECT_COUNT = re.compile(r"^count\s*=\s*(\d+)$")


def money(v):
    return Decimal(str(v)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def parse_blocks(text):
    blocks, cur = [], None
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("-- name:"):
            cur = {"name": s.split(":", 1)[1].strip(), "params": {}, "expects": [],
                   "allow_scan": None, "sql": []}
            blocks.append(cur)
        elif cur is None:
            continue
        elif s.startswith("-- params:"):
            cur["params"] = json.loads(s.split(":", 1)[1])
        elif s.startswith("-- expect:"):
            cur["expects"].append(s.split(":", 1)[1].strip())
        elif s.startswith("-- allow-scan:"):
            cur["allow_scan"] = s.split(":", 1)[1].strip()
        elif s.startswith("--"):
            continue
        else:
            cur["sql"].append(line)
    for b in blocks:
        b["sql"] = "\n".join(b["sql"]).strip().rstrip(";")
    return blocks


def strip_comments(sql):
    return re.sub(r"--[^\n]*", "", sql)


def static_checks(schema, blocks):
    fails = []
    if re.search(r"\b(REAL|FLOAT|DOUBLE)\b", strip_comments(schema), re.I):
        fails.append("schema: REAL/FLOAT/DOUBLE column found (money must be TEXT decimal)")
    for b in blocks:
        sql = b["sql"]
        if re.search(r"select\s+(\w+\.)?\*", sql, re.I):
            fails.append(f"{b['name']}: SELECT * (name the columns)")
        if re.search(r"\b(SUM|AVG|TOTAL)\s*\(", sql, re.I):
            fails.append(f"{b['name']}: SUM/AVG/TOTAL in SQL (reduce money in code with Decimal)")
        if not b["expects"]:
            fails.append(f"{b['name']}: no -- expect: line")
    return fails


def reduce_rows(rows, col, by):
    if by is None:
        return money(sum((Decimal(str(r[col])) for r in rows), Decimal(0)))
    out = {}
    for r in rows:
        k = r[by]
        out[k] = out.get(k, Decimal(0)) + Decimal(str(r[col]))
    return {k: money(v) for k, v in out.items()}


def check_expect(expect, rows):
    m = EXPECT_COUNT.match(expect)
    if m:
        want, got = int(m.group(1)), len(rows)
        return want == got, f"count want {want} got {got}"
    m = EXPECT_SUM.match(expect)
    if not m:
        return False, f"cannot parse expect '{expect}'"
    col, by, raw = m.group(1), m.group(2), m.group(3).strip()
    if rows and col not in rows[0].keys():
        return False, f"column '{col}' not in result"
    got = reduce_rows(rows, col, by)
    if by is None:
        want = money(raw)
        return want == got, f"sum({col}) want {want} got {got}"
    want = {k: money(v) for k, v in json.loads(raw).items()}
    ok = want == got
    detail = "" if ok else f" want {dict((k, str(v)) for k, v in want.items())} got {dict((k, str(v)) for k, v in got.items())}"
    return ok, f"sum({col}) by {by}{detail}"


def scan_check(con, b):
    plan = con.execute("EXPLAIN QUERY PLAN " + b["sql"], b["params"]).fetchall()
    scans = [p[3] for p in plan if re.match(r"SCAN (transactions|t|tx)\b", p[3])
             and "USING" not in p[3]]
    if scans and not b["allow_scan"]:
        return False, "full scan on transactions: " + "; ".join(scans) + " (add an index or -- allow-scan: reason)"
    return True, "plan ok" + (f" (scan allowed: {b['allow_scan']})" if scans else "")


def main(argv):
    if len(argv) < 4:
        print(__doc__)
        return 2
    schema = open(argv[1], encoding="utf-8").read()
    fixture = open(argv[2], encoding="utf-8").read()
    blocks = []
    for path in argv[3:]:
        blocks += parse_blocks(open(path, encoding="utf-8").read())

    con = sqlite3.connect(":memory:")
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    con.executescript(schema)
    con.executescript(fixture)

    failed = 0
    for f in static_checks(schema, blocks):
        print("FAIL  static  " + f)
        failed += 1
    for b in blocks:
        try:
            rows = con.execute(b["sql"], b["params"]).fetchall()
        except sqlite3.Error as e:
            print(f"FAIL  {b['name']}: SQL error {e}")
            failed += 1
            continue
        ok, msg = scan_check(con, b)
        print(f"{'PASS' if ok else 'FAIL'}  {b['name']}: {msg}")
        failed += 0 if ok else 1
        for ex in b["expects"]:
            ok, msg = check_expect(ex, rows)
            print(f"{'PASS' if ok else 'FAIL'}  {b['name']}: {msg}")
            failed += 0 if ok else 1
    print(f"\n{len(blocks)} queries, {failed} failure(s)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

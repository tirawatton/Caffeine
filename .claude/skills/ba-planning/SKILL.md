---
name: ba-planning
description: How the Caffeine BA writes a developer-ready feature plan - the plan template (need, scope, flow, tasks, Given/When/Then acceptance criteria, screen map, analytics, open questions), task splitting rules, the analytics privacy rules and the 9-point readiness checklist that must pass before PLAN_READY. Loaded by ba.
---

# BA Planning

Question behind every line: *could a developer and a designer build this now without asking anything?*

## Plan file: `docs/plan/<feature>-plan.md`
Start the file with the Readiness checklist (below) as numbered PASS/FAIL lines, then:

1. **Need** – 2–3 sentences (5 Whys). If the ask hides a different need, say so.
2. **Scope** – goal, KPI or "none", platform scope (iOS / Android / Both / iOS solo), priority, non-goals.
3. **Flow** – Mermaid flowchart covering every branch: happy, empty, error, offline, privacy mode.
4. **Tasks** `T-01…` – 8 fields each:
   | Field | Rule |
   |---|---|
   | purpose | one sentence, one purpose |
   | layer | Data / Domain / UI / Platform |
   | what to build | no design or data decision left open |
   | error behaviour | what the user sees, what is stored |
   | depends on | task ids or "none" |
   | platform | iOS / Android / Both |
   | priority | Must / Should / Could |
   | definition of done | at least one test scenario |
   Max half a day each. Split by layer, by happy path vs each error path, and by screen state.
5. **Acceptance criteria** `AC-01…` – 2–4 per task, exact `Given … When … Then …` with concrete values (amounts in THB, dates, strings). At least one error/edge AC per task. Numbers follow `caffeine-domain` (signed amounts, rounding, pace status).
6. **Screen map** – screen state → Feature Journeys step code (H1, 2A, 10B…) → v5.1 Dark / Light node ids (from CLAUDE.md). A state with no frame = **Design gap** (ux-ui-designer designs it).
7. **Analytics** (only if the brief has a KPI) – KPI → metric → events: `snake_case` name, trigger = screen id + intent, properties with allowed values, identical on iOS and Android.
   **Forbidden properties:** amounts, balances, notes, merchant, account numbers, names, slip data. Buckets (`amount_bucket: "0-500"`) only if Ton approves. No KPI → write "N/A — no KPI".
8. **Security** – for each task that creates, shows, stores, sends or exports user data: the data it touches with its class (`security-standard` §2) and at least one security AC (e.g. "Given Privacy Mode is on, When Home opens, Then every amount shows ฿••••••"; "Given a note is saved, When the database file is read, Then the note is ciphertext").
9. **Open questions** – max 3, the most important.

## Readiness checklist (any miss = fix and re-check all)
1. Every task has all 8 fields filled.
2. Every AC starts Given / When / Then, has concrete values, and no vague words (fast, nice, easy, properly, user-friendly, etc.).
3. Every task has at least one error/edge AC.
4. Every flow branch is referenced by at least one AC.
5. No dependency cycles, no duplicate tasks.
6. Every number agrees with `caffeine-domain`.
7. Every screen state maps to a journey step or is listed as a Design gap.
8. Analytics has no forbidden property, or says "N/A — no KPI".
9. Every task touching user data names its data classes and has a security AC.

Judgment only after all 8 pass: is each task atomic, is scope right for the priority.

## Feedback runs (`PLAN_RETURNED`)
Fix only the listed items, re-run all 9 checks, set `PLAN_READY` again.

## Brief missing
Return the questions in `docs/briefs/TEMPLATE-brief.md` to Ton, max 3 at once.

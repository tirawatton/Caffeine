# Caffeine v5.1 — UX/UI Audit

- **Date:** 21 Nov 2026
- **Scope:** Figma file `jVIND6Rm2KzxmEhO6w2b00`, page **🏠 v5.1 — UX journey pass** `446:10036`, sections A–M (280 phone frames, 402×874, Dark + Light). Not covered: J States boards, Z Reference notes.
- **Mode:** read-only. No Figma changes were made. Fixes go to `ux-ui-designer` (the only agent allowed to edit Figma).
- **Method:** a contrast probe over 11,438 visible text layers. Each colour comes from its variable resolved in the frame's own mode, and the background comes from the painted layers under the text's centre (gradients averaged and marked as estimates). Tap-target sizes were measured on DS component instances. Six screenshots were taken to check the suspicious results. Every frame's copy was read and compared with `docs/plan/caffeine-app-master-plan.md`.
- **Standards:** WCAG 2.2 (1.4.3 contrast; large text = 24px, or 18.66px bold), Apple HIG 44pt tap targets, and the CLAUDE.md design rules.
- **Limits:** a static file can't show VoiceOver, Dynamic Type, focus order or motion. Text is measured in Inter (the MCP stand-in), so SF Pro wraps are unverified. Probe false positives were removed after the screenshot check: the 4E text under the sheet, the 4B donut centre, and the legacy Wallet cards on Household.

## Summary

| Severity | Count |
|---|---|
| Critical | 2 |
| Accessibility | 8 (870 raw contrast failures, 11 sections) |
| Major | 7 |
| Note | 4 |

About 92% of text layers pass contrast. The failures cluster on about 6 tokens, so a few variable changes fix most of them.

## Findings

### 01 · Critical · A First run — Onboarding 3 `448:5106` (+ Light `448:5210`)
**The V1 onboarding sells a shared household wallet, which the plan builds in V2.0.** The plan puts this frame in the V1 pager (E04-T02), so every new user is promised a feature V1 doesn't have.
```
Copy:  "One wallet for the whole home" / "Everyone logs into one shared wallet.
       Caffeine tracks who paid and who owes." / pill "Auto settle-up"
Plan:  line 68 "V2.0 | Shared Household / Family Space"; E04-T02 pager = 448:4716, 448:4808, 448:5106
```
**Fix:** replace page 3 with a V1 feature (Fixed costs, or Budget & forecast). "Auto settle-up" is wrong even for V2: settling is manual (11G "Mark ฿5,875 as received").

### 02 · Critical · A Sign in `448:5314` / `448:5344`, I Sync & devices `448:30549` / `448:30604`
**Sign in promises cloud sync, but V1 is local-first with backup only.**
```
Sign in:  "Your data is encrypted and securely synced to the Cloud."
Sync:     device list includes "Web app · Chrome on Mac · yesterday"
Plan:     E21 sync-backend = V2.0; no web app in any epic
```
**Fix:** use copy like "Encrypted on this iPhone · back up to your private iCloud" (it matches 7C). Keep Sync & devices out of V1.

### 03 · Accessibility · Invisible text (WCAG 1.4.3), confirmed by screenshot
```
5B Light 448:13743  "17 Nov · Netflix ฿419 · Tap to view"  #000000 on #1C1C1E = 1.23:1
F Dark  ×18         "Paid" badge  #9EE6C4 on #9EE6C4 = 1.00:1  (renders as a solid mint bar)
                    e.g. 448:13650 Spotify and Claude Pro rows
```
The Paid badge bug has been listed in CLAUDE.md since the DS sync and is not fixed yet.
**Fix:** callout ink → `text-on-inverse`. Paid badge fill → back to 16% (or label → `text-on-light`).

### 04 · Accessibility · Light mint income text 1.44:1 (1.4.3)
About 45 occurrences in 10 of 11 sections, including the 34pt hero figure on 9L.
```
"+฿18,000" (Home, History rows)  #9EE6C4 on #FFFFFF = 1.44:1  (needs 4.5)
"↓ 6.0% vs Oct" (Reports badge)  #9EE6C4 on #E5E5EA = 1.15:1
"+฿18,450" 34pt (9L 448:7443)    #9EE6C4 on #FFFFFF = 1.44:1  (needs 3.0)
Also: 9E "+฿120.00", 9F "+฿52,000", 6B widget "+฿52,000", 4D "↑ 12.0%"
```
**Fix:** add a Light-only income *text* token, and keep #9EE6C4 for fills. Example: #237A55 = 5.27:1 on white.

### 05 · Accessibility · Light coral/600 fails by 0.23 everywhere (1.4.3)
This affects every Light primary button and every Light expense amount. A 17pt Semibold label is not large text under WCAG.
```
"Start tracking", "Save budget", "Apply Filters", "Create trip"…  #FFFFFF on #DC4526 = 4.27:1
"−฿65", "−฿1,290", "Due tomorrow · KBank Credit"…                  #DC4526 on #FFFFFF = 4.27:1
```
**Fix:** use a slightly darker Light `night/accent`. coral/700 #C93A1E = 5.12:1, so pick a value between the two that reaches at least 4.5:1.

### 06 · Accessibility · Budget hero secondary text 3.59:1 (1.4.3)
Every Home state, both modes, about 100 instances. The hero is meant to be the loudest screen in the app.
```
"PERSONAL BUDGET · NOV", "LEFT TO SPEND", "of ฿40,000 · ฿537/day", "used"
  on-primary-soft (72%) on #8C88F8 = 3.59:1
Over budget 448:6790: "OVER BUDGET BY ฿1,200", "of ฿40,000 · spending paused"
  on-accent-soft on #FF6A4D = 3.83:1
Onboarding 3 coin: "SHARED", "this month" = 3.59:1
```
**Fix:** raise `night/on-primary-soft` to at least 86% alpha (85% computes to 4.52:1). Do the same check for `night/on-accent-soft`.

### 07 · Accessibility · Periwinkle text links in Light (1.4.3)
The Light rule ("periwinkle links → `text-primary`") exists, but it was applied only to sections K–M.
```
"See all" (Home, 11 Light frames, Section header 192:786)   #8C88F8 on #FAF9F6 = 2.85:1
"See all transactions" (Wallet, 11×)                        2.85:1
"Done" (1J, 8C, 9N), "Reset All" (8D), "Edit" (8H),
"Cancel" / "Add (3)" (2C Photos picker)                     #8C88F8 on #FFFFFF = 3.00:1
"Save" (9G), "Add income" (9F), "Reset all" (8E)            2.85:1
"Continue as Guest" (Sign in Light 448:5344)                #C8C6FF on #FAF9F6 = 1.54:1
"Settle up" (Onboarding 3)                                  3.00 Light / 3.19 Dark
```
**Fix:** in Light, set these links to `text-primary` across sections A–I.

### 08 · Accessibility · Keypad Entry card text (1.4.3)
This line carries the consequence of the action the user is about to take.
```
"Left to spend ฿6,450 → ฿1,450" (10H), "≈ ฿2,820 · 100 ¥ = ฿23.50 locked" (11I),
"1,200 + 90", "Statement due 25 Nov"                    #494775 on #8C88F8 = 2.86:1 (both modes)
Picker tile labels "From" / "To" / "Category" (Dark)    #444360 on #A19DF9 = 3.95:1
```
**Fix:** raise the expression/hint line to `text-on-light` solid, or to an alpha that reaches ≥ 4.5:1 (as in 06).

### 09 · Accessibility · Light secondary text on raised surfaces (1.4.3)
```
text-secondary #6C6C70 on surface-raised #E5E5EA = 4.16:1
  sheet row subtitles (2E pickers, 5E, 5F, 5G, 9J, 10F, 10I, 11G, 12B), unselected segments
  ("12M", "Exact", "Custom", "25th"), 2B "TOTAL PURCHASE", 7D "Waiting for network…"
Warning text:
  "Cancel subscription" (5F)            #FF6A4D on #3A3A3C = 4.01 Dark / #DC4526 on #E5E5EA = 3.40 Light
  "3 recent transactions will be lost." (7F) same 4.01 / 3.40
```
**Fix:** darken Light `text-secondary` on raised surfaces (or use `surface` rather than `surface-raised` under secondary text). Destructive text follows the 05 fix.

### 10 · Accessibility (HIG, not WCAG) · Tap targets under 44pt
```
Segment 32pt tall ×446 · Filter chip / Meta chip / Dropdown pill / Space pill 40pt ×400+ · Tag 32pt · Switch 48×32
```
These pass WCAG 2.5.8 (24px minimum), so this isn't a WCAG violation. The "extend to 44 in code" note lives only in CLAUDE.md, not in the component specs or descriptions.
**Fix:** state a 44pt hit area (`contentShape` / `minimumInteractiveComponentSize`) in each component's description and in `docs/design/*-spec.md`.

### 11 · Major · Budget cycle has two rules
```
O5 (446:10038):   "Payday 25th of each month"
12B (597:37098):  "Your budget cycle runs 25th to 24th. This also updates Budget & Cycle in Settings, Home…"
Budget & Cycle:   "Budget resets on 1st" · "Current cycle: 1 – 30 Nov 2026"
Settings:         "Budget & Cycle · ฿40,000 · 1st"
Home:             "PERSONAL BUDGET · NOV · 12 days left"
```
**Decision for Ton:** does payday drive the budget cycle? Then align all five screens.

### 12 · Major · Card due date contradicts itself on one card
Showing the wrong date on a payment-due badge can lead to late fees.
```
Wallet KBank Credit (448:11831): pill "Due in 9 days" + "Payment due 10 Dec · in 9 days" + "Cut-off 25 Nov"
9J forecast (448:15814):         "Card payments · KBank Credit · 25 Nov"
```
"In 9 days" matches the 25 Nov cut-off, not 10 Dec.
**Fix:** define which date drives the due badge and the forecast, then make the card agree.

### 13 · Major · One category, two budgets in the same month
```
Home 1F (446:10784):  "Food & Drink over budget by ฿710" / "฿2,710 spent of ฿2,000 this month"
Reports (448:6926):   "Food & Drink · ฿5,715 of ฿5,000 · Over by ฿715 (114%)"
4E (448:7174):        "Your budget stays at ฿5,000 unless you change it."
Category budget total: Reports ฿36,600 vs Budget & Cycle "฿32,500 allocated"
  (category lists also differ: Utilities / Other vs Bills & Utilities / Entertainment / Health)
```

### 14 · Major · Sample data contradicts itself across screens
Developers and QA build from these frames and screenshots.
```
Today:      Home / History "Wed 18 Nov" vs Wallet "MON Today" and Fixed costs "Today, 16";
            Home (18 Nov) still says "Next: Netflix tomorrow" although Netflix is due 17 Nov
··4410:     KBank Savings (2E, 2D, 8H, 8D) and "KBank Credit ··4410" (5F);
            KBank Credit is also "•••• 4417" (Wallet)
iPhone:     "iPhone 16 · 3 of 10 · ฿2,490" (Wallet) vs "iPhone 17 Pro · Installment 4 of 10 · ฿4,490/month" (Fixed costs, 5G)
Sofa:       "ends Mar 2027" (Household wallet) vs "ends Feb 2027" (Fixed costs)
Net worth:  Wallet ฿468,300 − ฿30,270 = ฿438,030 vs Reports ฿412,850 (฿425,690 − ฿12,840);
            All Wallets assets ฿561,910 ≠ Personal ฿468,300 + Household ฿86,420 (= ฿554,720)
Income:     Fixed costs "฿12,000 received · ฿52,000 upcoming" vs History / Reports / 1L "In ฿52,000"
Goal/trip:  10F "Trip starts soon" for a trip 11B shows ACTIVE "Day 3 of 7" (16–22 Nov);
            11C is already "Funded by · Goal reached · Japan Trip Fund" before 10F completes the goal
```
**Fix:** keep one sample-data sheet (accounts, masked numbers, dates, today = one day) and re-sync the frames to it.

### 15 · Major · Naming drift
```
"Left to spend" (Home, Goals, Trips, Profile) vs "Safe to Spend" (Budget & Cycle footnote)
Tab "Analytics" vs screen title "Reports" (4A–4E, 11A, 9M back label)
Space: "FAMILY BUDGET" (1B) / "Household" (Wallet) / "Shared" (Choose a wallet) / "Family split" (2B) / "Household wallet" (2D)
User: "Ton Raweephat" (Settings, Profile) vs "Raweephat S." (Sync & devices)
Household partner: Nui (Home 1B) vs Fon (Wallet Household, Sync & devices)
4D on one screen: "Assets ฿425,690 · Debts ฿12,840" and "Assets ฿425,690 · Liabilities ฿12,840"
```
**Fix:** a glossary (one name per concept) applied across all sections.

### 16 · Major · The "share a slip" promise has no designed flow
```
Onboarding 2: "Share a slip. We log it." / "Drop in any bank e-slip."
11G:          "Scan it, or share it to Caffeine from your bank app"
```
No v5.1 frame and no plan epic covers a share sheet / share extension entry. Only in-app scanning is designed, and that path is good: + → Scan slip → 2D → Save is 4 taps.
**Decision for Ton:** design the share extension, or change the copy to "Scan or pick a slip".

### 17 · Major · Unproven and misleading claims
```
"Most Thai bank slips read in 2 seconds." (1H) / "2 sec per entry" (Onboarding 2)  — not measured; E08-T00 spike open
"Saved ฿1,240 vs Oct" (Onboarding 1)  — depends on an insight that isn't built
"of ฿40,000 · spending paused" (Over budget hero)  — reads as if the app blocks spending
```

### 18–21 · Notes
- **18:** 584 visible texts have no text style. Most are inside Budget hero v5 instances (section C has 206), which is already documented.
- **19:** the Settings footer reads "Caffeine 2.0 (2026.11)" before 1.0 ships.
- **20:** "Type IMG_4120 amount" (2C batch) reads like a generated string, and "Full ledger · UTF-8 (Thai safe)" (9I) is jargon.
- **21:** a user who signs in with Google has no designed Profile or backup state; 12A and 7C cover only Apple and Guest.

Exempt, not counted: disabled rows at 40% opacity (2E "··4410 · Sending account" 1.63–2.06:1; 12B unpicked focus pills 2.83 / 3.79:1). WCAG 1.4.3 excludes inactive components.

## What works

- **Trips math reconciles end to end.** Budget ฿60,000 = 22,000 + 12,000 + 12,000 + 8,000 + 6,000. Spent ฿27,530 = sum of categories. Paid ฿47,975 = shares ฿47,975. Settle up uses the fewest transfers (3). ¥12,000 × 0.235 = ฿2,820; ฿60,000 / 0.235 = ¥255,319; ฿32,470 / 4 days = ฿8,118/day.
- **Goals math is correct.** ฿120,000 / 24 months = ฿5,000/mo; ฿71,600 / 13 = ฿5,508; ฿191,600 to go = 120,000 + 71,600.
- **Fixed costs and Profile numbers add up.** Fixed costs: 419 + 99 + 179 + 139 + 700 = ฿1,536; 4,490 + 1,990 = ฿6,480; paid ฿839 = 139 + 700. Profile badges: 2 + 2 + 2 = 6 / 10.
- **Cash Flow is correct.** ฿52,000 − ฿33,550 = ฿18,450. "↑ ฿7,712 vs Oct" = 18,450 − (46,428 − 35,690). "฿4,120 higher than your 6-month average of +฿14,330."
- **Empty states have a next step.** 1H "Scan your first slip", 1L "Set monthly budget", 1I "Tap + below to add your first one.", 8J "Try another word or amount, or reset filters to search all of November." + Reset All Filters.
- **Destructive flows name the consequence.** 7F "3 recent transactions will be lost." + "Nothing is replaced until you confirm"; G "All 148 transactions stay"; 8G Undo toast.
- **Privacy copy is specific.** 12E "Never included: balances, amounts, account names or your name."; 2C "Caffeine only sees the photos you pick".
- **The scan path is short and has several entry points:** 1H CTA, 1N, 2A chip, widget.
- **Dark mode passes contrast outside the hero and keypad.** For example, section I has 14 failures out of 582 texts, all in Light.

## Where to start (impact ÷ effort)

1. **Token values (04, 05, 06, 09).** About four variable edits fix most of the 870 failures.
2. **Two targeted fixes (03):** the 5B callout ink and the Paid badge opacity.
3. **Light links (07):** apply the existing rule to sections A–I.
4. **Copy decisions for Ton (01, 02, 17):** onboarding page 3 and the Sign in sync claim.
5. **Rule decisions for Ton (11, 12):** payday vs cycle, and which date drives the card due badge.
6. **Data and naming (13, 14, 15):** one sample-data sheet and one glossary.
7. **Hit areas in the specs (10), and the share flow decision (16).**

## Audit fix status (ux-ui-designer, 21 Nov 2026)

Scope set by Ton: fix 01–12, 16, 17, 19, 20; defer 13, 14, 15; 18 and 21 are notes. Verify method: an ancestor-background contrast probe over the 11,677 visible texts in sections A–I and K–M (each colour resolved in its frame's mode; translucent fills composited; texts on gradients skipped), plus `get_screenshot` of the changed frames. Contrast ratios below are WCAG 2.2 relative luminance. Loop: pass 1 built the fixes; pass 2 (probe) found the Paid badge 16% fill had reverted, the Onboarding 1 hero tile labels at 3.91:1, 1B Light "Settle up" on coral, and a 12I Light "See all"; pass 3 fixed them and the probe is clean for every audited pair.

| # | Status | Evidence |
|---|---|---|
| 01 | Fixed | Onboarding page 3 is now "Know every bill before it lands" (Fixed costs): `448:5106` / `448:5210`, real Fixed costs hero `615:37399` / `615:37479` + Fixed cost rows. Old household page kept as "v5.1 — replaced 21 Nov 2026 …" `614:37371` / `614:37475`. Re-cloned on Feature Journeys (`615:63877`, step card updated) and updated in place on the App Prototype (`540:22150`). Motion for the new vignette not added yet. |
| 02 | Fixed | Sign in `448:5327` / `448:5357`: "Encrypted on this iPhone · back up to your private iCloud" (matches 7C "Encrypted in your private iCloud Drive"). Sync & devices `448:30549` / `448:30604` renamed "(V2.0 — not in V1.0)", Web app row removed, "Live on both". |
| 03 | Fixed | 5B Light callout `I448:13752;287:965` → `text-on-inverse` (white on #1C1C1E, 17.1:1). Paid badge (24 on v5.1, 10 FJ, 10 AP): the 16% fill would not persist on these instances, so the badge is solid `tint-mint` with a `text-on-light` label and check: 11.8:1 both modes. |
| 04 | Fixed | New `night/income-text` (Dark #9EE6C4, Light mint/700 #1F714C). Light: 5.96:1 on white, 5.66:1 on paper, 4.75:1 on surface-raised. 196 v5.1 texts + 5 DS components rebound; fills unchanged. Probe min: Light income-text on surface 5.96, on surface-raised 4.75. |
| 05 | Fixed | Light `night/accent` → coral/650 #CF3D20: white on coral 4.84:1, coral on white 4.84:1, on paper 4.59:1. Dark unchanged (coral/500). |
| 06 | Fixed | `night/on-primary-soft` 88%: 4.76:1 on periwinkle (both modes). `night/on-accent-soft` Dark 88%: 5.09:1; Light white 96%: 4.56:1. |
| 07 | Fixed | 64 Light links in A–I and M → `text-primary` (21:1 on white). Includes "Continue as Guest" on Sign in Light. Probe: 0 periwinkle texts left in Light frames. |
| 08 | Fixed | 140 texts at 60–70% `text-on-light` on periwinkle (Entry card expression/hint lines, Picker tile labels, Account card labels) → `on-primary-soft` at full layer opacity: 4.76:1 on periwinkle, 5.77:1 on the Picker tile glass. Picker tile main component label `68:478` fixed too. |
| 09 | Fixed | Light `night/text-secondary` → gray/650 #636366: 4.77:1 on surface-raised, 5.99:1 on surface. Destructive text: 5F button and 7F warning row moved to `night/bg` + glass stroke: coral 6.01:1 Dark, 4.59:1 Light. |
| 10 | Fixed | 44pt (iOS) / 48dp (Android) hit-area note in the descriptions of Segment, Segmented control, Filter chip, Meta chip, Dropdown pill, Space pill, Tag, Switch. Feature specs must repeat it when they are written. |
| 11 | Fixed | Payday drives the cycle (25th–24th). 9A selects 25th + "Current cycle: 25 Oct – 24 Nov 2026, set by your payday."; Settings "฿40,000 · 25th" ×6; all Home heroes "6 days left" with per-day = left ÷ 6 (฿6,450 → ฿1,075/day); 1I (Dec cycle) "29 days left", ฿1,379/day. O5 / 12B already said 25th. See questions Q-A2 and Q-A3. |
| 12 | Partly fixed | Rule recorded in CLAUDE.md: the due date drives the badge, reminders and forecast; the cut-off is only the statement date. KBank Credit now reads "Due in 22 days" (10 Dec, today 18 Nov) on 42 texts. **Deferred:** the 9J/9K line "KBank Credit · 25 Nov", see Q-A1. |
| 13, 14, 15 | Deferred (Ton) | Sample-data sheet, glossary and naming re-sync are left for a later pass. |
| 16 | Fixed | Copy only: Onboarding 2 "Scan a slip. / We log it." + "Scan or pick any bank e-slip…"; 11G "Scan it, or pick it from Photos"; 11F/11G "Got a repayment slip? Scan it and Caffeine matches it…". |
| 17 | Fixed | "2 sec per entry" → "QR read on this iPhone"; 1H → "Reads the QR code on Thai bank e-slips, right on this iPhone."; "Saved ฿1,240 vs Oct" → "On track for payday"; Over budget hero "of ฿40,000 · ฿41,200 spent" (neutral, and it doesn't repeat the "Over budget by ฿1,200" caption above it). |
| 18, 21 | Notes | Not in scope. |
| 19 | Fixed | Settings footer "Caffeine 1.0 (2026.11) · Made in Bangkok" ×6. |
| 20 | Fixed | 2C batch "Type the amount"; 9I "Full ledger · opens in Excel and Numbers". |

**Probe result after pass 3:** 76 of 11,677 texts below threshold, and none in an audited pair: 42 status-bar "9:41" texts bound to `Labels/Primary` (new finding, see below), 31 on the legacy Household Wallet cards (exempt in this audit) and 3 on the 2C camera chrome, which stays Dark in Light frames on purpose. The probe reads backgrounds from ancestors only. Text over sibling shapes or gradients needs a screenshot check.

**New, not fixed:** status-bar time "9:41" on 42 v5.1 frames (for example 9F / 9G Dark) is bound to `Labels/Primary` and renders faint (1.23:1 Dark, 1.05:1 Light). This is system chrome in the app, but the frames should follow the re-theme rule (`text-primary`).

**Questions for Ton:**
- **Q-A1 (12):** the 9J/9K forecast is "Balance on 30 Nov". With the payment due on 10 Dec, the KBank card payment (−฿24,960) falls outside the forecast, which would move 9J from ฿64,750 to ฿89,710. Should the forecast end on 30 Nov (drop the card line), at the cycle end (24 Nov), or 30 days ahead (keep it, dated 10 Dec)?
- **Q-A2 (11):** the Figma per-day figure counts the days left without today (฿6,450 ÷ 6 = ฿1,075). caffeine-domain counts today too (÷ 7 = ฿921). Which one is right?
- **Q-A3 (11):** with the 25th–24th cycle, elapsed on 18 Nov is 25/31 = 81%. 1B Family at 80% used becomes **On track** by the pace rule, but the frame still shows Over pace. Change 1B's data, or switch it to On track?

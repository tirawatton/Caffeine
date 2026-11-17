# Caffeine — Design Context for Claude

This file orients Claude (or any agent) working on the **Caffeine** personal finance iOS app — the SwiftUI app and its Figma design file. Read this before making design or product decisions so new work stays consistent with what's already built.

## Project

- **App:** Caffeine — a personal finance / expense-income tracker, built in **Swift + SwiftUI**.
- **Figma file:** `https://www.figma.com/design/jVIND6Rm2KzxmEhO6w2b00/Caffeine` (fileKey `jVIND6Rm2KzxmEhO6w2b00`)
- **Owner:** Ton (Raweephat Sirinatthakul) — senior iOS/SwiftUI developer, Bangkok. Second track: founder.
- **Standing rule:** if unsure what a requirement means, ask Ton first instead of guessing.

## Workflow — the loop

All design and implementation work runs as a loop, not a straight line. Both skills in `skills/` (`designer` → `ios-swiftui-design`) follow it:

```
Start -> Set Goal -> Reason -> Verify -> Pass? --YES--> Exit loop
                       ^                  |
                       |                  NO
                       |                  v
                       +----- Fix <--- Feedback
```

- **Set Goal** = a one-line goal plus numbered PASS/FAIL acceptance criteria, built from the brief, the design rules below, and the UX/HIG baseline. Show them to Ton before building.
- **Verify** = check every criterion by number with evidence (screenshot, node, measured value) — re-check all of them each iteration.
- **Feedback → Fix** = a list of failures (criterion · where · what's wrong · what's right), fixed with the smallest targeted change, then back to Reason.
- **Loop limit:** 3 Verify iterations. Still failing → stop and ask Ton.
- **Hand-off between skills:** `designer` exits into `ios-swiftui-design`. A design-level failure found during implementation goes back to `designer` as Feedback (re-enters at Fix).
- Ambiguous requirement at any stage → ask Ton (standing rule).

## Design rules (apply to every new screen/component)

- **60:30:10 color theory** — 60% charcoal (night/background/surface), 30% periwinkle hero card (one per screen), 10% coral (action / money-out accent).
- **iOS typography guidelines** — use the `iOS/*` and `Data/*` text styles already defined (see Text styles below). Don't invent ad hoc sizes.
- **8-Point Grid System** — all padding, gaps, and radii bind to the `space/*` and `radius/*` variables (0, 8, 16, 24, 32). Content area: x=16, y=64, 16px side margins, 24px section gaps. Bottom-pinned elements sit 40px from the bottom.
- **Mood/tone reference:** tubik's Dribbble shot "AI-Powered Mobile App for Restaurant Operations" — dark charcoal, periwinkle block, coral accent, white/pill controls, glass materials.
- **Screen size:** 402×874 (iPhone frame).
- **Font:** Inter stands in for SF Pro in Figma previews (SF Pro doesn't render there); DM Mono Medium for data/mono text. Real app should use SF Pro / SF Mono.
- **Color semantics:** mint = income, coral = expense/accent, off-white/pill = selected state only.

## File structure (Figma pages)

| Page | Contents |
|---|---|
| `0:1` Dashboard | Original seed page — untouched |
| `🎨 Design System` | Components, Foundations (variables/styles), Patterns |
| `🔎 Research — Expense vs Income` | Moodboard / inspiration board |
| `📱 Screen 1 — Dashboard` | Dashboard & Transactions, Household ledger (shared) |
| `📱 Screen 2 — Add Transaction` | Add transaction (keypad + details), Scan slip camera, Review slip |
| `📱 Screen 3 — Accounts & Wallet` | Wallet (cards), Household wallet (shared) |
| `📱 Screen 4 — Statistics & Reports` | Spending / Cash flow / Net worth views, Insight sheet; v1 archived alongside |
| `📱 Screen 5 — Subscriptions & Installments` | Fixed-costs dashboard: Subscriptions view, Installments view |
| `📱 Screen 6 — Sync, Devices & Widgets` | Sync & devices modal, sync-state reference, Home Screen widgets |
| `🧭 Concept coverage — Next-gen features` | One-page map of the 6 next-gen features → screens/components |

## Design System — key tokens

**Variable collections:**
- `Caffeine / Primitives` — raw color values
- `Caffeine / Night` — semantic colors: `bg`, `surface`, `surface-raised`, `pill`, `primary` (periwinkle), `accent` (coral), `income` (mint), `text-primary`, `text-secondary`, `text-on-light`, `tint-mustard`, `tint-mint`, `tint-lilac`, `tint-coral`, `tint-sky`, `glass-light`, `glass-stroke`, `glass-stroke-dark`, `glass-dark`
- `Caffeine / Dimensions` — `space/0,8,16,24,32`; `radius/sm,md,lg,xl,full`

**Hex reference:** charcoal `#1C1C1E`/`#2A2A2C`/`#3A3A3C`, paper `#F4F3EE`, periwinkle `#8C88F8`, coral `#FF6A4D`, mint `#9EE6C4`, mustard `#F5C85A`, lilac `#C8C6FF`, coral-tint `#FFB3A1`, sky `#BDE3EE`, grey `#A1A1A6`.

**Text styles:** `iOS/Large Title`, `Title 2`, `Title 3`, `Headline`, `Body`, `Subhead`, `Subhead Regular`, `Footnote`, `Footnote Regular`, `Caption`, `Caption Regular`, `Caption Upper`; `Data/Mono Caption`, `Data/Display`, `Data/Mono Subhead`.

**Effect styles:** `Elevation/Floating`, `Material/Glass`, `Material/Glass Floating`.

**Core components:** Filter chip, Date header, Transaction row (+ optional "Paid by" household marker), Tab bar (Collapsed/Expanded), Avatar, Icon button, Dropdown pill, Badge, Search field, Segment / Segmented control, Stat tile, Key, Button, Picker tile, Meta chip, Favorite chip, Tag, Attachment tile, Switch, Text area, Wallet card (Credit/Bank/Cash), Legend row, Budget row (v1, archived), Alert banner, Category budget row (OK/Warning/Over/No budget), Account summary row.

**"Next-gen features" components** (added for the concept redesign): **Insight card** (AI nudge), **Sync status** (Synced/Syncing/Offline), **Member** (household avatar marker), **Auto-fill row** (Slip/AI source tags), **Subscription row**, **Installment row**.

## What's been built — by concept feature

The brief asked the app to move from a legacy local-DB tracker to a next-gen app. Six concept features were mapped to concrete screens:

1. **Automated E-Slip Processing** (Vision framework QR scan of Thai bank slips)
   - Screen 1 quick-add: **Scan slip** action.
   - Screen 2A: Scan slip chip.
   - Screen 2C (new): camera view with QR viewfinder lock-on.
   - Screen 2D (new): review screen — amount/date/recipient auto-filled, each tagged **"From slip"**, with a **"Not bank-verified"** badge (placeholder for a future bank verification API).

2. **Shared Household Wallets**
   - Screen 1: **Household ledger** frame — every row shows who paid (Member marker).
   - Screen 3: **Household wallet** frame — joint account card, "who paid this month" split, settle-up, shared installment plan.
   - Screen 2D: wallet + payer picker.

3. **Cloud-Native Architecture & Cross-Platform Sync** (Firebase/Supabase-style)
   - Dashboard header: wallet switcher + "Synced" state.
   - Screen 6A (new): **Sync & devices** — account, device list (iPhone/iPad/web), household members, Money Manager backup import.
   - Sync status states documented: Synced / Syncing / Offline (with queued-count).

4. **Next-Gen Liquid Glass UI & Interactive Widgets**
   - New sheets/toasts/modals use the glass material tokens (`Material/Glass`, `Material/Glass Floating`).
   - Screen 6B (new): three **Home Screen widgets** — Balance + quick-add (+), Next fixed charge, Quick-log row (Expense/Income/Scan slip).

5. **AI-Powered Categorization & Insights**
   - Screen 2D: category auto-suggested with a reason shown ("Transport suggested from 6 earlier PTT payments").
   - Screen 4 (Spending view): alert banner now opens an **Insight sheet** — e.g. "You dined out 30% more than last month," budget comparison bars, suggested new budget, Raise/Keep actions.

6. **Smart Subscription & Installment Tracker**
   - Screen 5 (new): **Fixed costs** dashboard — month charge timeline (hero), Subscriptions / Installments segmented views, cash-flow coverage check.
   - Screen 1: new "upcoming fixed charges" row linking into it.

A full mapping lives on the Figma page **🧭 Concept coverage — Next-gen features**, and in the companion spreadsheet (see below).

## Known limitations / things to know

- **Font:** Inter is a stand-in for SF Pro in Figma; real app uses SF Pro/SF Mono.
- **Liquid Glass scope:** glass material applied only to *new* surfaces (sheets, toasts, widgets). Existing solid cards were left as-is — restyling every card to translucent would be a separate, larger pass.
- **Dashboard fold:** the new "upcoming fixed charges" row pushes the transaction list below the tab bar on the main Screen 1 frame (visible on scroll / in the full-scroll reference frame).
- **Fixed costs entry point:** lives under the Wallet tab, opened from the Dashboard's upcoming-charges row.
- **Localization:** the AI-categorization example uses a Thai PTT fuel payment rather than "ค่าน้ำมัน" because the stand-in font (Inter) has no Thai glyphs.
- **Placeholders:** camera feed (Screen 2C) and widget wallpaper (Screen 6B) are flat gradients, not real screenshots; Member initials render at 10pt, below the documented type scale.
- **Sample data:** all amounts, dates, and names across the new/updated frames are invented for illustration.
- **Audit coverage:** the newly created frames (Screens 2C/2D, 3 Household, 4 Insight sheet, 5, 6, and the Design System additions) were checked for 16px margins, 8pt spacing, text styles, and token bindings — all clean except one unbound fill (fixed). The in-place edits to the original Screen 1 frames and the new Screen 1 Household frame were **not** re-audited.
- Earlier in the project: a stale "Screen 1 — 8pt Grid Fixes" spreadsheet exists from an older pass and has not been updated to match the current card; two retired v1 Screen 4 components (two-ring donut, Legend row, Budget row) remain in the Design System unused by current screens; the Screen 3 tab layer selected for Credit Cards is still internally named "Budgets".

## Deliverables produced this session

- **Figma file** (link above) — all pages/frames listed under "File structure."
- **Spreadsheet:** *Caffeine — Next-gen concept coverage* — `https://claude.ai/artifact/WiXoEwVvpuFEbhwRhq126U`
  - **Coverage** sheet: every screen/frame × concept feature × New/Updated status × what it covers.
  - **Design System** sheet: new components/icons added.
  - **Things to know** sheet: the limitations above.

## Working conventions for future sessions

- Match existing component/variable naming exactly before creating new ones — search the Design System first (`search_design_system` / on-canvas inspection) rather than hardcoding colors or spacing.
- New frames are added beside existing ones on the same page (or a new page) rather than overwriting; older versions are kept and labeled (e.g. "v1 — before review") for comparison.
- Screenshot after composing a frame, and again only after a targeted fix — don't re-screenshot unchanged work.
- Ask Ton before guessing on ambiguous requirements (standing preference).

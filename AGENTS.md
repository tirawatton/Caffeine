# Caffeine — Design Context for Codex

This file orients Codex (or any agent) working on the **Caffeine** personal finance iOS app — the SwiftUI app and its Figma design file. Read this before making design or product decisions so new work stays consistent with what's already built.

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
| `📱 Screen 2 — Add Transaction` | **Add Transaction spec v1.2** (v1.1 frames edited in place, new v1.2 states added; row at y=0 in flow order, all frames top-aligned with 80px gaps, Night theme, spec mapped): 2A Keypad · Expense · Personal `144:897`, 2A Keypad · Income · Personal `166:1494`, 2A Keypad · Transfer · Card payment `144:952`, 2A Keypad · Smart Banner (P2) `166:1675`, 2A Keypad · Limited Photos access `166:1810`, 2B Details · Credit card + Installment (full scroll) `144:1007`, 2B Details · Family split (full scroll) `144:1065`, 2B Details · Unreadable slip fallback (full scroll) `166:2220`, 2C Scan slip · Scanning `144:1123`, 2C Scan slip · Error `144:1156`, 2D Review slip · Personal `144:1189`, 2D Review slip · Family (full scroll) `144:1232`, 2D Review slip · Batch queue (1 of 3) `166:2058`, States & notes board `144:1275` (v1.2: Smart Banner P2 + Limited access, To-account picker same-account guard, Income, From Photos, Scan/Share Extension, Review, Batch queue, Priority, Layout). The v1 frames (2A, 2B, 2C, 2D, Behaviour notes) were kept in a second row at y=2160 (same 80px gaps, order 2A · 2B · 2C · 2D · notes) and renamed "v1 — before review · …" |
| `📱 Screen 3 — Accounts & Wallet` | **Wallet** (Multi-Wallet spec 1.1; frames named "Wallet — A …" to "Wallet — I …", "v1.1" dropped from names once v1 was deleted; row at y=0): A Carousel · Personal `116:1039`, C Carousel · All Wallets (Combined) `117:1596`; sheets at y=2100: D Choose a wallet `119:1658`, E Add / Manage accounts `119:1838`, F Account `…` menu `119:1993`, G Hide from Wallet confirm `119:2207`, H Exclude from Net Worth confirm `119:2334`; States board `120:2785` (y=3100) (loading, empty Space, offline/stale, card × CTA states, empty filter, pagination); Notes `121:3252` (behaviour & handoff). Frame B (Grid view) was removed at Ton's request — grid mode has no screen frame now (Account tile component and grid toggle remain). The old v1 frames (main screen, full scroll, card edit menu, behaviour notes) were deleted at Ton's request — only v1.1 remains. Household wallet (shared) `86:868` kept unchanged, renamed "Screen 3 — Household wallet (shared, full scroll)" and moved to x=1576, y=0 beside the v1.1 row |
| `📱 Screen 4 — Statistics & Reports` | Spending / Cash flow / Net worth views, Insight sheet; v1 archived alongside |
| `📱 Screen 5 — Subscriptions & Installments` | Fixed-costs dashboard: Subscriptions view, Installments view |
| `📱 Screen 6 — Sync, Devices & Widgets` | Sync & devices modal, sync-state reference, Home Screen widgets |
| `📱 Onboarding & Login` | 4-screen flow: Safe to Spend, E-Slip & AI, Household & Assets, Login & Security (prototype flow "Onboarding"). Screens 1–3 are the UI-first redesign (Pinterest-inspired: 2-line headline, 1-line description, benefit pill, large UI vignette — ring / stacked slip card / household orbit); the old text-heavy versions were deleted. Login & Security still uses Thai lines in Noto Sans Thai (not a text style). DM Mono has no ฿ glyph, so baht amounts use Inter styles. DS additions: `Page indicator`, `icon/lock`, `icon/utensils` |
| `🧭 Concept coverage — Next-gen features` | One-page map of the 6 next-gen features → screens/components |

## Design System — key tokens

**Variable collections:**
- `Caffeine / Primitives` — raw color values
- `Caffeine / Night` — semantic colors: `bg`, `surface`, `surface-raised`, `pill`, `primary` (periwinkle), `accent` (coral), `income` (mint), `text-primary`, `text-secondary`, `text-on-light`, `tint-mustard`, `tint-mint`, `tint-lilac`, `tint-coral`, `tint-sky`, `glass-light`, `glass-stroke`, `glass-stroke-dark`, `glass-dark`
- `Caffeine / Dimensions` — `space/0,8,16,24,32` (plus 40, 48, 64); `radius/sm,md,lg,xl,full`; layout tokens `layout/tab-bar-inset` = 128 (scroll content bottom padding: tab bar 64 + bottom offset 40 + section gap 24) and `layout/row-divider-inset` = 72 (ledger divider leading inset)

**Hex reference:** charcoal `#1C1C1E`/`#2A2A2C`/`#3A3A3C`, paper `#F4F3EE`, periwinkle `#8C88F8`, coral `#FF6A4D`, mint `#9EE6C4`, mustard `#F5C85A`, lilac `#C8C6FF`, coral-tint `#FFB3A1`, sky `#BDE3EE`, grey `#A1A1A6`.

**Text styles:** `iOS/Large Title`, `Title 2`, `Title 3`, `Headline`, `Body`, `Subhead`, `Subhead Regular`, `Footnote`, `Footnote Regular`, `Caption`, `Caption Regular`, `Caption Upper`; `Data/Mono Caption`, `Data/Display`, `Data/Mono Subhead`.

**Effect styles:** `Elevation/Floating`, `Material/Glass`, `Material/Glass Floating`.

**Core components:** Filter chip, Date header, Transaction row (+ optional "Paid by" household marker), Tab bar (Collapsed/Expanded), Avatar, Icon button, Dropdown pill, Badge, Search field, Segment / Segmented control, Stat tile, Key, Button, Picker tile, Meta chip, Favorite chip, Tag, Attachment tile, Switch, Text area, Wallet card (Credit/Bank/Cash), Legend row, Budget row (v1, archived), Alert banner, Category budget row (OK/Warning/Over/No budget), Account summary row.

**Wallet components** (frame "Components — Wallet" `114:532` on the Design System page; renamed from "Components — Wallet v1.1" once the v1 Wallet screens were deleted, along with its title and the "Icons — Wallet" group): **Account card** `114:615` (Active = periwinkle / Inactive = surface-raised; padding 24 all sides; `…` has a 48pt hit area pinned absolute top-right so the 32pt circle aligns to the padding; toggles for space badge, status pill, pin, usage bar, meta tiles, footer), **Account tile** `114:668` (grid Bento tile, padding 16, same `…` treatment, icon swap), **Account pager** `114:689` (`n / total` with 48pt prev/next), **Sheet row** `118:568` (Default/Destructive). **Card face refactor:** Account card now has a `Type` axis — `Type=Detailed` (the original 338×302 layout) and `Type=Card face` (`133:1040` Active / `133:1080` Inactive): a physical-credit-card look at 338×208 with chip, masked PAN (`Card number` prop, Data/Mono Subhead), `Network` (VISA), statement balance bottom-left, `VALID THRU` + `Expiry` bottom-right, and two concentric `tint-lilac` rings bottom-right. The details that no longer fit (due-status pill, usage bar, Available credit / Payment due tiles, cut-off footer) moved into the **Card details strip** component `134:562`, placed under the `Account pager` (`1 / 6` in A, `1 / 11` in C). Card face is used for credit cards only, and only in frames A and C. Bank/Cash cards and frames D–H plus the States board still use `Type=Detailed`. Icons: `cardPlus` (Manage accounts = `card.badge.plus`, plus drawn as a corner badge), `grid`, `carousel`, `pin`, `eyeOff`, `minusCircle`, `pencil`, `trash`, `cloudOff`, `archive`. The old Wallet card is renamed **Wallet card (legacy)** `71:525`, with a component description saying it is used only by the Household wallet frame; new wallet screens use Account card.

**"Next-gen features" components** (added for the concept redesign): **Insight card** (AI nudge), **Sync status** (Synced/Syncing/Offline), **Member** (household avatar marker), **Auto-fill row** (Slip/AI source tags), **Subscription row**, **Installment row**.

## What's been built — by concept feature

The brief asked the app to move from a legacy local-DB tracker to a next-gen app. Six concept features were mapped to concrete screens:

1. **Automated E-Slip Processing** (Vision framework QR scan of Thai bank slips)
   - Screen 1 quick-add: **Scan slip** action.
   - Screen 2A: Scan slip and From Photos (v1.2) sit next to Save in the bottom dock, in the thumb zone. In v1.2 both are icon-only 56×56 buttons so Save keeps its label (v1.1 had a labelled Scan slip; v1 had a chip). Smart Banner (P2) and Limited Photos access states are separate 2A frames.
   - Screen 2C: camera view with the QR viewfinder. It has a Scanning state and an Error state with the copy "QR code is processed on-device". v1.2 Error actions: Choose another photo (Try again when scanning live) and Use as receipt & type amount, which opens the 2B fallback frame with the photo already attached as the receipt.
   - Screen 2D: review screen. v1.2 adds a slip thumbnail in the card header (tap to expand), a Bank row (source bank, From slip), an "Attach slip as receipt" switch (on by default), and a Batch queue variant ("Slip 1 of 3", Skip + Save & next). Amount, date, recipient and bank are tagged **"From slip"**; category and account are tagged **"Suggested"**. The verification badge reads **"QR parsed (local)"**, and "Bank verified" with a check appears only after a bank API confirms. Only Expense and Transfer types are offered.

2. **Shared Household Wallets**
   - Screen 1: **Household ledger** frame — every row shows who paid (Member marker).
   - Screen 3: **Household wallet** frame — joint account card, "who paid this month" split, settle-up, shared installment plan.
   - Screen 2B (Family): Paid by + Split (50/50 / Custom / 100% shared). Screen 2D (Family): a "Household wallet · Paid by You · Split 50/50" summary card pinned above Save. Both are hidden in the Personal space.

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
- **Layout audit (17 Nov 2026):** every 402pt screen on the Onboarding page and on Screens 1–6 was checked for overflow, 16pt margins, constraints, 8pt padding and gaps, token bindings and centering. Fixed: the Screen 1 full-scroll tab bar, home indicator and bottom fade were below the frame (the frame was cut to 1604pt and these are now pinned to the bottom); the raw 160 Content bottom padding on Screens 1, 3 Household and 4 is now bound to `layout/tab-bar-inset` (128); the raw 72 dividers are bound to `layout/row-divider-inset`; Content, sheets and onboarding blocks now Stretch, and the onboarding CTAs are pinned to the Bottom; the onboarding 4/2pt gaps were snapped to `space/8` / `space/0`; the onboarding status bars were recolored to `text-primary` (they were black on charcoal); the Screen 6B caption now sits on the 16pt margins; the 2B Total/Monthly tiles are equal height; the 2C toast is centered. Kept on purpose: the carousel peek cards, scroll content under the tab bar, the filter-chip and Favorites scrollers clipped at the margin, the Back/Skip glyphs aligned to the margin inside 48pt tap areas, and the Household ledger's stacked second avatar.
- **Audit coverage:** the newly created frames (Screens 2C/2D, 3 Household, 4 Insight sheet, 5, 6, and the Design System additions) were checked for 16px margins, 8pt spacing, text styles, and token bindings — all clean except one unbound fill (fixed). The in-place edits to the original Screen 1 frames and the new Screen 1 Household frame were **not** re-audited.
- **Add Transaction v1.2 (Screen 2):** Ton chose to keep the Night theme (spec §6 asks for Light Bento) and to edit the v1.1 frames in place. The Smart Banner and Limited-access pills take the Today/Memo chip slot while shown (they don't fit in the flow otherwise); × brings the chips back. The icon-only Scan slip / From Photos buttons hide the Button label layer on the instance and use `space/16` side padding; VoiceOver labels must be set in code. 2D Family became a full-scroll reference (920pt) because the new rows push the content into the pinned summary card. The new rows/pills (thumbnail, receipt switch row, queue actions row) are local frames, not DS components. The sample data (KBank ··4410 / ··7731, ฿45,000 salary) is invented.
- **Add Transaction v1.1 (Screen 2):**
  - Theme: Ton chose "Night, spec mapped" over the spec's light Bento theme. The spec's black hero is the periwinkle Entry card, and the black Save is the coral Primary Button. The spec's red errors are coral with an icon and text.
  - The spec's referenced screenshot was not attached; the frames were built from the spec text and the v1 frames.
  - Scan slip moved from the detail-chip row into the bottom dock next to Save, for thumb reach. The chip row keeps only Today and Memo. In the Actions row, Scan slip hugs its content (about 151pt, QR icon + label). Save fills the rest (about 211pt). Both use the Button's default 24pt side padding. Ton reviewed equal-width and 1:3 / 2:3 splits and chose to keep this one.
  - Every type-specific frame (2A, 2B, 2D) has a Space switcher (Dropdown pill) beside THB in the hero. 2A Transfer replaces the eyebrow with a `CARD PAYMENT` Badge and uses the expression line for "Statement due 25 Nov".
  - 2D hides the hero From/Category tiles so the same field isn't shown twice. Account and Category appear as `Suggested` Auto-fill rows.
  - The 2B frames are full-scroll references. In the real 874pt viewport, Save stays pinned 40pt from the bottom. The 2A gap between the content and the keypad (26pt) stretches with device height and is not a token.
  - The Installment / Family split cards, the in-card selectors (cloned Type selector on `night/bg`), and the Smart Banner are local frames, not DS components yet.
  - The detail chips and the Space pill are 40pt tall, inherited from the DS; in code, extend the hit area to 44pt.
  - Layout fixes (after review): the 2A Favorites row is a 370pt horizontal scroller that clips at the 16pt margin, so it no longer overflows Content. The hero Entry card padding is `space/24` on all four sides, and the Amount block inside it has 0 padding, so the content is centered (this matches the Wallet Account card). Because the tiles are narrower, the credit card tile reads "KTC Visa". The Actions-row buttons are a fixed 56pt (not Fill inside a Hug row). Hidden leftover layers were removed (the 2A Transfer eyebrow and the 2C Error title). Uneven padding is kept on purpose only for: divider insets (48 left), pills with a leading circle (the toast, the Favorite chip: 8 left / 16 right), and the Tag pill with a trailing × (16 left / 8 right). The 2A keypad → Save gap is 8, matching the key gaps. 2C/2D pinned elements use bottom constraints (sheet and summary = Stretch/Bottom, toast = Center/Bottom, slip and viewfinder = Center/Center). The 2B frames are sized so the content ends exactly 24pt above Save.
  - All sample data (KTC Visa ··4821, Makro, Ploy, amounts) is invented.
- **Wallet v1.1 (Screen 3):**
  - Theme: Ton chose "Night, spec mapped" over the spec's light Bento theme. The spec's solid-black active card is the periwinkle Account card; inactive cards are surface-raised; the spec's red alert is coral with an icon and text.
  - Not designed (entry points only): Net Worth detail, Add account, Manage accounts list, payment flow. The 1-account state is a text note, not a screen.
  - Icon tint: icons swapped inside instances keep per-instance color overrides; swapping an icon resets them, so handle icon tint in code.
  - The disabled CTA (offline) is shown at 40% opacity, not as a component state.
  - The carousel's next card deliberately bleeds to the screen edge as a peek.
  - Card face is 338×208 (1.625:1). That is about 2.5% off the ISO card ratio (1.586:1, which would be 338×213) so that padding and gaps stay on the 8pt grid. The peek cards (`116:1247`, `117:1629`, still `Type=Detailed`) are fixed at 208 tall with clipping on, so their own 24pt corners match the active card. Content below 208, such as the meta tiles, is hidden. In code, the peek should be the next card at full height. Frames A and C are 70pt taller because of the details strip. The VISA mark is plain `iOS/Headline` text, not a brand logo asset. The rings use paint opacity on `tint-lilac` (14%), and that opacity is not a token.
  - SwiftUI hand-off (`ios-swiftui-design`) is paused: still need Ton's choice of output (Swift files vs guidance) and the minimum iOS version.
- Earlier in the project: a stale "Screen 1 — 8pt Grid Fixes" spreadsheet exists from an older pass and has not been updated to match the current card; two retired v1 Screen 4 components (two-ring donut, Legend row, Budget row) remain in the Design System unused by current screens. Tab bar order is Home, Wallet, Analytics, Profile (Wallet tab layer renamed from the old "Budgets" name).

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

# Tokens changelog

Figma `Caffeine / Night` and `Caffeine / Primitives` (file `jVIND6Rm2KzxmEhO6w2b00`). Newest first.

> Since 2026-11-21 the token pipeline exists (foundation T-01): `scripts/tokens/figma-export.json` → `scripts/tokens/generate.py` → `docs/design/tokens.json`, the iOS colour sets (`ios-app/Resources/Colors.xcassets/Night/`) + `DesignTokens.swift`, and the Android `Caffeine{Colors,Dimens,Type}.kt`. Gate: `python3 scripts/tokens/diff.py` must print `0`. This file keeps the human-readable history.

## 2026-11-21 · Token pipeline built (foundation T-01) and DG-52 component sync

- **Generated from Figma** (36 `Caffeine / Night` colours × Dark / Light, 22 `Caffeine / Dimensions`, 15 `iOS/*` + `Data/*` text styles, 3 effect styles). Includes every 21 Nov audit value below: `incomeText` Dark #9EE6C4 / Light #1F714C; Light `accent` #CF3D20; Light `textSecondary` #636366; `onPrimarySoft` `0xE01C1C1E`; `onAccentSoft` Dark `0xE01C1C1E` / Light `0xF5FFFFFF`; `shadow` `0x59000000` / `0x1F000000`.
- Legacy `hero`, `hero-start`, `hero-end`, `hero-rim`, `hero-text-secondary` are generated as **deprecated** (unused since v5). `Caffeine / Bento` is not exported. Ton D-2 (21 Nov 2026): keep both marked deprecated until every active frame is migrated to the Home v5 global variables and verified, then delete them from Figma once zero frames reference them.
- Text style weights follow Figma, not the older table in the `design-tokens` skill: `iOS/Subhead` = Medium, `iOS/Caption` = Semibold.
- **DG-52 (Ton Q-50), DS page only:** 14 secondary labels in **Stat tile** `47:413` (Income / Expense label) and **Wallet card (legacy)** `71:525` (number, label, meta labels) were `text-on-light` at 70% layer opacity (below 4.5:1 on periwinkle); they are now `night/on-primary-soft` at 100%, like the audit fix pass did on screens. Every other main component already carried the audit values (0 texts bound to `night/income`; Picker tile label `68:478` = `on-primary-soft`). Budget hero v5 / Metric hero v5 on Home v5 were checked read-only (clean). No pins or overrides on the Home v5 page.

## 2026-11-21 · UX/UI audit v5.1 fixes (findings 04, 05, 06, 09)

| Token | Mode | Before | After | Why (contrast) |
|---|---|---|---|---|
| `coral/650` (new primitive) | — | — | #CF3D20 | between coral/600 and coral/700 |
| `mint/700` (new primitive) | — | — | #1F714C | Light income text |
| `gray/650` (new primitive) | — | — | #636366 | Light secondary text |
| `night/accent` | Light | coral/600 #DC4526 | coral/650 #CF3D20 | white on it 4.84:1, on white 4.84:1, on paper 4.59:1 (was 4.27:1) |
| `night/text-secondary` | Light | gray/600 #6C6C70 | gray/650 #636366 | 4.77:1 on surface-raised (was 4.16:1) |
| `night/income-text` (new) | Dark / Light | — | mint/300 #9EE6C4 / mint/700 #1F714C | Light 5.96:1 on white, 4.75:1 on surface-raised (mint was 1.44:1). Text only; fills keep `night/income` |
| `night/on-primary-soft` | both | #1C1C1E 72% | #1C1C1E 88% | 4.76:1 on periwinkle (was 3.59:1) |
| `night/on-accent-soft` | Dark | #1C1C1E 72% | #1C1C1E 88% | 5.09:1 on coral/500 (was 3.83:1) |
| `night/on-accent-soft` | Light | #FFFFFF 72% | #FFFFFF 96% | 4.56:1 on coral/650 |

Dark is visually unchanged except `on-primary-soft` / `on-accent-soft` (darker secondary ink on the hero blocks). Variable ids: coral/650 `VariableID:613:326`, mint/700 `VariableID:613:327`, gray/650 `VariableID:613:328`, night/income-text `VariableID:613:329`.

**For T-01:** add `incomeText` to both platform outputs. `on-*-soft` keeps its alpha in the ARGB value.

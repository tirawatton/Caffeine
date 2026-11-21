# Tokens changelog

Figma `Caffeine / Night` and `Caffeine / Primitives` (file `jVIND6Rm2KzxmEhO6w2b00`). Newest first.

> The token pipeline (`scripts/tokens/`, `docs/design/tokens.json`, the generated iOS colour sets / `DesignTokens.swift` and the Android `Caffeine{Colors,Dimens,Type}.kt`) does not exist yet. It is foundation task T-01. Until then this file is the record of token changes.

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

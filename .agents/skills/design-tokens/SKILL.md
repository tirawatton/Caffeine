---
name: design-tokens
description: Mapping of Caffeine Figma variables and text styles to iOS (Colors.xcassets + DesignTokens.swift) and Android (CaffeineColors/CaffeineDimens/CaffeineType Kotlin). Token naming, Dark/Light handling, alpha tokens, fonts, and the diff gate. Read by ux-ui-designer (generates them) and both developers (use them).
---

# Design Tokens

## Sources (Figma)
- `Caffeine / Night` (modes Dark, Light): bg, bg-clear, surface, surface-raised, pill, primary, accent, income, text-primary, text-secondary, text-on-light, text-on-inverse, text-on-accent, inverse, tint-mustard, tint-mint, tint-lilac, tint-coral, tint-sky, glass-light, glass-dark, glass-stroke, glass-stroke-dark, on-primary-soft/-wash/-line, on-accent-soft/-wash/-line, shadow.
- `Caffeine / Dimensions`: space/0,8,16,24,32,40,48,64; radius/sm,md,lg,xl,full; layout/tab-bar-inset (128), layout/row-divider-inset (72).
- Text styles `iOS/*`, `Data/*`; effect styles `Elevation/Floating`, `Material/Glass`, `Material/Glass Floating`.

Read them with `get_variable_defs` (resolve both modes). Never copy hex values from screenshots.

## iOS output
- `ios-app/Resources/Colors.xcassets/Night/<token>.colorset` with Any (Light) and Dark appearances. Name = token name in camelCase (`textPrimary`).
- `ios-app/Sources/Shared/DesignSystem/DesignTokens.swift` (generated header comment, do not hand-edit): `Color.night.textPrimary`, `Space.s16`, `Radius.lg`, `CaffeineFont.headline` etc.
- Fonts: SF Pro via system font (`Font.system(.headline)` with Dynamic Type); `Data/Display` = 48pt rounded/monospaced digits scaled with `@ScaledMetric`; SF Mono for `Data/Mono *`.

## Android output
- `android-app/app/src/main/kotlin/com/tonapps/caffeine/shared/theme/{CaffeineColors.kt, CaffeineDimens.kt, CaffeineType.kt}` (generated header comment).
- `CaffeineColors` has `dark` and `light` instances; alpha tokens keep their alpha in the ARGB value.
- Fonts: SF Pro is licensed for Apple platforms only, so Android uses the system sans (Roboto) at the same sizes and weights unless Ton picks a brand font; `Data/Mono *` uses Roboto Mono.

## Text style map (default; confirm sizes/weights against Figma on each sync)
| Figma | iOS | Android (sp) |
|---|---|---|
| iOS/Large Title | `.largeTitle` bold | 34 Bold |
| iOS/Title 2 | `.title2` bold | 22 Bold |
| iOS/Title 3 | `.title3` semibold | 20 SemiBold |
| iOS/Headline | `.headline` | 17 SemiBold |
| iOS/Body | `.body` | 17 Regular |
| iOS/Subhead | `.subheadline` semibold | 15 SemiBold |
| iOS/Footnote | `.footnote` semibold | 13 SemiBold |
| iOS/Caption | `.caption` medium | 12 Medium |
| iOS/Caption Upper | `.caption` heavy, uppercase, tracking | 12 Bold, uppercase, letterSpacing |
| Data/Display | 48 bold, monospaced digits | 48 Bold, tnum |

## Rules
- Feature code uses tokens only. A raw colour or spacing value in feature code is a review finding, except the documented exceptions (brand logos, gradients/glows that cannot bind variables).
- Light pill rule: a selected `pill` on a white container becomes `inverse` + `text-on-inverse`. Light text links use `text-primary`, not periwinkle.
- Shadows use `night/shadow` (35% Dark, 12% Light).

## Gate
After generating, `ux-ui-designer` re-reads Figma and diffs every token, both modes, against both outputs. Diff must be empty.

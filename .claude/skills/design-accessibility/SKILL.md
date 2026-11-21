---
name: design-accessibility
description: The accessibility and trust check the Caffeine UX/UI designer runs on every feature's design before Ton approves it - labels and ids, contrast in Dark and Light computed from Figma variables, hit targets, Dynamic Type / font scale, Reduce Motion, colour-not-alone, signed amounts and privacy mode. Output format and how failures are fixed. Loaded by ux-ui-designer.
---

# Design Accessibility

Output: `docs/design/<feature>-a11y.md` — one table row per check per screen: check · element · value measured · threshold · PASS/FAIL · evidence (node id or screenshot).

## Mechanical checks (any miss = FAIL)
1. **Label + id** on every interactive element; id format `<screen>.<element>` (same id on iOS and Android).
2. **Contrast**, both modes, from `get_variable_defs` values (never from screenshots). Small Python script, WCAG relative luminance:
   - body text ≥ 4.5:1
   - large text (≥ 17pt bold or ≥ 24pt) and icons/non-text ≥ 3:1
   Record each foreground/background token pair and its ratio. Known risky pairs (CLAUDE.md Known limitations): mint text on white, periwinkle links in Light, faint Light home indicator, coral on periwinkle.
3. **Hit targets** ≥ 44pt (iOS) / 48dp (Android). A 40pt visual pill is fine if the spec notes the extended hit area.
4. **Amounts** always signed; colour is never the only signal (icon or label too).
5. **Per screen**: Dynamic Type / font-scale behaviour stated (wrap, truncate, or `.minimumScaleFactor` for hero amounts) and Reduce Motion behaviour stated (final state + 0.2 s cross-fade).
6. **Privacy mode** masks every amount (`฿••••••`); counts are not masked.

## Judgment (after all mechanical checks pass)
Copy clarity, VoiceOver / TalkBack reading order, whether the error and empty states tell the user what to do next.

## Fixing failures
The designer owns Figma, so a failing pair is fixed **in Figma** (token swap or Light-mode rule such as the Light pill rule), then re-measured. If the fix changes the brand (a new colour, a hero colour), ask Ton first. Never hide a failure in the spec.

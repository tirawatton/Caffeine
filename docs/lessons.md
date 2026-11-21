# Lessons

The pipeline's memory. Every agent reads this before working. The agent that finds a mistake appends one line at that moment:

`- YYYY-MM-DD [agent-name] (feature): what went wrong -> rule that would have prevented it`

When a lesson repeats across 3 features, fold it into the relevant `.claude/skills/*/SKILL.md` and delete it here.

## Seeded from the Figma work (CLAUDE.md Known limitations)
- 2026-11-21 [setup]: Figma sample data is invented -> bind every figure to a State field; never ship Figma numbers as constants.
- 2026-11-21 [setup]: Hero ring arcs, spend wave and pace marker are drawn per variant in Figma -> draw them from data in code (round caps).
- 2026-11-21 [setup]: Figma text is Inter measured as an SF Pro stand-in -> recheck wraps and truncation with SF Pro (iOS) and Roboto (Android) at large font sizes.
- 2026-11-21 [setup]: Light mode has known contrast gaps (mint text on white, periwinkle links, faint home indicator) -> design-governor checks every Light pair; links use text-primary in Light.
- 2026-11-21 [setup]: 40pt pills and chips in Figma -> extend hit areas to 44pt / 48dp in code.

## Lessons
- 2026-11-21 [setup] (scaffold): `Locale(identifier: "en_US_POSIX")` formats numbers without a thousands separator -> use `en_US` (or an explicit grouping) for display amounts; parity test tables catch this.
- 2026-11-21 [setup] (scaffold): simulator names are duplicated on Ton's Mac and "iPhone 17 Pro" is not installed -> address simulators by `id=$SIM_ID`.
- 2026-11-21 [setup] (scaffold): XcodeGen sets ASSETCATALOG_COMPILER_APPICON_NAME=AppIcon by default and the build fails with no icon set -> keep it empty until the app icon is chosen (Branding page, option A/B/C).

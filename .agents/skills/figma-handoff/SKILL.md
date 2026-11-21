---
name: figma-handoff
description: How to read the Caffeine Figma file (v5.1 page, Feature Journeys, App Prototype) and turn a feature's frames into a platform-neutral design spec both iOS and Android can build from. Access rules, which page is the source of truth, what the spec must contain. Read by ux-ui-designer (the only Figma writer); developers and QA use the spec and screenshots it produces.
---

# Figma Handoff

## Access rules
- File: `jVIND6Rm2KzxmEhO6w2b00` (Caffeine), personal team only.
- **Never access the TISCO FINANCIAL GROUP PUBLIC COMPANY LIMITED organisation** (`organization::1205441950410473811`) for any reason.
- Call `create_session` with the file key before any other Figma tool. Load the `figma:figma-use` skill before any `use_figma` call and `figma:figma-design-to-code` before `get_design_context`.
- **Only `ux-ui-designer` may change the Figma file** (it is the only agent with `use_figma` / `upload_assets`, and it runs the `designer` skill loop). No other agent has any Figma tool, and the main session routes every Figma change to `ux-ui-designer` as Feedback. Link: https://www.figma.com/design/jVIND6Rm2KzxmEhO6w2b00/Caffeine?node-id=482-29722 (Feature Journeys).
- After any Figma change, `ux-ui-designer` re-clones the changed frames onto Feature Journeys and the App Prototype and records node ids in `AGENTS.md`.

## Source of truth
1. **v5.1 page** `446:10036` (🏠 v5.1 — UX journey pass) — the single working page; every screen has a Dark frame and a Light mirror.
2. **Feature Journeys** `482:29722` — step order per feature (sections 01–17); use it to list every screen and state for a feature.
3. **App Prototype** `540:21852` — navigation and motion (push 300 ms slide, sheet 250 ms dissolve, ease cubic-bezier(0.22, 1, 0.36, 1)).
4. **Design System page** — components, variables (`Caffeine / Night`, `Caffeine / Dimensions`), text and effect styles.
5. `AGENTS.md` design rules and Known limitations (sample data is invented; arcs and waves are drawn from data in code; Inter is a stand-in for SF Pro).

Do not use the Home v5, Remaining screens or archived v1–v4 rows for new builds unless the spec says a frame exists only there.

## Spec file: `docs/design/<feature>-spec.md`
1. **Screens**: table of code (e.g. H1, 2A, 10B), name, Dark node id, Light node id, journey step, entry/exit.
2. **Per screen**: layout tree (sections top to bottom with spacing tokens), components used (DS name + variant + overrides), every state (loading, empty, error, offline, privacy, over budget...), copy strings (en; mark th as TODO), data bindings (which State field feeds each text), interactions (tap/swipe/long-press → intent), navigation (push / sheet / full screen) and motion.
3. **Tokens used**: colours (`night/*`), spacing, radii, text styles, effects; flag any raw value with the reason (documented exceptions in AGENTS.md).
4. **Platform notes**: SF Symbol + Material Symbol per icon; iOS-only or Android-only behaviour (Liquid Glass, haptics, back gesture, widgets).
5. **Accessibility**: label, id (`<screen>.<element>`), traits, Dynamic Type / font-scale behaviour, reduced motion.
6. **Gaps**: screens or states the journey needs but Figma lacks (Feature Journeys "Gap" cards, section 14 open questions). Gaps block DESIGN_APPROVED until Ton decides.

## Evidence
Attach `get_screenshot` images of each Dark and Light frame (saved under `docs/design/img/<feature>/`) so engineers can compare without opening Figma.

---
name: ios-swiftui-design
description: Use when a finished UI/UX design (from the designer skill or elsewhere) needs to become modern iOS/SwiftUI implementation guidance — Liquid Glass, SF Symbols, native components, widgets, SwiftUI structure.
---

# iOS/SwiftUI Design

Turn a finished design — Figma frames, a design system, or a plain description — into implementation guidance a SwiftUI developer can build from directly: real view structure, real modifiers, real native equivalents. This is the second half of a two-skill workflow: the **designer** skill produces the design and hands off here. This skill never starts a design from a blank page — if no design has been handed off yet, say so and point back to the designer skill.

Like the designer skill, this runs as a **loop**: set a goal with pass/fail criteria, reason and write, verify, and fix until every criterion passes.

## The loop

```
Start -> Set Goal -> Reason -> Verify -> Pass? --YES--> Exit loop (hand back)
                       ^                  |
                       |                  NO
                       |                  v
                       +----- Fix <--- Feedback
```

| Stage | Question it answers | Output |
|---|---|---|
| **Start** | What was handed off? | Frames, tokens, rules, limitations |
| **Set Goal** | What does "done" look like? | Goal statement + numbered acceptance criteria |
| **Reason** | How should this be built natively? | Token mapping, view structure, code or notes |
| **Verify** | Does it meet every criterion? | PASS/FAIL per criterion, with evidence |
| **Pass?** | All criteria PASS? | YES → exit; NO → feedback |
| **Feedback** | What exactly failed, and why? | List of failures: criterion, where, what's wrong |
| **Fix** | What's the smallest change that fixes it? | Targeted edits only, then back to Reason |

**Loop limit:** at most **3 iterations** of Verify. If criteria still fail after the third, stop, show Ton the remaining failures and options, and ask how to proceed.

---

## 1. Start — take the handoff

From the designer skill (or the user directly), collect:

- The finished screens/frames (Figma link, screenshots, or a description).
- The design-system tokens: colors, spacing/radius scale, text styles, named components.
- The stated design rules (grid system, color ratio) and platform target — **iOS version floor**.
- The designer's final acceptance checklist, and known limitations already flagged (stand-in fonts, placeholder imagery) — carry these forward rather than re-discovering them.

## 2. Set Goal — define "done" before writing

- **Goal:** one sentence — which screens/components, delivered as Swift files or as structured guidance.
- **Acceptance criteria:** a numbered PASS/FAIL checklist, built from:
  1. **Fidelity** — every frame/component in the handoff is covered; variants and states match the design system 1:1.
  2. **Tokens** — every color, spacing, radius and font comes from a named token/constant; zero magic numbers or hex literals in views.
  3. **Native idioms** — SF Symbols where an equivalent exists; real materials/Liquid Glass for glass surfaces; stack/grid layout, not absolute positioning; correct navigation pattern per screen; Swift Charts for charts; WidgetKit for widgets.
  4. **HIG** — 44×44pt tap targets, Dynamic Type scales without breaking, VoiceOver labels on icon-only controls/charts/custom views, every color token has a dark-mode counterpart.
  5. **Builds** — if Swift files are written, they compile for the stated iOS floor (and previews render) where a build is possible; if not possible in this environment, say so.

If a gap would change the implementation (unknown iOS floor, unclear whether an element is interactive), ask Ton once now rather than guessing.

## 3. Reason — map and write

On the first pass this is the full translation; on later passes, re-think only what the feedback touched.

**Map design tokens to SwiftUI.**

- Colors → a `Color` extension or asset-catalog color set per token name (`Color.surfaceRaised`, not a repeated hex literal), preserving light/dark pairing.
- Spacing/radius → named constants (`enum Spacing { static let sm: CGFloat = 8 }`) matching the design system's scale.
- Text styles → nearest Dynamic Type style (`.font(.headline)`) or a custom `Font` extension if the design fixes a type ramp. Prefer Dynamic Type unless the brief fixes sizes.
- Icons → **SF Symbols** wherever a visual equivalent exists (check by name/shape, not just category); keep a custom icon only where none matches.
- Named components (cards, chips, rows) → one SwiftUI `View` struct per component, with the same variants/states.

**Apply modern iOS idioms, don't just port pixels.**

- **Liquid Glass / materials:** real SwiftUI materials (`.ultraThinMaterial`, `.regularMaterial`) or the current Liquid Glass APIs on the target OS — not a flat semi-transparent color.
- **Layout:** `VStack`/`HStack`/`LazyVGrid`/`ScrollView` with modifiers; re-express Figma x/y as a real layout tree.
- **Navigation:** `NavigationStack`, `.sheet`, `.presentationDetents` — name which one each screen/overlay maps to.
- **Charts:** **Swift Charts**, unless the design's treatment isn't expressible there — then say so.
- **Widgets:** **WidgetKit** with the right family (`.systemSmall`/`.systemMedium`); note which elements are interactive (iOS 17+ App Intents/Button) vs. deep links.
- **State & data:** `@Observable` view models; note where a view needs live/async data (e.g. sync status) vs. static content.

## 4. Verify — check every criterion, with evidence

- Go through the acceptance criteria **one by one by number**, marking each **PASS** or **FAIL** with evidence (file/view name, the line or modifier in question, the measured size).
- Scan the code for raw hex values and numeric literals in view code; each one is a FAIL on the Tokens criterion unless it's a documented exception.
- If Swift files were written and a build is possible, build them; a compiler error is a FAIL.
- On later iterations, re-check *all* criteria — a fix can break something that passed.

## 5. Pass? — the decision

- **All PASS → exit the loop.** Go to Hand back.
- **Any FAIL → Feedback**, unless this was the 3rd iteration — then stop and ask Ton.

## 6. Feedback — turn failures into a fix list

For each FAIL, one line: **criterion # · where (file/view) · what's wrong · what "right" looks like.** Example: `#4 · FilterChip · frame 32pt tall · needs 44pt hit area via .contentShape + padding`.

Classify each failure:

- **Implementation issue** → fix it here.
- **Design issue** (no clean native equivalent, the design itself forces a HIG violation, a missing state) → don't silently approximate. Send it back to the **designer** skill as Feedback (it re-enters its loop at Fix), or ask Ton if it's a product decision.

## 7. Fix — smallest targeted change, then loop back

- Change only what the feedback list names.
- Return to **Reason** to confirm the fix fits the overall structure, then run **Verify** again.
- Keep a short loop log: `Iteration n — failed: #… → fixed: …`.

---

## Exit — hand back implementation guidance

Deliver, per screen or component:

- The SwiftUI view structure (real code, or a clear structural description — whichever was asked for). If code was asked for, write and save the Swift files.
- The tokens/constants it depends on.
- Each native substitution made (e.g. "custom chevron → SF Symbol `chevron.right`") and why.
- Anything from the design with no clean native equivalent, named explicitly.
- The final PASS checklist and how many iterations it took.

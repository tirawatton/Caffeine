---
name: ios-swiftui-design
description: Use when a finished UI/UX design (from the designer skill or elsewhere) needs to become modern iOS/SwiftUI implementation guidance — Liquid Glass, SF Symbols, native components, widgets, SwiftUI structure.
---

# iOS/SwiftUI Design

Turn a finished design — Figma frames, a design system, or a plain description — into implementation guidance a SwiftUI developer can build from directly: real view structure, real modifiers, real native equivalents. This is the second half of a two-agent workflow: the **designer** skill produces the design and hands off here; this skill never starts a design from a blank page — if no design has been handed off yet, say so and point back to the designer skill.

## Step 1 — Take the handoff

From the designer skill (or the user directly), collect:

- The finished screens/frames (Figma link, screenshots, or a description).
- The design-system tokens: colors, spacing/radius scale, text styles, named components.
- Any stated design rules (grid system, color ratio, platform target — iOS version floor).
- Known limitations already flagged (stand-in fonts, placeholder imagery, etc.) — carry these forward rather than re-discovering them.

If any of this is missing and the gap would change the implementation (e.g. unknown minimum iOS version, unknown whether an element is interactive), ask once rather than guessing.

## Step 2 — Map design tokens to SwiftUI

- Colors → a `Color` extension or asset-catalog color set per token name (`Color.surfaceRaised`, not a repeated hex literal). Preserve light/dark mode pairing if the design has both.
- Spacing/radius → named constants (`enum Spacing { static let sm: CGFloat = 8 }`) matching the design system's own scale — never a magic number that happens to match.
- Text styles → either map to the nearest Dynamic Type text style (`.font(.headline)`, `.title2`) or a custom `Font` extension if the design uses a fixed type ramp. Prefer Dynamic Type unless the brief explicitly fixes sizes.
- Icons → use **SF Symbols** wherever a visual equivalent exists (check by name/shape, not just by category) instead of reimplementing a custom vector; only keep a custom icon where SF Symbols has no match.
- Named components (cards, chips, rows) → one SwiftUI `View` struct per component, with the same variants/states the design system defines, so the code mirrors the design system 1:1.

## Step 3 — Apply modern iOS idioms, don't just port pixels

- **Liquid Glass / materials:** translate "glass" surfaces to real SwiftUI materials (`.background(.ultraThinMaterial)`, `.background(.regularMaterial)`, or the current Liquid Glass APIs on the target OS) rather than a flat semi-transparent color layer.
- **Layout:** use `VStack`/`HStack`/`LazyVGrid`/`ScrollView` with modifiers, not fixed-frame absolute positioning. A screen built from Figma's x/y coordinates should be re-expressed as a real SwiftUI layout tree.
- **Navigation:** `NavigationStack`, sheets (`.sheet`), and `.presentationDetents` for the bottom-sheet/modal patterns common in the design — name which one each screen/overlay maps to.
- **Charts:** use **Swift Charts** for any data visualization (bar/line/donut) instead of hand-drawn shapes, unless the design's chart treatment is not expressible in Swift Charts — then say so explicitly.
- **Widgets:** if the design includes Home Screen widgets, specify them as **WidgetKit** widgets with the right family size (`.systemSmall`/`.systemMedium`) and note which elements are genuinely interactive (iOS 17+ App Intents/Button in widgets) versus deep-links into the app.
- **State & data:** suggest `@Observable` view models over the data shown, and note where a view needs live/async data (e.g. a sync status) versus static content.

## Step 4 — Check against the Human Interface Guidelines

- Tap targets at least 44×44pt — flag any control inherited from the design that's smaller.
- Dynamic Type: confirm text scales, and that layouts don't break at larger accessibility sizes (wrap rather than truncate where it matters).
- VoiceOver: note `accessibilityLabel`/`accessibilityValue` for icon-only controls, charts, and custom components.
- Dark mode: confirm every mapped color token has a sensible dark-mode counterpart, not just the token's single documented value.

## Step 5 — Hand back implementation guidance

Deliver, per screen or component:

- The SwiftUI view structure (either real code or a clear structural description, matching what the user asked for).
- Which tokens/constants it depends on.
- Any native substitution made (e.g. "custom chevron icon → SF Symbol `chevron.right`") and why.
- Anything from the design that has no clean native equivalent, named explicitly rather than silently approximated.

If the user also wants this written as actual Swift files, write and save them; if they want guidance only, keep it as structured notes the developer can implement from.

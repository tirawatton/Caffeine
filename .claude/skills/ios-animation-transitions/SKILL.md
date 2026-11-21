---
name: ios-animation-transitions
description: Playing animations and screen transitions in SwiftUI for Caffeine - withAnimation and scoped animation, springs, the Figma motion tokens (push 300 ms, sheet 250 ms, ease-out 0.22/1/0.36/1), transitions, matchedGeometryEffect, iOS 18 zoom navigation transitions, sheets and detents, PhaseAnimator and KeyframeAnimator for onboarding, numeric content transitions for amounts, symbol effects, haptics, and Reduce Motion. Loaded by ios-developer.
---

# iOS — Animation and Screen Transitions

## Motion tokens (from the App Prototype `540:21852`)
| Use | SwiftUI |
|---|---|
| Push / pop | native `NavigationStack` push (don't fake a slide) |
| Sheet | native `.sheet` + `.presentationDetents`; dims at 60 % `night/bg` per spec |
| Ease-out | `.timingCurve(0.22, 1, 0.36, 1, duration: 0.3)` |
| User-driven / entrances | `.spring(duration: 0.4, bounce: 0.25…0.5)` |
| Micro (chips, toggles) | 0.15–0.2 s |
Define these once in `Sources/Shared/DesignSystem/Motion.swift`; features use the names, not literals.

## Playing animations
- Animate **state changes**, not views: `withAnimation(.caffeineEaseOut) { store.send(...) }` or `.animation(.caffeineSpring, value: state.x)` scoped to one value. Never the deprecated `.animation(_:)` without `value`.
- **Amounts:** `.contentTransition(.numericText(value:))` so ฿ figures roll instead of cross-fading.
- **Insert/remove:** `.transition(.opacity)`, `.move(edge:)`, `.asymmetric(...)` for alerts, toasts (Unlock toast, Undo toast) and list rows.
- **Shared element:** `matchedGeometryEffect` inside one screen (segment indicator, selected tile ring).
- **Multi-step / keyframed:** `PhaseAnimator` for looping or stepped motion (page 3 orbit drift is the only loop), `KeyframeAnimator` for the onboarding hero keyframes (2.4–2.6 s timelines in the Onboarding v6b notes). Play once when the page settles in the pager, then hold. Copy and buttons never animate.
- **Icons:** `.symbolEffect(.bounce, value:)` for confirmations; `.sensoryFeedback(.success, trigger:)` for saves and unlocks.

## Screen transitions
- Push for drill-down (Home → History, card → detail). iOS 18: `.navigationTransition(.zoom(sourceID:in:))` with `.matchedTransitionSource(id:in:)` for card → detail where the spec asks for it (goal card → goal detail, badge → badge sheet).
- Sheets for tasks (pickers, settle up, reconcile). Full-screen cover for camera scan (2C) and App Lock (12H).
- Tab switches are instant (no animation), as in the prototype.

## Reduce Motion
`@Environment(\.accessibilityReduceMotion)`: replace movement with a 0.2 s cross-fade, show final states immediately, no loops, no parallax. Zoom transitions fall back to the default push.

## Verify
Preview each animated state; record a simulator video for any motion AC; check no animation runs while idle (battery).

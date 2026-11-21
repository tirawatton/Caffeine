---
name: ios-core-animation
description: Core Animation and custom drawing for Caffeine iOS - when to use SwiftUI Shape, Canvas and TimelineView versus CALayer, drawing the budget ring and arc gauge with round caps, animating strokeEnd, model vs presentation layers, timing functions matching the Figma motion curve, the spend wave and particle effects, render performance (offscreen passes, shadowPath, drawingGroup) and Reduce Motion. Loaded by ios-developer.
---

# iOS — Core Animation and Custom Drawing

Figma draws the hero ring, arc gauge, spend wave and onboarding particles as static vectors; the app must **draw them from data** (CLAUDE.md Known limits).

## Pick the lowest layer that works
1. **SwiftUI `Shape` + `.trim(from:to:)` + `.stroke(style: StrokeStyle(lineWidth:, lineCap: .round))`** — budget ring, arc gauge track and fill, pace tick. Animate by changing the trim value inside `withAnimation`. Use round caps (Figma shows square ends).
2. **`Animatable` / `animatableData`** on a custom `Shape` when a value other than trim must interpolate (e.g. the 240° arc from 150° to 390°, the pace needle angle).
3. **`Canvas` (+ `TimelineView(.animation)` only while animating)** — the spend wave from daily data, charts with many points. Stop the timeline when idle.
4. **`CALayer` via `UIViewRepresentable`** — only when SwiftUI can't: `CAEmitterLayer` for the onboarding page 2 particles, `CAShapeLayer` path morphing, or 60 fps effects that SwiftUI re-renders too often.

## Core Animation essentials (when you do use layers)
- `CAShapeLayer` with `path`, `strokeEnd`, `lineCap = .round`; animate `strokeEnd` with `CABasicAnimation(keyPath: "strokeEnd")`.
- **Model vs presentation:** set the model value first, then add the animation from the old value; never rely on `fillMode = .forwards` + `isRemovedOnCompletion = false` to keep a final state.
- Group related changes in `CATransaction`; disable implicit animations (`setDisableActions(true)`) for instant updates.
- Motion curve from the prototype: `CAMediaTimingFunction(controlPoints: 0.22, 1, 0.36, 1)` (SwiftUI: `.timingCurve(0.22, 1, 0.36, 1, duration:)`).
- `cornerCurve = .continuous` to match Figma squircles.

## Performance
- Shadows: set `shadowPath` (or use the token shadow in SwiftUI once per container), never per row.
- Avoid offscreen passes: masks + shadows + blur on the same scrolling layer; glass blur only on bars/sheets (`ios-swiftui-design`).
- `.drawingGroup()` for complex static vector composites (onboarding hero), not for text-heavy views.
- Don't animate layout of a whole list; animate the one element that changed.
- Verify with Instruments **Animation Hitches** / Core Animation FPS on a real device when a task has a motion AC.

## Accessibility
`@Environment(\.accessibilityReduceMotion)`: show the final state (ring at value, wave drawn) with at most a 0.2 s opacity fade. Drawings need an accessibility element with a text summary (e.g. "84% of budget used, ฿537 a day left").

---
name: android-core-graphics
description: Custom drawing and low-level animation for Caffeine Android, the counterpart of iOS Core Animation - Compose Canvas and DrawScope for the budget ring, arc gauge, pace needle and spend wave, drawWithCache, graphicsLayer, Animatable driving the draw phase only, the Figma motion curve, RenderEffect blur on API 31+, render performance and reduced motion. Loaded by android-developer.
---

# Android — Core Graphics and Drawing (Core Animation counterpart)

Figma draws the hero ring, arc gauge, spend wave and onboarding particles as static vectors; the app must **draw them from data**, matching iOS.

## Drawing
- **`Canvas` / `Modifier.drawBehind` / `drawWithCache`** with `DrawScope`:
  - ring and arc gauge: `drawArc(startAngle, sweepAngle, useCenter = false, style = Stroke(width, cap = StrokeCap.Round))` — round caps; the 240° gauge starts at 150°.
  - pace tick / needle: `rotate(degrees) { drawLine(...) }`.
  - spend wave: build a `Path` from daily data inside `drawWithCache` so it is rebuilt only when the data or size changes.
- Gradients and glows: `Brush.radialGradient` / `linearGradient` (raw hex stops are the documented exception in AGENTS.md).
- Sizes from `CaffeineDimens` converted with `toPx()` inside the draw scope.

## Animating drawings cheaply
- Hold progress in an `Animatable` (or `animateFloatAsState`) and **read it inside the draw lambda** (`drawWithCache { onDrawBehind { … progress.value … } }`) so changes trigger redraw only — no recomposition, no relayout.
- Transforms, alpha and scale through `Modifier.graphicsLayer { }` (lambda form), never by changing layout size each frame.
- Curve from the prototype: `CubicBezierEasing(0.22f, 1f, 0.36f, 1f)`; durations from `android-animation-transitions` motion tokens.
- Particles (onboarding page 2): a small particle list advanced in `withFrameNanos` inside a `LaunchedEffect`, drawn in one `Canvas`; stop when the page leaves.

## Platform limits
- Blur (glass): `Modifier.blur` / `RenderEffect` only on API 31+; below that, the solid `glass-*` token fill + 1dp `glass-stroke` (`compose-craft`).
- Avoid overdraw: one background per surface; check with "Debug GPU overdraw" on a device.
- Shadows: `Modifier.shadow` with the token elevation once per container, not per row.

## Accessibility
When animations are off (animator duration scale 0, or the in-app reduce-motion setting) draw the final state at once. Each drawing gets `Modifier.semantics { contentDescription = "84% of budget used, ฿537 a day left" }` matching iOS.

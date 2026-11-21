---
name: android-animation-transitions
description: Playing animations and screen transitions in Jetpack Compose for Caffeine - the shared motion tokens (push 300 ms, sheet 250 ms, ease-out 0.22/1/0.36/1, springs), animate*AsState, updateTransition, AnimatedVisibility, AnimatedContent for rolling amounts, keyframes, infinite transitions, shared element transitions, Navigation Compose enter/exit transitions, bottom sheets, predictive back, haptics, and reduced motion. Loaded by android-developer.
---

# Android — Animation and Screen Transitions

## Motion tokens (same values as iOS, from the App Prototype `540:21852`)
Define once in `shared/theme/CaffeineMotion.kt`; features use the names, not literals.
| Use | Compose |
|---|---|
| Ease-out | `CubicBezierEasing(0.22f, 1f, 0.36f, 1f)` |
| Push / pop | `tween(300, easing = EaseOutCaffeine)` slide + fade |
| Sheet | `ModalBottomSheet` (its own motion); scrim 60 % `night/bg` |
| User-driven / entrances | `spring(dampingRatio = 0.7f…0.8f, stiffness = Spring.StiffnessMediumLow)` |
| Micro (chips, toggles) | `tween(150–200)` |

## Playing animations
- **Single values:** `animateFloatAsState`, `animateColorAsState`, `animateDpAsState` with a `label` (shows in the Animation Preview).
- **Several values from one state:** `updateTransition(targetState = state.status)` (On track / Over pace / Over budget hero).
- **Appear/disappear:** `AnimatedVisibility` with `fadeIn() + slideInVertically()` for toasts (Undo, Unlock) and alerts; `animateItem()` on `LazyColumn` items for insert/remove.
- **Changing content:** `AnimatedContent(targetState = amount)` with a vertical slide so ฿ figures roll like iOS `numericText`.
- **Keyframed onboarding:** `keyframes { durationMillis = 2400; … }` per element, played once when the pager page settles (`pagerState.settledPage`), then held. Copy and buttons never animate. `rememberInfiniteTransition` only for the page 3 orbit drift.
- **Haptics:** `LocalHapticFeedback` / `HapticFeedbackConstants.CONFIRM` (API 30+, fallback `VIRTUAL_KEY`) on saves and unlocks.

## Screen transitions
- Navigation Compose `NavHost(enterTransition = …, exitTransition = …, popEnterTransition = …, popExitTransition = …)` with the push tokens: `slideIntoContainer(SlideDirection.Start, tween(300, easing = EaseOutCaffeine))`.
- Shared element (card → detail, where the spec asks: goal card → goal detail, badge → badge sheet): `SharedTransitionLayout` + `Modifier.sharedElement(rememberSharedContentState(key), animatedVisibilityScope)`.
- Sheets for tasks (pickers, settle up, reconcile); full-screen destinations for camera scan (2C) and App Lock (12H). Tab switches are instant.
- Predictive back (API 34+): default NavHost back animation; custom only via `PredictiveBackHandler`; below 34 the normal pop transition.

## Reduced motion
Compose scales animation durations by the system animator duration scale, so with animations off most finish instantly. Infinite transitions, `withFrameNanos` loops and manually driven `Animatable`s must check it (`Settings.Global.ANIMATOR_DURATION_SCALE == 0f`) or the in-app reduce-motion setting and show the final state with at most a 200 ms fade.

## Verify
Animation Preview in Android Studio for each transition; screen-record the emulator for any motion AC; nothing animates while idle.

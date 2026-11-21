---
name: android-app-lifecycle
description: Android app, process and activity lifecycle for Caffeine - single-activity Compose app, startup cost, lifecycle-aware collection, configuration changes vs process death with SavedStateHandle, app foreground and background via ProcessLifecycleOwner, App Lock with BiometricPrompt, FLAG_SECURE privacy in recents, WorkManager backup, Glance widget updates, deep links, predictive back, and onTrimMemory. Loaded by android-developer.
---

# Android — App Lifecycle

## Entry and startup
- Single `MainActivity` (`ComponentActivity`, `enableEdgeToEdge()`, `setContent { CaffeineTheme { AppNavHost() } }`). `Application.onCreate` only initialises Hilt and cheap singletons — no database queries, no network.
- Room is created lazily by Hilt as a singleton. A failed migration shows an error screen, never a crash.
- Add a Baseline Profile once the first screens exist (startup and Home scroll).

## Lifecycles to respect
| Event | Survives | Use |
|---|---|---|
| Configuration change (dark mode, font scale, locale, window size, rotation if enabled) | ViewModel | keep state in the ViewModel, never in the Activity |
| Process death (system kills app in background) | `SavedStateHandle`, Room | save navigation args, in-progress keypad amount, selected filters in `SavedStateHandle`; reload the rest from Room |
| App to background / foreground | — | `ProcessLifecycleOwner` observer in one `AppLifecycleObserver` |
- Collect flows with `collectAsStateWithLifecycle()` so collection stops below STARTED. One-off lifecycle work in composables: `LifecycleEventEffect` / `LifecycleStartEffect`.

## Foreground / background behaviour (parity with iOS)
| Transition | Do |
|---|---|
| → background | Room writes are already committed (suspend calls finish); record the time; enqueue backup; update widgets if data changed |
| Privacy Mode or App Lock on | `window.addFlags(FLAG_SECURE)` so recents shows no amounts (also blocks screenshots — say so in Settings copy) |
| → foreground | App Lock on and background longer than the timeout → show the 12H lock with `BiometricPrompt` (`BIOMETRIC_STRONG or DEVICE_CREDENTIAL`) before data; refresh "today" past midnight / cycle start |

## Background work
- Backup: `WorkManager` unique periodic/one-time work with network constraint; idempotent; surfaces "Backup failed / Waiting for network" from `WorkInfo`.
- Widgets (Glance): `XxxWidget().updateAll(context)` once per user action that changes widget data.

## Navigation
- Deep links and widget taps via Navigation Compose `deepLinks`; type-safe routes.
- Predictive back: `android:enableOnBackInvokedCallback="true"`; custom back handling only through `BackHandler`/`PredictiveBackHandler`.

## Memory pressure
`ComponentCallbacks2.onTrimMemory(level)` ≥ `TRIM_MEMORY_UI_HIDDEN`: clear image caches and slip thumbnails (`android-concurrency-memory`).

---
name: ios-app-lifecycle
description: iOS app and scene lifecycle for Caffeine - SwiftUI App entry, scenePhase handling, launch cost, privacy cover in the app switcher, App Lock on return, saving on background, background tasks for iCloud backup, widget reloads, deep links, state restoration and memory warnings. Loaded by ios-developer.
---

# iOS — App Lifecycle

## Entry and launch
- `@main struct CaffeineApp: App` creates the `ModelContainer` **once** and injects repositories into the root; no other place creates containers.
- Keep `init` and the first `body` cheap: no network, no migration UI, no large fetches before the first frame. Load data in the screen's `.task`.
- Migrations run when the container opens; a failed migration shows an error screen, never `fatalError` (`swift-style`: no crashes for recoverable states).

## Scene phase (`@Environment(\.scenePhase)`)
| Transition | Do |
|---|---|
| → `.inactive` | If Privacy Mode or App Lock is on, show the privacy cover immediately (the app-switcher snapshot is taken now) |
| → `.background` | Make sure pending SwiftData changes are saved; record the time; schedule the backup task; reload widgets if data changed |
| → `.active` | If App Lock is on and the app was in background longer than the lock timeout, present the 12H lock (`LocalAuthentication`, `LAContext.evaluatePolicy(.deviceOwnerAuthentication…)`) before showing data; remove the privacy cover; refresh "today" (date may have changed past midnight or a cycle start) |
Handle phases in one place (the root view or an `AppLifecycle` object), not in every screen.

## Background work
- iCloud backup: `BGProcessingTask` registered in `Info.plist` (`BGTaskSchedulerPermittedIdentifiers`) via SwiftUI `.backgroundTask(.appRefresh(...))` / `BGTaskScheduler`. Always set an expiration handler and finish the task; assume it may never run (the "Backup failed / Waiting for network" states exist for that).
- Widgets: after any write that changes widget data, `WidgetCenter.shared.reloadTimelines(ofKind:)` — once per user action, not per row.

## Navigation state
- Deep links / widget taps: `.onOpenURL` routes through the app Router into the typed `NavigationStack` path.
- Restoration: selected tab and simple selections in `@SceneStorage`; never money or personal data there.

## Memory pressure
Listen for `UIApplication.didReceiveMemoryWarningNotification` (or use `NSCache`, which purges itself) and drop image caches and slip thumbnails. Never hold full-resolution slip photos in memory (`ios-concurrency-memory`).

## Store and task lifetime
A Store lives as long as its root view's identity. Work started with `.task { await store.… }` is cancelled automatically when the view disappears; prefer it over unowned `Task {}` for long-running observation.

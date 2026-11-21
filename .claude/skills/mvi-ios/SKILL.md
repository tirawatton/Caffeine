---
name: mvi-ios
description: The iOS MVI pattern for Caffeine (State struct, Intent enum, @MainActor @Observable Store, Repository protocol) - no MVVM, no ObservableObject. Read by ios-architect, ios-ui-engineer, ios-reviewer and solo-builder.
---

# MVI on iOS (Swift 6, iOS 18+)

Flow: View → Intent → Store (reducer + effects) → State → View. Persistence only through a Repository protocol.

```swift
struct HomeState: Equatable {
    var hero: BudgetHero = .loading      // explicit enum, no optional soup
    var recent: [TransactionRow] = []
    var alert: HomeAlert?
}

enum HomeIntent {
    case appeared
    case seeAllTapped
    case transactionTapped(id: UUID)
}

@MainActor @Observable
final class HomeStore {
    private(set) var state = HomeState()
    private let transactions: TransactionRepository
    private let clock: () -> Date

    init(transactions: TransactionRepository, clock: @escaping () -> Date = Date.init) {
        self.transactions = transactions
        self.clock = clock
    }

    func send(_ intent: HomeIntent) {
        switch intent {
        case .appeared: Task { await load() }
        case .seeAllTapped, .transactionTapped: break // navigation via a Router passed in
        }
    }

    private func load() async { /* repository calls, then state = ... */ }
}

struct HomeView: View {
    @State private var store: HomeStore
    var body: some View { /* reads store.state, calls store.send(...) */ }
}
```

## Rules
- One Store per screen/feature lifetime, held in `@State` by the root View.
- Views only send Intents. No repository calls, no business logic in `body`.
- State is the only source of truth; no `@State` copies of state fields (UI-local focus/scroll state is fine).
- `send` is synchronous; async work runs in a Task owned by the Store.
- Repository protocols are `Sendable`; implementations live in `Sources/Repositories/`.
- Inject `clock`, `calendar` and `locale` so date maths are testable.
- Forbidden: `ObservableObject`, `@StateObject`, `@ObservedObject`, `@Published`, `@Query` / `ModelContext` in Views or Stores.
- Navigation: `NavigationStack` with a typed path owned by the app Router; sheets driven by State.

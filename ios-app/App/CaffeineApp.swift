import SwiftUI

@main
struct CaffeineApp: App {
    var body: some Scene {
        WindowGroup {
            RootView()
        }
    }
}

/// Placeholder root. Replaced by the tab shell (Home · Wallet · Analytics · Profile)
/// when the first feature runs through the pipeline.
struct RootView: View {
    var body: some View {
        Text("Caffeine")
            .font(.largeTitle.bold())
            .accessibilityIdentifier("root.title")
    }
}

#Preview("Dark") { RootView().preferredColorScheme(.dark) }
#Preview("Light") { RootView().preferredColorScheme(.light) }

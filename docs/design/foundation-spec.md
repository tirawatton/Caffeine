# foundation — design spec (E00)

Author: `ux-ui-designer` · 2026-11-21 · Plan: `docs/plan/foundation-plan.md` revision 7 · Figma file `jVIND6Rm2KzxmEhO6w2b00`, v5.1 page `446:10036`, section **N · Foundation** `620:37505`.
Status: **DESIGN_READY** (draft until Ton approves at GATE 1). Accessibility: `docs/design/foundation-a11y.md`. Tokens: `docs/design/tokens.json`, `docs/design/tokens-changelog.md`.

## 0. Goal and acceptance criteria (Set Goal)

**Goal:** give both apps the token files and the four foundation surfaces they need before any feature (splash, secure-store failure, app-switcher shield, tab placeholders), so the shell can be built without guessing.

| # | Criterion | Result | Evidence |
|---|---|---|---|
| 1 | Token pipeline exists: Figma export → `docs/design/tokens.json` → iOS colour sets + `DesignTokens.swift`, Android `CaffeineColors/Dimens/Type.kt`, each with the generated header | PASS | `scripts/tokens/{common,generate,diff}.py`; `generate.py` prints 36 colours × 2 modes, 22 dimensions, 15 text styles, 3 effects |
| 2 | AC-01: `shadow` Dark alpha 0.35 / Light 0.12; Android `0x59000000` / `0x1F000000` | PASS | `Night/shadow.colorset` alpha 0.350 / 0.120; `CaffeineColors.kt` lines `shadow = Color(0x59000000)` / `Color(0x1F000000)` |
| 3 | AC-01a: `income-text` Dark #9EE6C4 / Light #1F714C; Light `accent` #CF3D20; Light `textSecondary` #636366 | PASS | `Night/income-text.colorset`; Android `incomeText = Color(0xFF9EE6C4)` / `Color(0xFF1F714C)`, `accent = Color(0xFFCF3D20)`, `textSecondary = Color(0xFF636366)` (light) |
| 4 | AC-01b: `on-primary-soft` alpha 0.88 both modes, `0xE01C1C1E`; Light `on-accent-soft` `0xF5FFFFFF`, Dark `0xE01C1C1E`; no opaque colour + separate opacity | PASS | colour sets store alpha in the colour; Kotlin ARGB carries the alpha |
| 5 | AC-02: token diff = 0 for iOS and Android, both modes | PASS | `python3 scripts/tokens/diff.py` prints `0` (exit 0); a fresh Figma re-read (36 tokens × 2 modes) vs the generated Kotlin: 0 diffs |
| 6 | AC-03: a renamed `night/bg-clear` stops generation with "missing token: night/bg-clear" and leaves files byte-identical | PASS | negative run: exit 2, `shasum -c` OK on `DesignTokens.swift` and `CaffeineColors.kt` |
| 7 | Both apps compile with the generated files | PASS (with a scaffold caveat) | iOS `xcodebuild … build` BUILD SUCCEEDED; Android `:app:compileDebugKotlin` BUILD SUCCESSFUL using the cached Gradle 8.13 and `-Pandroid.useAndroidX=true` (the scaffold has no `gradlew` and no `gradle.properties`, T-04) |
| 8 | DG-52: global variables and DS main components carry the Home v5 / audit values; no pins or overrides on the Home v5 page | PASS | DS scan of 261 main components: 0 texts bound to `night/income` (7 bound to `income-text`), 0 unbound text fills; 14 faded `text-on-light` labels (Stat tile, Wallet card legacy) moved to `on-primary-soft` at 100%; Picker tile label `68:478` = `on-primary-soft`; Budget hero v5 `400:452` / Metric hero v5 `406:1610` (read only): 0 faded, 0 income-bound, 0 unbound |
| 9 | DG-01 splash, DG-22 store error (+ retrying), DG-26 shield exist as Dark + Light pairs on the v5.1 page | PASS | 8 frames in section N (§1) |
| 10 | 8pt grid and tokens: every fill/stroke bound, every text styled, every padding/gap bound to `space/*`; 16pt margins; bottom action 40pt from the bottom | PASS | audit of section N: 0 unbound paints, 0 unstyled texts, 0 raw spacing; Retry is 370×56, 40pt above the bottom |
| 11 | Copy: real, platform-neutral (no iPhone / iCloud, DG-49 rule), tells the user what to do next, never suggests deleting the app | PASS | §2.2 copy |
| 12 | Accessibility: label + id on every interactive element, contrast ≥ 4.5:1 text / 3:1 non-text both modes, hit targets ≥ 44pt / 48dp, Dynamic Type and Reduce Motion stated | PASS | `foundation-a11y.md` (15 contrast pairs, all PASS) |
| 13 | DG-23 tab placeholders confirmed scaffold only | PASS | §2.5 |

Loop log: Verify iteration 1 failed #7 (Android: a generated KDoc containing `iOS/*` opened a nested comment, "Unclosed comment") and #11 (the store error message wrapped a lone "again." line) → fixed (comment text; shorter message) → iteration 2 all PASS.

**Out of scope:** App Lock prompt (E06, DG-02), Theme setting (E05), app icon (Ton to pick A/B/C on the Branding page), Thai copy (Q-19), the wordmark image asset export (§4).

## 1. Screens

| Code | Name | Dark | Light | Journey step | Entry → exit |
|---|---|---|---|---|---|
| F1 | Splash | `620:37506` | `620:37602` | Journey 01 step "F1 · Splash" (Feature Journeys copy `625:26698`, replaced the Gap card); App Prototype `625:44449` (flow 01 now starts here, 0.5 s → O6·1) | App launch → (store OK) launch gate → tab shell / first run; (store fails) → F2 |
| F2 | Store error · STORE-DB-01 | `620:37527` | `620:37611` | none (error branch of F12) | F1 failure → F2; Try again → F3 |
| F3 | Store error · Retrying | `620:37561` | `620:37625` | none | F2 Try again → F3 → (success) launch gate → Home; (failure) → F2 same code |
| F4 | Privacy shield | `620:37593` | `620:37639` | none (system transition) | App goes inactive / background → F4; foreground → previous tab and stack |
| — | Tab root placeholders | none | none | — | scaffold only (DG-23) |

Screenshots: `docs/design/img/foundation/` (`F1-splash-{dark,light}.png`, `F2-store-error-…`, `F3-store-error-retrying-…`, `F4-privacy-shield-…`, `section-N-overview.png`).

## 2. Per screen

### 2.1 F1 Splash (DG-01, T-20)
- **Layout:** full screen `night/bg`. The chosen app logo (wordmark + splash strokes, source `533:49904`, Branding `504:329`) centred horizontally and vertically, 240pt wide (≈ 240×76). Nothing else: no spinner, no tagline, no copy, no motion (it shows for under 0.5 s; a spinner would only flash).
- **Tokens:** background `night/bg`; logo ink `night/accent` (Dark #FF6A4D, Light #CF3D20; brand asset, may ship as an image with Dark / Light variants).
- **States:** one. Init success → launch gate (passes through in foundation) → shell; failure → F2. Never shows Home behind it.
- **iOS:** `UILaunchScreen` in `project.yml`: `UIColorName: Night/bg` (the generated colour set, namespace `Night`), `UIImageName:` the wordmark image asset (Dark / Light appearances), `UIImageRespectsSafeAreaInsets: true`. The in-app `splash.screen` view (shown while T-07 / T-09 finish) draws the same composition so the hand-off is invisible.
- **Android 12+:** SplashScreen API: `windowSplashScreenBackground` = `night/bg` (values / values-night), `windowSplashScreenAnimatedIcon` = the wordmark as a vector drawable, **sized to fit the 192dp safe circle of the 288dp icon area (wordmark max 176dp wide)**, no icon background, `postSplashScreenTheme` → app theme. API 28–30: same through `androidx.core:core-splashscreen`. Keep the splash on screen with `setKeepOnScreenCondition` until the store is open.
- **Accessibility:** id `splash.screen`; the logo image is decorative to VoiceOver / TalkBack except one label "Caffeine" on the container; no focusable controls.
- **Motion:** none. Reduce Motion: no change.

### 2.2 F2 Store error (DG-22, T-10)
Layout tree (frame 402×874, `night/bg`, no tab bar, no navigation):
```
Content  x16 y64 w370 h770 (bottom 40pt from the frame bottom)
├─ Message  (FILL height, centred both axes, gap space/16)
│  ├─ Icon tile 64×64  night/surface-raised, radius/full · icon/lock 32pt, stroke night/text-primary
│  ├─ Title       iOS/Title 2, night/text-primary, centred
│  ├─ Message     iOS/Body, night/text-secondary, centred, 338 wide (wraps)
│  └─ Code chip   night/surface-raised, radius/full, padding space/8 · space/16 · Data/Mono Caption, night/text-secondary
└─ Actions  (gap space/16, centred)
   ├─ Button Primary (DS Button 68:462) FILL 370×56 · icon/restore · label "Try again"
   └─ Help        iOS/Footnote Regular, night/text-secondary, centred, 338 wide
```
- **Copy (en; th = TODO, Q-19):**
  - Title: "We can't open your data"
  - Message: "Your data is still on this device. Caffeine couldn't unlock it this time."
  - Code chip: "Error code STORE-DB-01" or "Error code STORE-KEY-01" (the only difference between the two failures)
  - Button: "Try again"
  - Help: "Still stuck? Restart your phone, then open Caffeine. Don't delete the app: that erases anything you haven't backed up."
  - Platform-neutral on purpose ("device", "phone"): the same strings ship on Android (DG-49 rule).
- **Data bindings:** `StoreErrorState.code` (`STORE-KEY-01` | `STORE-DB-01`) → code chip. No other data, no amounts, nothing from the store.
- **Interactions:** Try again → intent `retryOpenStore` → F3. No back / dismiss: Android system back on F2 moves the app to the background (there is nothing behind it). Never offers "Reset" or "Delete data" (T-10: data is never deleted automatically).
- **Tokens:** see §3. Button Primary = `night/accent` fill, label + icon `night/text-on-accent`.
- **Dynamic Type / font scale:** Title and Message wrap (no truncation); the Message block scrolls if it no longer fits above Actions at the largest sizes (wrap Content in a scroll view; Actions stay pinned). Button label one line, may grow the button height (min 56).

### 2.3 F3 Store error · Retrying
- Same as F2; the button shows "Trying again…" and is disabled (whole button at 40% opacity, the file's disabled convention). Code chip unchanged.
- VoiceOver: button reads "Trying again", trait busy / not enabled; announce "Trying again" once on entry.
- Ends on success (launch gate → Home with `tab.home` selected, AC-21) or failure (back to F2, same code, focus returns to the Title).
- Minimum display: none; if the retry finishes in < 300 ms the label may not change visibly, which is fine.

### 2.4 F4 Privacy shield (DG-26, T-21)
- **Layout:** identical to F1 (one shared `BrandCover` view: `night/bg` + centred 240pt wordmark). Solid cover, **not a blur**: a blur of a 48pt hero amount can still be read in the app-switcher thumbnail.
- **When:** every transition to inactive / background, whatever App Lock or Privacy Mode is set (Ton Q-04). Removed on foreground with no animation (instant), showing the same tab and stack.
- **E06 reuse:** with App Lock on, the lock prompt (Face ID / passcode, DG-02) sits on top of this cover; nothing else changes.
- **Fallback (T-21 error behaviour):** a plain `night/bg` window cover without the logo is acceptable.
- **Accessibility:** id `privacy.shield`; not focusable; no announcement.
- **Reduce Motion:** no animation in either case.

### 2.5 DG-23 Tab root placeholders: confirmed scaffold only
No frame. Each tab root shows its Large Title ("Home", "Wallet", "Analytics", "Profile"; `iOS/Large Title`, `night/text-primary`) at x16 y64 on `night/bg`, ids `home.placeholder` / `wallet.placeholder` / `analytics.placeholder` / `profile.placeholder`, above the DS Tab bar `State=No add` (`272:990`) 40pt from the bottom with the `surface-raised` active capsule. Never shipped to beta; each feature replaces its placeholder with its v5.1 frame.

## 3. Tokens used
| Kind | Tokens |
|---|---|
| Colour | `night/bg`, `night/surface-raised`, `night/text-primary`, `night/text-secondary`, `night/accent`, `night/text-on-accent` |
| Spacing | `space/8`, `space/16`; content x16 y64; bottom 40 |
| Radius | `radius/full` (icon tile, code chip); Button keeps its DS radius |
| Text | `iOS/Title 2`, `iOS/Body`, `iOS/Footnote Regular`, `Data/Mono Caption` (DM Mono in Figma = SF Mono on iOS, system monospace on Android) |
| Effects | none |
| Raw values | the wordmark artwork (brand asset; colours = `night/accent` per mode) |

### 3.1 Token pipeline (T-01)
- Run: `python3 scripts/tokens/generate.py` then `python3 scripts/tokens/diff.py` (must print `0`). Source: `scripts/tokens/figma-export.json` (a read-only `use_figma` export, re-exported on every token change).
- **iOS:** `ios-app/Resources/Colors.xcassets/Night/<token>.colorset` (folder provides the `Night` namespace; Any = Light, Dark = Dark; alpha stored in the colour), `ios-app/Sources/Shared/DesignSystem/DesignTokens.swift`: `Color.night.<camelCase>`, `Space.s0…s64`, `Radius.sm…full`, `Size.*`, `Layout.tabBarInset / rowDividerInset`, `CaffeineFont.<style>` (`CaffeineTextStyle` with size, line height, weight, tracking in pt, uppercase, monospaced, Dynamic Type anchor; `.font`), `CaffeineEffect.*` (SwiftUI shadow radius = Figma blur / 2).
- **Android:** `CaffeineColors.dark` / `.light` (`0xAARRGGBB`), `CaffeineDimens` (dp, including effect offsets / blurs), `CaffeineType` (`TextStyle`, Roboto via `FontFamily.Default`, mono via `FontFamily.Monospace`, `Data/Display` with `tnum`; names in `CaffeineType.UPPERCASE` render upper case).
- Colour set file names are the Figma names in kebab case (`income-text.colorset`, as AC-01 / AC-01a are written); the Swift and Kotlin accessors are camelCase (`incomeText`).
- 5 legacy tokens (`hero`, `hero-start`, `hero-end`, `hero-rim`, `hero-text-secondary`) are still Figma variables but unused since v5; they are generated and marked deprecated in Swift / Kotlin. The `Caffeine / Bento` collection (unused) is not exported.

## 4. Platform notes
| Element | SF Symbol | Material Symbol |
|---|---|---|
| Lock tile (F2) | `lock` | `lock` |
| Try again | `arrow.counterclockwise` | `restart_alt` |
- Status bar and home indicator are drawn by the OS (DG-50). Splash on iOS = `UILaunchScreen`; Android = SplashScreen API (§2.1).
- Android recents: T-21 also calls `setRecentsScreenshotEnabled(false)` on API 33+; no FLAG_SECURE (Q-31).
- **Wordmark asset:** export node `533:49904` (Dark) / `533:49910` (Light) from Figma as PDF (iOS, "Preserve Vector Data", Any + Dark appearances) and SVG → vector drawable (Android). The MCP export includes the frame background, so the developer exports it from the Figma UI ("Export selection", background off) or asks ux-ui-designer for the cleaned files.

## 5. Accessibility (summary; full table in `foundation-a11y.md`)
| Element | id | Label | Traits |
|---|---|---|---|
| Splash container | `splash.screen` | "Caffeine" | image, not focusable children |
| Store error screen | `storeError.screen` | — | container; VoiceOver starts on the Title (header) |
| Title | `storeError.title` | "We can't open your data" | header |
| Code chip | `storeError.code` | "Error code STORE-DB-01" (reads the code letter by letter via `.speechSpellsOutCharacters` / `ttsSpan`) | static text |
| Try again | `storeError.retry` | "Try again"; hint "Opens your data again" | button; F3: not enabled, busy, label "Trying again" |
| Help text | `storeError.help` | the help string | static text |
| Privacy shield | `privacy.shield` | — | hidden from accessibility |
| Tab placeholders | `<tab>.placeholder` | the tab name | header |

## 6. Gaps and questions (none blocks DESIGN_READY)
1. **App icon** is still not chosen (Branding page options A/B/C). The splash uses the wordmark, so it does not need the icon, but Android 12+ shows the launcher icon in some system surfaces. Ton to pick.
2. **Wordmark image asset** (iOS PDF / Android vector) needs a clean export (§4); owner ux-ui-designer on request, or the developer from the Figma UI.
3. **Legacy hero tokens** in `Caffeine / Night` (5) and the unused `Caffeine / Bento` collection: delete them from Figma? (Conservative choice made: kept, generated as deprecated.)
4. **Thai copy** for F2 / F3 waits for Q-19.

# foundation — accessibility check (E00)

Author: `ux-ui-designer` · 2026-11-21 · Frames: v5.1 section N `620:37505` · Spec: `docs/design/foundation-spec.md`.
Contrast is computed from the `Caffeine / Night` values read with `use_figma` (WCAG 2.x relative luminance), never from screenshots. Result: **all mechanical checks PASS.**

## 1. Label + id (every interactive element)
| Screen | Element | id | Label | Result |
|---|---|---|---|---|
| F1 | Splash container | `splash.screen` | "Caffeine" | PASS (no interactive element) |
| F2 / F3 | Screen | `storeError.screen` | — | PASS |
| F2 / F3 | Title | `storeError.title` | "We can't open your data" (header) | PASS |
| F2 / F3 | Code chip | `storeError.code` | "Error code STORE-DB-01" / "STORE-KEY-01", spelled out | PASS |
| F2 | Try again | `storeError.retry` | "Try again", hint "Opens your data again" | PASS |
| F3 | Try again (busy) | `storeError.retry` | "Trying again", not enabled, busy | PASS |
| F2 / F3 | Help | `storeError.help` | help string | PASS |
| F4 | Shield | `privacy.shield` | hidden from accessibility | PASS |
| — | Tab placeholders | `home/wallet/analytics/profile.placeholder` | tab name, header | PASS |

## 2. Contrast (both modes)
| Mode | Pair | Foreground / background | Ratio | Threshold | Result | Evidence |
|---|---|---|---|---|---|---|
| Dark | text-primary on bg (Title) | #FFFFFF / #1C1C1E | 17.01:1 | 4.5:1 | PASS | `620:37548` |
| Dark | text-secondary on bg (Message, Help) | #AEAEB2 / #1C1C1E | 7.69:1 | 4.5:1 | PASS | `620:37549`, `620:37560` |
| Dark | text-secondary on surface-raised (code chip) | #AEAEB2 / #3A3A3C | 5.13:1 | 4.5:1 | PASS | `620:37551` |
| Dark | text-primary icon on surface-raised (lock) | #FFFFFF / #3A3A3C | 11.35:1 | 3:1 | PASS | Icon tile in `620:37527` |
| Dark | text-on-accent on accent (Try again) | #1C1C1E / #FF6A4D | 6.01:1 | 4.5:1 | PASS | `620:37553` |
| Dark | accent button vs bg (non-text) | #FF6A4D / #1C1C1E | 6.01:1 | 3:1 | PASS | `620:37553` |
| Dark | accent wordmark on bg | #FF6A4D / #1C1C1E | 6.01:1 | 3:1 | PASS | F1 / F4 |
| Light | text-primary on bg | #000000 / #FAF9F6 | 19.95:1 | 4.5:1 | PASS | `620:37611` |
| Light | text-secondary on bg | #636366 / #FAF9F6 | 5.69:1 | 4.5:1 | PASS | `620:37611` |
| Light | text-secondary on surface-raised (code chip) | #636366 / #E5E5EA | 4.77:1 | 4.5:1 | PASS | `620:37611` |
| Light | text-primary icon on surface-raised | #000000 / #E5E5EA | 16.73:1 | 3:1 | PASS | `620:37611` |
| Light | text-on-accent on accent (Try again) | #FFFFFF / #CF3D20 | 4.84:1 | 4.5:1 | PASS | `620:37611` |
| Light | accent button vs bg (non-text) | #CF3D20 / #FAF9F6 | 4.59:1 | 3:1 | PASS | `620:37611` |
| Light | accent wordmark on bg | #CF3D20 / #FAF9F6 | 4.59:1 | 3:1 | PASS | F1 / F4 Light |
F3's disabled button (40% opacity) is exempt (WCAG 1.4.3 inactive components); its state is also announced.
The icon tile's surface-raised vs bg boundary (1.50:1 Dark) is decorative; the icon itself carries the meaning.

## 3. Hit targets
| Element | Visual | Hit area | Result |
|---|---|---|---|
| Try again | 370×56 | 370×56 | PASS (≥ 44pt / 48dp) |
| Code chip | 32pt tall | not interactive | n/a |

## 4. Amounts
None of the foundation surfaces shows an amount (the shield and splash exist to hide them). PASS.

## 5. Dynamic Type / font scale and Reduce Motion
| Screen | Font scale | Reduce Motion |
|---|---|---|
| F1 / F4 | logo is an image, does not scale | no motion |
| F2 / F3 | Title and Message wrap; Message block scrolls above the pinned Actions at the largest sizes; button min height 56, label wraps to 2 lines at most | no motion; F3 state change is a label swap |
| Placeholders | Large Title scales | none |

## 6. Privacy mode
No amounts shown; the shield (F4) hides everything in the app switcher regardless of Privacy Mode. PASS.

## 7. Judgment
- Copy tells the user what happened (data can't be opened), that nothing is lost ("still on this device"), what to do (Try again, restart) and what not to do (don't delete the app).
- VoiceOver order F2: Title → Message → Code → Try again → Help.
- Store error codes are support identifiers, not explanations; they sit in a secondary chip so they don't lead the message.

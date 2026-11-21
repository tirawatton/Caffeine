---
name: ios-security
description: How Caffeine iOS implements the security standard - Data Protection on the SwiftData store and files, CryptoKit AES-256-GCM field encryption for Restricted data, Keychain and Secure Enclave key handling, App Lock with keys released only after authentication, token storage, ATS and certificate pinning, privacy cover, pasteboard and keyboard rules, private logging, exports, and the MASVS checks QA will run. Loaded by ios-developer.
---

# iOS — Security and Data Protection

Implements `security-standard` (classes, crypto policy, layers). If anything here conflicts with it, the standard wins.

## 1. Store and files at rest
- Entitlement `com.apple.developer.default-data-protection` = `NSFileProtectionComplete`, and set `FileProtectionType.complete` explicitly on the SwiftData store directory and every file the app writes (slips, receipts, category photos, exports).
- Consequence: data is unreadable while the device is locked. Background backup checks `UIApplication.shared.isProtectedDataAvailable` and defers if false. Widgets read only a small summary written by the app (see §7 open decisions).
- Exclude caches of Restricted data from iCloud device backup (`URLResourceValues.isExcludedFromBackup = true`).

## 2. Field-level encryption (Restricted fields)
```swift
// FieldCipher.swift (Sources/Shared/Security) — the only place that touches CryptoKit for data
struct FieldCipher: Sendable {
    let key: SymmetricKey                      // 256-bit DEK from KeyStore
    func seal(_ plain: Data, aad: Data) throws -> Data {
        let box = try AES.GCM.seal(plain, using: key, nonce: AES.GCM.Nonce(), authenticating: aad)
        guard let combined = box.combined else { throw SecurityError.sealFailed }  // nonce || ciphertext || tag
        return combined
    }
    func open(_ combined: Data, aad: Data) throws -> Data {
        try AES.GCM.open(AES.GCM.SealedBox(combined: combined), using: key, authenticating: aad)
    }
}
```
- AAD = `"\(entity).\(field).\(recordID).v\(schemaVersion)"` so ciphertext can't be swapped between rows or fields.
- `@Model` stores Restricted fields as `Data` (`noteCiphertext`); the **repository** encrypts on write and decrypts into the domain struct. Stores and Views never see ciphertext or keys.
- Encrypted fields can't be queried by predicate: search on them by decrypting a bounded, already-filtered result set in the repository actor.

## 3. Keys
- DEK: `SymmetricKey(size: .bits256)`, created on first launch, stored in the Keychain as `kSecClassGenericPassword` with `kSecAttrAccessibleWhenUnlockedThisDeviceOnly`, never synced (`kSecAttrSynchronizable = false`).
- Wrap the DEK with a Secure Enclave key where available (`SecureEnclave.P256.KeyAgreement.PrivateKey` → ECDH → HKDF-SHA-256 → AES-GCM wrap); fall back to Keychain-only on devices without SE (simulator).
- App Lock on: the DEK's Keychain item uses `SecAccessControl` with `.userPresence` (biometry or passcode), so the key is released only after `LAContext` authentication — the lock is cryptographic, not just a screen.
- Crypto-shredding for "Delete my data": delete the Keychain items, then the store and files.

## 4. Authentication and tokens
- Sign in with Apple (`ASAuthorizationAppleIDProvider`); send the identity token to the backend once; store backend access/refresh tokens in the Keychain only (`WhenUnlockedThisDeviceOnly`). Never UserDefaults, never files, never logs.
- App Lock (12H): `LAContext.evaluatePolicy(.deviceOwnerAuthentication…)`; detect biometry changes via `evaluatedPolicyDomainState` and require passcode re-auth when it changes.

## 5. Network
- ATS on: no `NSAllowsArbitraryLoads`, no exceptions. TLS 1.3 minimum where the server supports it (`tlsMinimumSupportedProtocolVersion = .TLSv13` on the session configuration once the backend confirms).
- Pinning: `NSPinnedDomains` in Info.plist with SPKI SHA-256 pins for the API domain — the current key **plus a backup key**. A pin failure is a network error, never a prompt to continue.
- All requests go through the API client (`ios-networking`).

## 6. Platform leaks (MASVS-PLATFORM, ISO 8.12)
- Privacy cover on `.inactive` when Privacy Mode or App Lock is on (`ios-app-lifecycle`).
- Pasteboard: copying account numbers uses `UIPasteboard.general.setItems(_, options: [.localOnly: true, .expirationDate: now + 60])`.
- Sensitive text fields: `.textContentType(.oneTimeCode)`-style fields only where real; amounts/notes `.autocorrectionDisabled()`; never put Restricted text in notification bodies, Spotlight, Siri intents or widgets.
- Logging: `Logger` with `privacy: .private` (the default for dynamic values) — never `.public` for user data; no `print` in release.
- Exports (CSV/PDF): written to a temporary `complete`-protected file, shared via the share sheet, deleted after; the UI warns that an export leaves the app unencrypted.
- No secrets in Info.plist, xcconfig in the repo, or code. Third-party SDKs only with backend-lead review (none collect data before consent).

## 7. Open decisions for Ton (record answers in `docs/security/exceptions.md`)
- Widgets on the lock screen: show amounts (needs a summary readable after first unlock) or hide them until unlock.
- Jailbreak detection: off, signal-only (log + warn), or block.

## 8. What QA checks (MASTG)
Store file has `complete` protection; Restricted columns are ciphertext in the SQLite file; no tokens/keys in UserDefaults, plist or logs; ATS has no exceptions; pinning rejects a proxy certificate; recents snapshot shows the cover; export temp files are gone after sharing.

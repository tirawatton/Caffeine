---
name: android-security
description: How Caffeine Android implements the security standard - Room on SQLCipher with a Keystore-wrapped key, Tink AES-256-GCM field encryption for Restricted data, Android Keystore and StrongBox, App Lock with BiometricPrompt-bound keys, token storage, Network Security Config with cleartext off and pinning, backup rules, FLAG_SECURE, clipboard and exported-component rules, release logging, and the MASVS checks QA will run. Loaded by android-developer.
---

# Android — Security and Data Protection

Implements `security-standard`. If anything here conflicts with it, the standard wins.

## 1. Database and files at rest
- Room on **SQLCipher** (`net.zetetic:sqlcipher-android`, `SupportOpenHelperFactory(passphrase)`), AES-256. The 32-byte passphrase is generated once with `SecureRandom`, encrypted with a Keystore AES-GCM key and stored in app-private storage; zero the byte array after opening.
- Files (slips, receipts, photos, exports) are written as Tink-encrypted blobs in `filesDir` (never external storage).
- Do **not** use `androidx.security:security-crypto` (`EncryptedSharedPreferences` / `EncryptedFile`): it is deprecated. Use Tink + Keystore directly.

## 2. Field-level encryption (Restricted fields)
```kotlin
// shared/security/FieldCipher.kt — the only place that touches crypto for data
class FieldCipher @Inject constructor(private val aead: Aead) {        // Tink AES256_GCM keyset
    fun seal(plain: ByteArray, aad: ByteArray): ByteArray = aead.encrypt(plain, aad)
    fun open(cipher: ByteArray, aad: ByteArray): ByteArray = aead.decrypt(cipher, aad)
}
```
- Tink keyset (`AesGcmKeyManager.aes256GcmTemplate()`) stored with `AndroidKeysetManager`, its master key in the Android Keystore (`android-keystore://caffeine_master`).
- AAD = `"$entity.$field.$recordId.v$schemaVersion"`, same format as iOS.
- Entities store Restricted fields as `ByteArray` (`noteCiphertext`); the **repository** encrypts/decrypts; ViewModels and composables never see ciphertext or keys. Search on encrypted fields decrypts a bounded, pre-filtered result set on the IO dispatcher.

## 3. Keys
- Keystore keys: `KeyGenParameterSpec` AES-256, `BLOCK_MODE_GCM`, `ENCRYPTION_PADDING_NONE`, `setIsStrongBoxBacked(true)` with fallback when StrongBox is unavailable, `setUnlockedDeviceRequired(true)` (API 28+).
- App Lock on: the key that unwraps the SQLCipher passphrase requires user authentication (`setUserAuthenticationParameters(0, AUTH_BIOMETRIC_STRONG or AUTH_DEVICE_CREDENTIAL)` on API 30+, `setUserAuthenticationRequired(true)` on 28–29) and is used through `BiometricPrompt` with a `CryptoObject` — the lock is cryptographic.
- `setInvalidatedByBiometricEnrollment(true)`; on `KeyPermanentlyInvalidatedException` re-authenticate with device credential and re-wrap.
- Crypto-shredding for "Delete my data": delete Keystore aliases and keysets, then the database and files.

## 4. Authentication and tokens
- Sign in with Google via Credential Manager (and Sign in with Apple via web flow if Ton wants parity); tokens stored only Tink-encrypted (DataStore with an encrypted serializer). Never plain SharedPreferences, never logs.
- App Lock (12H): `BiometricPrompt` with `BIOMETRIC_STRONG or DEVICE_CREDENTIAL`.

## 5. Network
- `res/xml/network_security_config.xml`: `cleartextTrafficPermitted="false"` globally; `<pin-set expiration="…">` for the API domain with the current SPKI SHA-256 pin **plus a backup pin**; no user-added CAs in release (`<trust-anchors><certificates src="system"/></trust-anchors>`).
- OkHttp `ConnectionSpec.RESTRICTED_TLS` / TLS 1.3 once the backend confirms. All requests through the API client (`android-networking`).

## 6. Platform leaks (MASVS-PLATFORM, ISO 8.12)
- `FLAG_SECURE` when Privacy Mode or App Lock is on (`android-app-lifecycle`).
- Backup: `android:allowBackup="false"`, plus `dataExtractionRules` (API 31+) and `fullBackupContent` (≤ 30) that exclude the database, keysets and files.
- Clipboard: account numbers copied with `ClipDescription.EXTRA_IS_SENSITIVE` (API 33+) and cleared after 60 s.
- Components: only the launcher activity exported; deep links are verified App Links; every `PendingIntent` uses `FLAG_IMMUTABLE`; no WebView with JavaScript for app data.
- Never put Restricted text in notifications, App Search, Assistant or Glance widgets.
- Logging: Timber with no tree planted in release, plus R8 `-assumenosideeffects` for `android.util.Log`; no user data in logs at any level.
- Exports: temp file in `cacheDir`, shared through `FileProvider`, deleted after; the UI warns it leaves the app unencrypted.
- No secrets in `BuildConfig`, `strings.xml`, `local.properties` committed, or code. New SDKs only with backend-lead review.

## 7. Open decisions for Ton (record answers in `docs/security/exceptions.md`)
- Lock-screen / home widgets with amounts: show, or hide until unlock.
- Root / integrity: off, Play Integrity signal-only, or block.

## 8. What QA checks (MASTG)
The DB file is not readable as plain SQLite; Restricted columns are ciphertext; no tokens/keys in SharedPreferences, logs or `adb backup`; cleartext is refused; pinning rejects a proxy certificate; recents shows a blank window with FLAG_SECURE; no exported components except launcher; export temp files are gone.

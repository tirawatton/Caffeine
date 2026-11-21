# qa-automation

Cross-platform Appium + Pytest suite owned by `qa-engineer`. One test body runs against both apps.

```bash
pip install -r requirements.txt
appium   # Appium 2 with xcuitest and uiautomator2 drivers
pytest tests --ios-app-path <Caffeine.app> --android-app-path <app-debug.apk>
```

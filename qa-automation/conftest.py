"""Shared Appium fixtures: every test runs once per platform (see .claude/skills/appium-parity)."""
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions


def pytest_addoption(parser):
    parser.addoption("--ios-app-path", default=None)
    parser.addoption("--android-app-path", default=None)
    parser.addoption("--appium-url", default="http://127.0.0.1:4723")


def _options(platform: str, app_path: str):
    if platform == "ios":
        opts = XCUITestOptions()
        opts.platform_version = "18.0"
    else:
        opts = UiAutomator2Options()
    opts.app = app_path
    opts.new_command_timeout = 120
    return opts


@pytest.fixture(params=["ios", "android"])
def driver(request):
    app_path = request.config.getoption(f"--{request.param}-app-path")
    if not app_path:
        pytest.skip(f"no {request.param} app path given")
    drv = webdriver.Remote(request.config.getoption("--appium-url"), options=_options(request.param, app_path))
    drv.platform = request.param
    yield drv
    drv.quit()

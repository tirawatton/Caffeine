from pages.base_page import BasePage


def test_app_launches_with_root_title(driver):
    assert BasePage(driver).find("root.title").is_displayed()

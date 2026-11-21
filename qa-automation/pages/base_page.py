from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Explicit waits only; locators are accessibility ids `<screen>.<element>`."""

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, element_id: str):
        return self.wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, element_id)))

    def tap(self, element_id: str):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, element_id))).click()

    def text(self, element_id: str) -> str:
        return self.find(element_id).text

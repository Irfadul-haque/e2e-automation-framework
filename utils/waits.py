from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import Settings

class WaitUtils:
    @staticmethod
    def wait_for_visible(driver: WebDriver, locator: tuple, timeout: int = Settings.DEFAULT_TIMEOUT) -> WebElement:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

    @staticmethod
    def wait_for_clickable(driver: WebDriver, locator: tuple, timeout: int = Settings.DEFAULT_TIMEOUT) -> WebElement:
        return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

    @staticmethod
    def wait_for_all(driver: WebDriver, locator: tuple, timeout: int = Settings.DEFAULT_TIMEOUT) -> list[WebElement]:
        return WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @staticmethod
    def wait_for_invisibility(driver: WebDriver, locator: tuple, timeout: int = Settings.DEFAULT_TIMEOUT) -> bool:
        return WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located(locator))

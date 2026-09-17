from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.waits import WaitUtils
from utils.logger import get_logger
from config.settings import Settings
import time

logger = get_logger("BasePage")

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate_to(self, path: str = ""):
        url = f"{Settings.UI_BASE_URL.rstrip('/')}/{path.lstrip('/')}"
        logger.info(f"Navigating to URL: {url}")
        self.driver.get(url)
        # Wait for the browser to finish rendering the DOM
        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        time.sleep(1) # Brief pause to let React async fetch complete

    def find(self, locator: tuple, timeout: int = Settings.DEFAULT_TIMEOUT) -> WebElement:
        return WaitUtils.wait_for_visible(self.driver, locator, timeout)

    def find_all(self, locator: tuple, timeout: int = Settings.DEFAULT_TIMEOUT) -> list[WebElement]:
        try:
            return WaitUtils.wait_for_all(self.driver, locator, timeout)
        except TimeoutException:
            return []

    def click(self, locator: tuple, timeout: int = Settings.DEFAULT_TIMEOUT):
        logger.info(f"Clicking element with locator: {locator}")
        element = WaitUtils.wait_for_clickable(self.driver, locator, timeout)
        element.click()

    def type_text(self, locator: tuple, text: str, clear_first: bool = True):
        logger.info(f"Typing into {locator}")
        element = self.find(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        return self.find(locator).text.strip()

    def is_visible(self, locator: tuple, timeout: int = 5) -> bool:
        try:
            return WaitUtils.wait_for_visible(self.driver, locator, timeout).is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    def scroll_into_view(self, locator: tuple):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        time.sleep(0.5) # Allow smooth scroll animation to finish

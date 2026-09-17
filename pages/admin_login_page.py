from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import Settings

class AdminLoginPage(BasePage):
    # Locators
    FOOTER_ADMIN_LINK = (By.CSS_SELECTOR, "a[href*='admin']")
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "doLogin")
    LOGOUT_BTN = (By.LINK_TEXT, "Logout")
    ROOMS_SECTION = (By.ID, "roomName")
    LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger, [class*='danger']")

    def load(self):
        # 1. Load the guest homepage to bootstrap React
        self.navigate_to("/")
        
        # 2. Scroll to the bottom and click the admin link to trigger the React router
        self.scroll_into_view(self.FOOTER_ADMIN_LINK)
        self.click(self.FOOTER_ADMIN_LINK)
        
        # 3. Wait for the admin login form to appear
        self.is_visible(self.USERNAME_INPUT, timeout=10)
        return self

    def login(self, username: str = Settings.ADMIN_USERNAME, password: str = Settings.ADMIN_PASSWORD):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BTN)

    def is_logged_in(self) -> bool:
        return self.is_visible(self.ROOMS_SECTION, timeout=10) or self.is_visible(self.LOGOUT_BTN, timeout=10)

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BookingForm(BasePage):
    FIRSTNAME_INPUT = (By.NAME, "firstname")
    LASTNAME_INPUT = (By.NAME, "lastname")
    EMAIL_INPUT = (By.NAME, "email")
    PHONE_INPUT = (By.NAME, "phone")
    BOOK_BTN = (By.XPATH, "//button[contains(text(), 'Book')]")
    CANCEL_BTN = (By.XPATH, "//button[contains(text(), 'Cancel')]")
    SUCCESS_CONFIRMATION = (By.XPATH, "//h3[contains(text(), 'Booking Successful!')]")
    ERROR_ALERTS = (By.CSS_SELECTOR, ".alert-danger p")

    def fill_guest_details(self, firstname: str, lastname: str, email: str, phone: str):
        self.type_text(self.FIRSTNAME_INPUT, firstname)
        self.type_text(self.LASTNAME_INPUT, lastname)
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PHONE_INPUT, phone)

    def submit_booking(self):
        self.click(self.BOOK_BTN)

    def cancel_booking(self):
        self.click(self.CANCEL_BTN)

    def is_booking_successful(self) -> bool:
        return self.is_visible(self.SUCCESS_CONFIRMATION, timeout=8)

    def get_validation_errors(self) -> list[str]:
        errors = self.find_all(self.ERROR_ALERTS, timeout=5)
        return [e.text.strip() for e in errors]

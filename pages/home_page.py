from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    ROOM_CARD = (By.CSS_SELECTOR, ".hotel-room-info, .room-card, div.row.hotel-room")
    ROOM_HEADER = (By.CSS_SELECTOR, ".hotel-room-info h3, h3")
    BOOK_THIS_ROOM_BTN = (By.CSS_SELECTOR, "button.openBooking")
    
    # Fallback locators that check common React attributes and IDs
    CONTACT_NAME_INPUT = (By.CSS_SELECTOR, "input#name, input[data-testid='ContactName']")
    CONTACT_EMAIL_INPUT = (By.CSS_SELECTOR, "input#email, input[data-testid='ContactEmail']")
    CONTACT_PHONE_INPUT = (By.CSS_SELECTOR, "input#phone, input[data-testid='ContactPhone']")
    CONTACT_SUBJECT_INPUT = (By.CSS_SELECTOR, "input#subject, input[data-testid='ContactSubject']")
    CONTACT_DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea#description, textarea[data-testid='ContactDescription']")
    
    # Resilient XPath: Find any button that contains the text 'Submit'
    CONTACT_SUBMIT_BTN = (By.XPATH, "//button[contains(text(), 'Submit')]")
    CONTACT_CONFIRMATION = (By.XPATH, "//*[contains(text(), 'Thanks for getting in touch') or contains(text(), 'success')]")
    CONTACT_ERROR_ALERTS = (By.CSS_SELECTOR, ".alert-danger p")

    def load(self):
        self.navigate_to("/")
        return self

    def get_room_names(self) -> list[str]:
        headers = self.find_all(self.ROOM_HEADER)
        return [h.text.strip() for h in headers if h.text.strip()]

    def is_room_displayed(self, room_name: str) -> bool:
        locator = (By.XPATH, f"//*[contains(text(), '{room_name}')]")
        return self.is_visible(locator, timeout=20) # Increased timeout for backend propagation

    def click_book_room(self, index: int = 0):
        buttons = self.find_all(self.BOOK_THIS_ROOM_BTN)
        if buttons and len(buttons) > index:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buttons[index])
            buttons[index].click()

    def submit_contact_form(self, name: str, email: str, phone: str, subject: str, description: str):
        self.scroll_into_view(self.CONTACT_NAME_INPUT)
        self.type_text(self.CONTACT_NAME_INPUT, name)
        self.type_text(self.CONTACT_EMAIL_INPUT, email)
        self.type_text(self.CONTACT_PHONE_INPUT, phone)
        self.type_text(self.CONTACT_SUBJECT_INPUT, subject)
        self.type_text(self.CONTACT_DESCRIPTION_INPUT, description)
        
        self.scroll_into_view(self.CONTACT_SUBMIT_BTN)
        self.click(self.CONTACT_SUBMIT_BTN)

    def get_contact_error_messages(self) -> list[str]:
        elements = self.find_all(self.CONTACT_ERROR_ALERTS, timeout=5)
        return [el.text.strip() for el in elements]

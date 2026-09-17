import pytest
from pages.home_page import HomePage
from data.factories import make_contact_message_payload

def test_successful_contact_form_submission(driver):
    home_page = HomePage(driver)
    home_page.load()
    
    # Generate random contact data
    data = make_contact_message_payload()
    
    # Act: Submit the form via Page Object
    home_page.submit_contact_form(
        name=data["name"],
        email=data["email"],
        phone=data["phone"],
        subject=data["subject"],
        description=data["description"]
    )
    
    # Assert: Verify the success confirmation overlay appears
    assert home_page.is_visible(home_page.CONTACT_CONFIRMATION, timeout=10), "Success confirmation did not appear"

import pytest
from data.factories import make_room_payload
from pages.admin_login_page import AdminLoginPage
from config.settings import Settings

def test_admin_sees_newly_created_room(driver, rooms_client, state_manager):
    # 1. API SETUP: Inject data directly into the database
    room_data = make_room_payload()
    create_resp = rooms_client.create_room(room_data)
    assert create_resp.status_code in [200, 201]
    
    data = create_resp.json()
    room_id = data.get("roomid") or data.get("roomId")
    
    if not room_id:
        rooms_list = rooms_client.get_rooms().json().get("rooms", [])
        for r in rooms_list:
            if r.get("roomName") == room_data["roomName"]:
                room_id = r.get("roomid")
                break
                
    assert room_id, f"Could not extract roomid for teardown."
    state_manager["rooms"].append(room_id)
    
    # 2. UI VERIFICATION: Log into Admin portal (bypasses Guest CDN cache)
    admin_page = AdminLoginPage(driver)
    admin_page.load()
    admin_page.login(Settings.ADMIN_USERNAME, Settings.ADMIN_PASSWORD)
    
    assert admin_page.is_logged_in(), "Admin failed to log in."
    
    # 3. ASSERT: Verify the specific room name appears in the live admin room list
    locator = ("xpath", f"//*[contains(text(), '{room_data['roomName']}')]")
    is_displayed = admin_page.is_visible(locator, timeout=10)
    
    assert is_displayed is True, f"Room '{room_data['roomName']}' was not found in the Admin Portal"

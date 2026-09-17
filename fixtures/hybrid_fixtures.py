import pytest
from api_clients.auth_client import AuthClient
from api_clients.rooms_client import RoomsClient
from api_clients.bookings_client import BookingsClient

@pytest.fixture(scope="session")
def api_token():
    client = AuthClient()
    token = client.login_and_get_token()
    assert token, "CRITICAL: Failed to authenticate and get API token for test session."
    return token

@pytest.fixture(scope="function")
def rooms_client(api_token):
    return RoomsClient(token=api_token)

@pytest.fixture(scope="function")
def bookings_client(api_token):
    return BookingsClient(token=api_token)

@pytest.fixture(scope="function")
def state_manager(rooms_client, bookings_client):
    '''
    Tracks entity IDs created during a test and aggressively cleans them up 
    after the test finishes (even if the test fails) to prevent data collisions.
    '''
    state = {
        "rooms": [],
        "bookings": []
    }
    
    yield state
    
    # Teardown: Reverse order (delete bookings before rooms to avoid foreign key constraints)
    for booking_id in state["bookings"]:
        try:
            bookings_client.delete_booking(booking_id)
        except Exception:
            pass
            
    for room_id in state["rooms"]:
        try:
            rooms_client.delete_room(room_id)
        except Exception:
            pass

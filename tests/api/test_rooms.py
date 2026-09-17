import pytest
from data.factories import make_room_payload

def test_create_and_verify_room(rooms_client, state_manager):
    payload = make_room_payload()
    
    create_response = rooms_client.create_room(payload)
    assert create_response.status_code in [200, 201], f"Unexpected status: {create_response.status_code}"
    
    # Safely extract ID using a fallback strategy
    data = create_response.json()
    room_id = data.get("roomid") or data.get("roomId")
    
    if not room_id:
        rooms_list = rooms_client.get_rooms().json().get("rooms", [])
        for r in rooms_list:
            if r.get("roomName") == payload["roomName"]:
                room_id = r.get("roomid")
                break
                
    assert room_id is not None, f"Failed to extract roomid. POST response was: {data}"
    state_manager["rooms"].append(room_id)
    
    get_response = rooms_client.get_room_by_id(room_id)
    assert get_response.status_code == 200
    
    body = get_response.json()
    assert body["roomName"] == payload["roomName"]

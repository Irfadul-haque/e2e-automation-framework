from api_clients.base_client import BaseClient

class RoomsClient(BaseClient):
    def __init__(self, token: str = None):
        super().__init__()
        if token:
            self.session.cookies.set("token", token)
            self.session.headers.update({"Cookie": f"token={token}"})

    def get_rooms(self):
        return self.get("/room/")

    def get_room_by_id(self, room_id: int):
        return self.get(f"/room/{room_id}")

    def create_room(self, payload: dict):
        return self.post("/room/", json=payload)

    def update_room(self, room_id: int, payload: dict):
        return self.put(f"/room/{room_id}", json=payload)

    def delete_room(self, room_id: int):
        return self.delete(f"/room/{room_id}")

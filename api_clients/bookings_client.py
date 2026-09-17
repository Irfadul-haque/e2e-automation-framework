from api_clients.base_client import BaseClient

class BookingsClient(BaseClient):
    def __init__(self, token: str = None):
        super().__init__()
        if token:
            self.session.cookies.set("token", token)
            self.session.headers.update({"Cookie": f"token={token}"})

    def get_bookings(self, room_id: int = None):
        params = {"roomid": room_id} if room_id is not None else None
        return self.get("/booking/", params=params)

    def get_booking_by_id(self, booking_id: int):
        return self.get(f"/booking/{booking_id}")

    def create_booking(self, payload: dict):
        return self.post("/booking/", json=payload)

    def delete_booking(self, booking_id: int):
        return self.delete(f"/booking/{booking_id}")

    def get_booking_summary(self, room_id: int):
        return self.get(f"/booking/summary?roomid={room_id}")

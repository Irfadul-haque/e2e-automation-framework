import random
import uuid
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

def make_room_payload(
    room_name: str = None,
    room_type: str = None,
    accessible: bool = True,
    price: int = None
) -> dict:
    types = ["Single", "Double", "Twin", "Family", "Suite"]
    unique_suffix = str(uuid.uuid4())[:4]
    return {
        "roomName": room_name or f"Room-{random.randint(100, 999)}-{unique_suffix}",
        "type": room_type or random.choice(types),
        "accessible": accessible,
        "image": "https://www.mwtestconsultancy.co.uk/img/room1.jpg",
        "description": f"Spacious and comfortable room - {fake.sentence(nb_words=6)}",
        "features": ["WiFi", "TV", "Safe"],
        "roomPrice": price or random.randint(120, 450)
    }

def make_booking_payload(room_id: int, days_ahead: int = 14, duration_days: int = 3) -> dict:
    checkin = datetime.now() + timedelta(days=days_ahead)
    checkout = checkin + timedelta(days=duration_days)
    return {
        "bookingdates": {
            "checkin": checkin.strftime("%Y-%m-%d"),
            "checkout": checkout.strftime("%Y-%m-%d")
        },
        "depositpaid": True,
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "roomid": room_id,
        "email": fake.email(),
        "phone": f"+447{random.randint(100000000, 999999999)}"
    }

def make_contact_message_payload() -> dict:
    return {
        "name": fake.name(),
        "email": fake.email(),
        "phone": f"+447{random.randint(100000000, 999999999)}",
        "subject": f"Inquiry about reservation {random.randint(100, 999)}",
        "description": fake.paragraph(nb_sentences=3)
    }

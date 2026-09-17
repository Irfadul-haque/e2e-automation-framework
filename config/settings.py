import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    UI_BASE_URL: str = os.getenv("UI_BASE_URL", "https://automationintesting.online")
    BASE_URL: str = os.getenv("BASE_URL", "https://automationintesting.online/api")
    ADMIN_USERNAME: str = os.getenv("ADMIN_USERNAME", "admin")
    ADMIN_PASSWORD: str = os.getenv("ADMIN_PASSWORD", "password")
    HEADLESS: bool = os.getenv("HEADLESS", "true").lower() in ("true", "1", "yes")
    DEFAULT_TIMEOUT: int = int(os.getenv("DEFAULT_TIMEOUT", "10"))
    REQUEST_TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", "15"))

from api_clients.base_client import BaseClient
from config.settings import Settings
from utils.logger import get_logger

logger = get_logger("AuthClient")

class AuthClient(BaseClient):
    def login(self, username: str = None, password: str = None):
        payload = {
            "username": username or Settings.ADMIN_USERNAME,
            "password": password or Settings.ADMIN_PASSWORD
        }
        return self.post("/auth/login", json=payload)

    def login_and_get_token(self, username: str = None, password: str = None) -> str:
        response = self.login(username, password)
        if response.status_code == 200:
            try:
                data = response.json()
                token = data.get("token") or response.cookies.get("token")
                if token:
                    logger.info(f"Successfully authenticated. Acquired token: {token[:6]}...")
                    return token
            except Exception as e:
                logger.error(f"Error parsing auth response: {e}")
        logger.warning(f"Failed to extract auth token. Status: {response.status_code}")
        return ""

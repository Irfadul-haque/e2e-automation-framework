import requests
from config.settings import Settings
from utils.logger import get_logger

logger = get_logger("BaseClient")

class BaseClient:
    def __init__(self, base_url: str = None):
        self.base_url = (base_url or Settings.BASE_URL).rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })

    def request(self, method: str, endpoint: str, **kwargs):
        clean_endpoint = endpoint.lstrip('/')
        url = f"{self.base_url}/{clean_endpoint}"
        timeout = kwargs.pop("timeout", Settings.REQUEST_TIMEOUT)
        logger.info(f"API Request: {method.upper()} {url}")
        
        response = self.session.request(method, url, timeout=timeout, **kwargs)
        logger.info(f"API Response: {response.status_code} ({response.elapsed.total_seconds():.2f}s)")
        return response

    def get(self, endpoint: str, **kwargs):
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs):
        return self.request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self.request("DELETE", endpoint, **kwargs)

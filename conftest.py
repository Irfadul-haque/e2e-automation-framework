import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from config.settings import Settings

# This hook lets us check if a test failed so we can take a screenshot
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(scope="function")
def driver(request):
    options = Options()
    if Settings.HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    # We rely on our explicit WaitUtils, so implicit wait stays at 0
    driver.implicitly_wait(0) 

    yield driver

    # Auto-capture screenshot on failure
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        try:
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"failure_screenshot_{request.node.name}",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")

    driver.quit()

# Import custom hybrid API fixtures
pytest_plugins = [
    "fixtures.hybrid_fixtures"
]

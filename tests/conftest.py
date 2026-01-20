import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urls


@pytest.fixture(scope = "function")
def get_driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument(
        "--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    driver.get(urls.login_page_url)
    yield
    driver.quit()
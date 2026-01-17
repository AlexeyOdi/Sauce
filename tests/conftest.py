import pytest
from selenium import webdriver

import urls


@pytest.fixture(scope = "function")
def get_driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.get(urls.login_page_url)
    yield
    driver.quit()
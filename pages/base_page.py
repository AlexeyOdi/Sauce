from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def find_element(self, locator):
        self.driver.find_element(*locator)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def wait(self, locator):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((locator)))

    def wait_for_page(self, url):
        WebDriverWait(self.driver, 5).until(EC.url_matches((url)))


    def send_keys(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    def get_current_url(self):
        return self.driver.current_url

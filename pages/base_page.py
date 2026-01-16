from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


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

    def scroll_to(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)

    @allure.step('Прокручиваем страницу до самого низа')
    def scroll_to_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def send_keys(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    def switch_window(self, handle):
        self.driver.switch_to.window(handle)

    def get_current_url(self):
        return self.driver.current_url

    def get_current_window_handle(self):
        return  self.driver.current_window_handle

    def get_window_handles(self):
        return  self.driver.window_handles
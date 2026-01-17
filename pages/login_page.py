from locators.login_page_locators import error_header, login_input, password_input, login_button
from pages.base_page import BasePage
from test_data import login_error_text, locked_out_error_text, empty_username_input_error_text
from urls import inventory_page_url
import allure


class LoginPage(BasePage):
    @allure.step('Вводим логин')
    def set_login(self,login):
        self.send_keys(login_input,login)

    @allure.step('Вводим пароль')
    def set_password(self, password):
        self.send_keys(password_input,password)

    @allure.step('нажимаем на кнопку входа')
    def click_login_button(self):
        self.click(login_button)

    @allure.step('Сравниваем адрес текущей страницы с ожидаемой')
    def check_assert_inventory_page(self):
        assert self.get_current_url() == inventory_page_url

    @allure.step('Сравниваем текст ошибки с ожидаемым')
    def check_assert_login_error(self):
        actual_text = self.get_text(error_header)
        assert actual_text == login_error_text

    @allure.step('Сравниваем текст ошибки с ожидаемым')
    def check_assert_locked_out_error(self):
        actual_text = self.get_text(error_header)
        assert actual_text == locked_out_error_text

    @allure.step('Сравниваем текст ошибки с ожидаемым')
    def check_assert_empty_login_input_error(self):
        actual_text = self.get_text(error_header)
        assert actual_text == empty_username_input_error_text

    @allure.step('Ждем загрузки блока с ошибкой')
    def wait_for_error_cont(self):
        self.wait(error_header)

    @allure.step('Ждем загрузки ожидаемой страницы')
    def wait_for_inventory_page(self):
        self.wait_for_page(inventory_page_url)
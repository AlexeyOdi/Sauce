import pytest
import allure


from pages.login_page import LoginPage
from test_data import valid_user, valid_password, invalid_password, locked_out_user, glitch_user


@pytest.mark.usefixtures("get_driver")
class TestLoginPage:

    @allure.title('Проверка входа под корректным логином и паролем')
    def test_valid_user_and_pass(self):
        test_lp = LoginPage(self.driver)
        test_lp.set_login(valid_user)
        test_lp.set_password(valid_password)
        test_lp.click_login_button()
        test_lp.check_assert_inventory_page()

    @allure.title('Проверка входа с некорректным паролем')
    def test_invalid_pass(self):
        test_lp = LoginPage(self.driver)
        test_lp.set_login(valid_user)
        test_lp.set_password(invalid_password)
        test_lp.click_login_button()
        test_lp.wait_for_error_cont()
        test_lp.check_assert_login_error()

    @allure.title('Проверка входа заблокированного пользователя')
    def test_locked_out_user(self):
        test_lp = LoginPage(self.driver)
        test_lp.set_login(locked_out_user)
        test_lp.set_password(valid_password)
        test_lp.click_login_button()
        test_lp.wait_for_error_cont()
        test_lp.check_assert_locked_out_error()

    @allure.title('Проверка входа с пустыми полями логина и пароля')
    def test_empty_input_login(self):
        test_lp = LoginPage(self.driver)
        test_lp.click_login_button()
        test_lp.wait_for_error_cont()
        test_lp.check_assert_empty_login_input_error()

    @allure.title('Проверка входа пользователя с медленным обновлением страницы')
    def test_glitch_user_login(self):
        test_lp = LoginPage(self.driver)
        test_lp.set_login(glitch_user)
        test_lp.set_password(valid_password)
        test_lp.click_login_button()
        test_lp.wait_for_inventory_page()
        test_lp.check_assert_inventory_page()


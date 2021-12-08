from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "login" in self.browser.current_url, "Login link is not presented"  # или self.browser.current_url.index("login")

    def should_be_login_form(self):
        # проверка, что есть форма логина на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registation form is not presented"

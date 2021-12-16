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
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email:str, password:str):
        register_email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        register_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD)
        register_confirm_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD_FIELD)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_email_field.send_keys(email)
        register_password_field.send_keys(password)
        register_confirm_password_field.send_keys(password)
        register_button.click()

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.login_url = self.browser.current_url
        assert "login" in self.login_url, "Login url is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.ENTER), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_IN), "Register form is not presented"

    def register_new_user(self, email, password):
        self.input_mail = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        self.input_mail.send_keys(email)
        self.input_password = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        self.input_password.send_keys(password)
        self.input_duplicate_password = self.browser.find_element(*LoginPageLocators.DUPLICATE_PASSWORD_FIELD)
        self.input_duplicate_password.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BTN).click()

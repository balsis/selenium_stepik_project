from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login/" in self.driver.current_url, "It's not a valid URL"

    def should_be_login_form(self):
        assert self.is_element_present(self.locators.LOGIN_FORM), "Login form is missing on the page"

    def should_be_register_form(self):
        assert self.is_element_present(self.locators.REGISTER_FORM), "Register form is missing on the page"
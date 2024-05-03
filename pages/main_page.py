from pages import locators
from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    locators = MainPageLocators()

    def should_be_login_link(self):
        assert self.is_element_present(self.locators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        login_link = self.driver.find_element(*self.locators.LOGIN_LINK)
        login_link.click()

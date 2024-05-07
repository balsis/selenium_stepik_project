import time

from pages.login_page import LoginPage
from pages.main_page import MainPage

URL = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(driver):
    page = MainPage(driver, URL)
    page.open()
    page.should_be_login_link()
    time.sleep(3)


def test_guest_can_go_to_login_page(driver):
    page = MainPage(driver, URL)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_url()
    login_page.should_be_login_form()
    login_page.should_be_register_form()
    time.sleep(3)

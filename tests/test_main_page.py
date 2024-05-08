import time

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_guest_should_see_login_link_from_main_page(driver):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, url)
    page.open()
    page.should_be_login_link()
    time.sleep(3)


def test_guest_can_go_to_login_page_from_main_page(driver):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, url)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_url()
    login_page.should_be_login_form()
    login_page.should_be_register_form()
    time.sleep(3)


def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, url)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.check_empty_basket()
    basket_page.check_no_items_in_basket()

import time

import pytest

from pages.product_page import ProductPage


# list(range(1, 7)) + [pytest.param(7, marks=pytest.mark.xfail)] + list(range(8, 10))
@pytest.mark.parametrize('num', [*range(1, 7), pytest.param(7, marks=pytest.mark.xfail), *range(8, 10)])
def test_guest_can_add_product_to_basket(driver, num):
    url = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    page = ProductPage(driver, url)
    page.open()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_adding_book_to_the_shopping_cart()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(driver, url)
    page.open()
    page.guest_can_add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(driver):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(driver, url)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(driver):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(driver, url)
    page.open()
    page.guest_can_add_product_to_basket()
    page.success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(driver):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(driver, url)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(driver):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(driver, url)
    page.open()
    page.go_to_login_page()

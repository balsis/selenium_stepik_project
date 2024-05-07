import time

import pytest

from pages.product_page import ProductPage

# list(range(1, 7)) + [pytest.param(7, marks=pytest.mark.xfail)] + list(range(8, 10))
@pytest.mark.parametrize('num', [*range(1, 7), pytest.param(7, marks=pytest.mark.xfail), *range(8, 10)])
def test_guest_can_add_product_to_basket(driver, num):
    URL = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    page = ProductPage(driver, URL)
    page.open()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_adding_book_to_the_shopping_cart()

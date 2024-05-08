from pages.base_page import BasePage
from pages.locators import ProductPageLocators, BasePageLocators
from itertools import chain


class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        button = self.is_element_clickable(ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def check_adding_book_to_the_shopping_cart(self):
        book_name = self.is_element_visible(ProductPageLocators.BOOK_NAME).text
        book_name_added_in_cart = self.is_element_visible(ProductPageLocators.BOOK_NAME_ADDED_TO_BASKET).text
        assert book_name == book_name_added_in_cart, "The book name doesn't match"

    def check_book_price_in_the_shopping_cart(self):
        book_price = self.is_element_visible(ProductPageLocators.BOOK_PRICE).text
        book_price_added_in_cart = self.is_element_visible(ProductPageLocators.COST_OF_THE_BASKET).text
        assert book_price == book_price_added_in_cart, "The book price doesn't match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(ProductPageLocators.BOOK_NAME_ADDED_TO_BASKET), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(ProductPageLocators.BOOK_NAME_ADDED_TO_BASKET), \
            "Success message is not disappeared"

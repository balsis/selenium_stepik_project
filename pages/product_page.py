from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    locators = ProductPageLocators()

    def guest_can_add_product_to_basket(self):
        button = self.is_element_clickable(self.locators.ADD_TO_BASKET_BUTTON)
        button.click()

    def check_adding_book_to_the_shopping_cart(self):
        book_name = self.is_element_visible(self.locators.BOOK_NAME).text
        book_name_added_in_cart = self.is_element_visible(self.locators.BOOK_NAME_ADDED_TO_CART).text
        assert book_name == book_name_added_in_cart, "The book name doesn't match"

    def check_book_price_in_the_shopping_cart(self):
        book_price = self.is_element_visible(self.locators.BOOK_PRICE).text
        book_price_added_in_cart = self.is_element_visible(self.locators.COST_OF_THE_SHOPPING_CART).text
        assert book_price == book_price_added_in_cart, "The book price doesn't match"

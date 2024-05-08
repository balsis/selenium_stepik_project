from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def check_empty_basket(self):
        assert self.is_element_present(BasketPageLocators.EMPTY_BASKET).text is not None, "The basket is not empty"

    def check_no_items_in_basket(self):
        no_items = self.is_not_element_present(BasketPageLocators.BASKET_ITEMS)
        assert no_items is True, "Items in basket"

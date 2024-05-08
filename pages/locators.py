class BasePageLocators:
    LOGIN_LINK = ("xpath", "//a[@id='login_link']")


class MainPageLocators:
    BASKET_LINK = ("xpath", "//a[@class='btn btn-default']")


class LoginPageLocators:
    LOGIN_FORM = ("xpath", "//form[@id='login_form']")
    REGISTER_FORM = ("xpath", "//form[@id='register_form']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = ("xpath", "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    BOOK_NAME = ("xpath", "//h1")
    BOOK_PRICE = ("xpath", "//p[@class='price_color']")
    BOOK_NAME_ADDED_TO_BASKET = ("xpath", "(//div[@class='alertinner ']/strong)[1]")
    COST_OF_THE_BASKET = ("xpath", "//div[@class='alertinner ']/p/strong")


class BasketPageLocators:
    EMPTY_BASKET = ("xpath", "//div[@id='content_inner']/p")
    BASKET_ITEMS = ("xpath", "//div[@class='basket-items']")

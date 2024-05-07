class BasePageLocators:
    LOGIN_LINK = ("xpath", "//a[@id='login_link']")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = ("xpath", "//form[@id='login_form']")
    REGISTER_FORM = ("xpath", "//form[@id='register_form']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = ("xpath", "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    BOOK_NAME = ("xpath", "//h1")
    BOOK_PRICE = ("xpath", "//p[@class='price_color']")
    BOOK_NAME_ADDED_TO_CART = ("xpath", "(//div[@class='alertinner ']/strong)[1]")
    COST_OF_THE_SHOPPING_CART = ("xpath", "//div[@class='alertinner ']/p/strong")

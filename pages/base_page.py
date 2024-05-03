from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver: webdriver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def is_element_present(self, selector):
        try:
            self.driver.find_element(*selector)
        except NoSuchElementException:
            return False
        return True

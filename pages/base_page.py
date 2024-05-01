from selenium import webdriver


class BasePage:
    def __init__(self, driver: webdriver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

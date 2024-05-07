import math

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: webdriver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def is_element_present(self, selector, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(selector))

    def is_element_clickable(self, selector, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(selector))

    def is_element_visible(self, selector, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(selector))

    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

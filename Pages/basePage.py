from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    url = 'https://demoqa.com'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def find_element(self, locator, time=10):
        locator = (By.CSS_SELECTOR, locator)
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_element_by_text(self, text, tag_name='span'):
        return self.driver.find_element_by_xpath(f'//{tag_name}[contains(., "{text}")]')

    def find_elements(self, locator, time=10):
        locator = (By.CSS_SELECTOR, locator)
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

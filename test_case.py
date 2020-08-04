from selenium import webdriver


class TestCase(object):

    driver = None

    def setup_method(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

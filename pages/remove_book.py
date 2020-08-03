import time


class RemoveBook:
    url = 'https://demoqa.com/profile'

    def __init__(self, driver):
        self.driver = driver

    def open_profile_page(self):
        self.driver.get(self.url)

    def validate_and_remove(self, book_name):
        time.sleep(0.5)
        assert book_name == self.driver.find_element_by_text(book_name, 'a').text
        self.driver.find_element_by_css_selector('#delete-record-undefined').click()
        time.sleep(0.5)
        self.driver.find_element_by_css_selector('#closeSmallModal-ok').click()
        time.sleep(0.5)

        alert = self.driver.switch_to.alert
        alert.accept()
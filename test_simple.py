"""
Apply Page Object pattern to this tests
"""
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_by_text(self, text, tag_name='span'):
        return self.driver.find_element_by_xpath("//" + tag_name + "[contains(., " + "'" + text + "'" + ")]")


class LoginPage(BasePage):
    def login_as_registered_user(self, user_data):
        self.driver.get('https://demoqa.com/login')

        user_name_field = self.driver.find_element_by_css_selector('#userName')
        user_name_field.send_keys(user_data['login'])

        user_password_field = self.driver.find_element_by_css_selector('#password')
        user_password_field.send_keys(user_data['password'])

        login_btn = self.driver.find_element_by_css_selector('#login')
        login_btn.click()

        time.sleep(1)
        assert self.driver.find_element_by_css_selector('#userName-value').text == user_data['login']


class BookPage(BasePage):
    def add_book_to_profile(self, book_name):
        self.driver.get('https://demoqa.com/books')

        search_field = self.driver.find_element_by_css_selector('#searchBox')
        search_field.send_keys(book_name)

        buy_book_link = self.find_element_by_text(book_name, 'span')
        buy_book_link.click()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        add_to_collection_btn = self.find_element_by_text('Add To Your Collection', 'button')
        add_to_collection_btn.click()

        time.sleep(0.5)

        alert = self.driver.switch_to.alert
        alert.accept()

    def validate_and_remove_book(self, book_name):
        time.sleep(0.5)
        assert book_name == self.find_element_by_text(book_name, 'a').text
        self.driver.find_element_by_css_selector('#delete-record-undefined').click()
        time.sleep(0.5)
        self.driver.find_element_by_css_selector('#closeSmallModal-ok').click()
        time.sleep(0.5)
        alert = self.driver.switch_to.alert
        alert.accept()

"""
Apply Page Object pattern to this tests
"""
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, path):
        self.driver.get(path)

    def find_element_by_text(self, text, tag_name='span'):
        return self.driver.find_element_by_xpath("//" + tag_name + "[contains(., " + "'" + text + "'" + ")]")


class LoginPage(BasePage):
    user_name_selector = '#userName'
    password_selector = '#password'
    login_selector = '#login'
    user_name_value_selector = '#userName-value'
    login_url = 'https://demoqa.com/login'

    def login_as_registered_user(self, user_data):
        self.open(self.login_url)

        user_name_field = self.driver.find_element_by_css_selector(self.user_name_selector)
        user_name_field.send_keys(user_data['login'])

        user_password_field = self.driver.find_element_by_css_selector(self.password_selector)
        user_password_field.send_keys(user_data['password'])

        login_btn = self.driver.find_element_by_css_selector(self.login_selector)
        login_btn.click()

        time.sleep(1)
        assert self.driver.find_element_by_css_selector(self.user_name_value_selector).text == user_data['login']


class BookPage(BasePage):
    book_url = 'https://demoqa.com/books'
    search_box_selector = '#searchBox'
    delete_record_selector = '#delete-record-undefined'
    close_selector = '#closeSmallModal-ok'

    def add_book_to_profile(self, book_name):
        self.open(self.book_url)

        search_field = self.driver.find_element_by_css_selector(self.search_box_selector)
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
        self.driver.find_element_by_css_selector(self.delete_record_selector).click()
        time.sleep(0.5)
        self.driver.find_element_by_css_selector(self.close_selector).click()
        time.sleep(0.5)
        alert = self.driver.switch_to.alert
        alert.accept()

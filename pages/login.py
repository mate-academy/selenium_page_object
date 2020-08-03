
import time


class LoginPage:

    user_name_field = '#userName'
    user_password_field = '#password'
    login_btn = '#login'
    url = 'https://demoqa.com/login'

    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.driver.get(self.url)

    def login_as_registered_user(self, user_data):

        user_name_field = self.driver.find_element_by_css_selector(self.user_name_field)
        user_name_field.send_keys(user_data['login'])

        user_password_field = self.driver.find_element_by_css_selector(self.user_password_field)
        user_password_field.send_keys(user_data['password'])

        login_btn = self.driver.find_element_by_css_selector(self.login_btn)
        login_btn.click()

        time.sleep(1)
        assert self.driver.find_element_by_css_selector('#userName-value').text == user_data['login']
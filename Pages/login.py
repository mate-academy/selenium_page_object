import time

from books_shop_test.Pages.basePage import BasePage


class LoginPage(BasePage):

    user_name_field = '#userName'
    user_password_field = '#password'
    login_btn = '#login'

    url = 'https://demoqa.com/login'

    def fill_required_fields(self, user_data):
        user_name_field = self.find_element(self.user_name_field)
        user_name_field.send_keys(user_data['login'])

        user_password_field = self.find_element(self.user_password_field)
        user_password_field.send_keys(user_data['password'])

    def login_as_registered_user(self, user_data):
        self.fill_required_fields(user_data)

        login_btn = self.find_element(self.login_btn)
        login_btn.click()

        time.sleep(1)
        assert self.find_element('#userName-value').text == user_data['login']

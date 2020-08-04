from selenium import webdriver
import pytest
import time

from books_shop_test.Pages.login import LoginPage
from books_shop_test.test_case import TestCase

USER = {
    'login': 'test12345678qweR',
    'password': '12345678qweR!'
}


class TestLoginFlow(TestCase):

    def test_login_as_registered_user(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.fill_required_fields(USER)

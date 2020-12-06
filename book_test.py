from page import LoginPage, BookPage
import pytest

from selenium import webdriver

USER = {
    'login': 'test12345678qweR',
    'password': '12345678qweR!'
}

BOOK_NAME_1 = 'Programming JavaScript Applications'
BOOK_NAME_2 = 'Learning JavaScript Design Patterns'

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(executable_path="c:/selenium/chromedriver.exe")
    yield driver
    driver.quit()

def test_add_book_to_profile_flow(driver):
    login_page = LoginPage(driver)
    book_page = BookPage(driver)
    login_page.login_as_registered_user(USER)
    book_page.add_book_to_profile(BOOK_NAME_1)

    book_page.open('https://demoqa.com/profile')

    book_page.validate_and_remove_book(BOOK_NAME_1)

def test_two_add_book_to_profile_flow(driver):
    login_page = LoginPage(driver)
    book_page = BookPage(driver)
    login_page.login_as_registered_user(USER)
    book_page.add_book_to_profile(BOOK_NAME_1)
    book_page.add_book_to_profile(BOOK_NAME_2)

    book_page.open('https://demoqa.com/profile')

    book_page.validate_and_remove_book(BOOK_NAME_1)
    book_page.validate_and_remove_book(BOOK_NAME_2)

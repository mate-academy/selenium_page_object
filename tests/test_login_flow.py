import pytest
from selenium import webdriver
from selenium_page_object.pages.login import LoginPage
from selenium_page_object.pages.add_books import AddBook
from selenium_page_object.pages.remove_book import RemoveBook

USER = {
    'login': 'test12345678qweR',
    'password': '12345678qweR!'
}
BOOK_NAME_1 = 'Programming JavaScript Applications'
BOOK_NAME_2 = 'Learning JavaScript Design Patterns'


def find_element_by_text(driver, text, tag_name='span'):
    return driver.find_element_by_xpath(f'//{tag_name}[contains(., "{text}")]')


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_add_book_to_profile_flow(driver):

    login_page = LoginPage()
    login_page.open_login_page()
    login_page.login_as_registered_user(USER)
    add_book = AddBook(driver)
    add_book.add_book_to_profile(BOOK_NAME_1)

    validate_and_remove_book = RemoveBook(driver)
    validate_and_remove_book.open_profile_page()
    validate_and_remove_book.validate_and_remove(BOOK_NAME_1)


def test_two_add_book_to_profile_flow(driver):

    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login_as_registered_user(USER)
    add_book = AddBook(driver)
    add_book.add_book_to_profile(BOOK_NAME_1)
    add_book.add_book_to_profile(BOOK_NAME_2)

    validate_and_remove_book = RemoveBook(driver)
    validate_and_remove_book.open_profile_page()
    validate_and_remove_book.validate_and_remove(BOOK_NAME_1)
    validate_and_remove_book.validate_and_remove(BOOK_NAME_2)


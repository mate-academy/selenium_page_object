import time

import pytest

from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys


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


def login_as_registered_user(driver, user_data):
    driver.get('https://demoqa.com/login')

    user_name_field = driver.find_element_by_css_selector('#userName')
    user_name_field.send_keys(user_data['login'])

    user_password_field = driver.find_element_by_css_selector('#password')
    user_password_field.send_keys(user_data['password'])

    login_btn = driver.find_element_by_css_selector('#login')
    login_btn.click()

    time.sleep(1)
    assert driver.find_element_by_css_selector('#userName-value').text == user_data['login']


def add_book_to_profile(driver, book_name):
    driver.get('https://demoqa.com/books')

    search_field = driver.find_element_by_css_selector('#searchBox')
    search_field.send_keys(book_name)

    buy_book_link = find_element_by_text(driver, book_name, 'span')
    buy_book_link.click()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    add_to_collection_btn = find_element_by_text(driver, 'Add To Your Collection', 'button')
    add_to_collection_btn.click()

    time.sleep(0.5)

    alert = driver.switch_to.alert
    alert.accept()


def validate_and_remove_book(driver, book_name):
    time.sleep(0.5)
    assert book_name == find_element_by_text(driver, book_name, 'a').text
    driver.find_element_by_css_selector('#delete-record-undefined').click()
    time.sleep(0.5)
    driver.find_element_by_css_selector('#closeSmallModal-ok').click()
    time.sleep(0.5)
    alert = driver.switch_to.alert
    alert.accept()


def test_add_book_to_profile_flow(driver):
    login_as_registered_user(driver, USER)
    add_book_to_profile(driver, BOOK_NAME_1)

    driver.get('https://demoqa.com/profile')

    validate_and_remove_book(driver, BOOK_NAME_1)


def test_two_add_book_to_profile_flow(driver):
    login_as_registered_user(driver, USER)
    add_book_to_profile(driver, BOOK_NAME_1)
    add_book_to_profile(driver, BOOK_NAME_2)

    driver.get('https://demoqa.com/profile')

    validate_and_remove_book(driver, BOOK_NAME_1)
    validate_and_remove_book(driver, BOOK_NAME_2)

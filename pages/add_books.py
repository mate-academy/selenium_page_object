import time


class AddBook:

    def __init__(self, driver):
        self.driver = driver

    def add_book_to_profile(self, book_name):
        self.driver.get(f'https://demoqa.com/books={book_name}')

        search_field = self.driver.find_element_by_css_selector('#searchBox')
        search_field.send_keys(book_name)

        buy_book_link = self.driver.find_element_by_text(book_name, 'span')
        buy_book_link.click()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        add_to_collection_btn = self.driver.find_element_by_text('Add To Your Collection', 'button')
        add_to_collection_btn.click()

        time.sleep(0.5)

        alert = self.driver.switch_to.alert
        alert.accept()
import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from Yandex_Page import YandexPage
import pytest

link = 'https://yandex.ru/'


def test_yandex_search():
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        current_page = YandexPage(browser)
        current_page.click_on_search()
        current_page.input_text_to_search()
        current_page.start_search_and_verify_input_field()
    finally:
        browser.quit()


def test_yandex_market():
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        current_page = YandexPage(browser)
        current_page.check_main_page_title()
        current_page.click_market_button()
        current_page.check_market_page_title()
    finally:
        browser.quit()



if __name__ == "__main__":
    pytest.main()

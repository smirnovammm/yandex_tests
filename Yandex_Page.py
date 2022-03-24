import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class YandexPage:
    def __init__(self, browser_tab):
        self.browser_tab = browser_tab
        self.search_loc = "//input[contains(@class, 'input__control')]"
        self.search_button_loc = "[class='mini-suggest__button-text']"
        self.market_button_loc = "[class='services-new__icon services-new__icon_market']"
        self.main_title_loc = "//title[contains(.,'Яндекс')]"
        self.market_title_loc = "//title[contains(.,'Яндекс.Маркет')]"
        self.first_tab_handle = browser_tab.current_window_handle
        pass

    def check_page_title(self, title_loc):
        WebDriverWait(self.browser_tab, 15).until(EC.presence_of_element_located((By.XPATH, title_loc)))

    def click_on_search(self):
        self.browser_tab.switch_to.window(self.first_tab_handle)
        self.search_input = self.browser_tab.find_element_by_xpath(self.search_loc)
        self.search_input.click()

    def input_text_to_search(self):
        self.expected_text = "Let's check search!"
        self.search_input.send_keys(self.expected_text)
        search_button = self.browser_tab.find_element_by_css_selector(self.search_button_loc)
        search_button.click()

    def start_search_and_verify_input_field(self):
        search_input = self.browser_tab.find_element_by_xpath("//input[contains(@class, 'input__control')]")
        assert search_input.get_attribute("value") == self.expected_text, 'Text in search input does not expected!'

    def click_market_button(self):
        market_button = self.browser_tab.find_element_by_css_selector(self.market_button_loc)
        market_button.click()
        self.browser_tab.switch_to.window(self.browser_tab.window_handles[1])

    def check_main_page_title(self):
        self.check_page_title(self.main_title_loc)

    def check_market_page_title(self):
        self.check_page_title(self.market_title_loc)

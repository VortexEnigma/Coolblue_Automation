from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.default_wait_time = 20
        with open ("xpath.json", "r") as file:
            self.xpath = json.load(file)


    def open_url(self):
        self.driver.get("https://www.coolblue.be/nl")

    def find_child_elements(self, xpath, tag_name):
        return self.find_element_by_xpath(xpath).find_elements(By.TAG_NAME, tag_name)

    def find_element_by_text(self, text):
        return WebDriverWait(self.driver,self.default_wait_time).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, text)))

    def find_element_by_xpath(self, xpath:str):
        return WebDriverWait(self.driver,self.default_wait_time).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def allow_cookies(self):
        self.find_element_by_xpath(self.xpath["Coolblue_Website"]["accept_cookies_button"]).click()

    def select_language(self, required_language=None):
        self.find_element_by_xpath(self.xpath["Coolblue_Website"]["languge_dropdown_button"]).click()
        language_options = self.find_child_elements(self.xpath["Coolblue_Website"]["language_dropdown_ul"], "li")
        for language_option in language_options:
            if language_option.text == required_language:
                language_option.click()

    def select_category_dropdown(self):
        self.find_element_by_xpath(self.xpath["Coolblue_Website"]["dropdown_phones"]).click()

    def select_category_iphone(self):
        self.find_element_by_xpath(self.xpath["Coolblue_Website"]["category_apple_iphone_button"]).click()

    def apple_iphone_deals(self):
        self.find_element_by_xpath(self.xpath["Coolblue_Website"]["apple_iphone_deals_button"]).click()

    def sorting_products(self):
        self.find_element_by_xpath(self.xpath["Coolblue_Website"]["sort_products_dropdown"]).click()

    def sorted_by_most_popular(self):
        sort_options = self.find_child_elements(self.xpath["Coolblue_Website"]["sort_products_dropdown"], "option")
        for sort_option in sort_options:
            if sort_option.text == "Most popular":
                sort_option.click()
                break

    def select_devices_by_amount(self, required_amount: int = 2):
        selected_devices = self.find_child_elements(self.xpath["Coolblue_Website"]["product_container"], "div")
        wanted_devices = selected_devices[:required_amount]
        for phone in wanted_devices:
            print(phone)



    def add_to_favorites(self):
        self.find_element_by_text("Save for later").click()

    def go_back(self):
        self.driver.back()

    def quit(self):
        self.driver.quit()


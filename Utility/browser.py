from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.default_wait_time = 10
        with open ("xpath.json", "r") as file:
            self.xpath = json.load(file)

    def open_url(self):
        self.driver.get("https://www.coolblue.be/nl")

    def find_element_by_xpath(self, xpath:str):
        return WebDriverWait(self.driver,self.default_wait_time).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def allow_cookies(self):
        self.find_element_by_xpath(self.xpath["Coolblue_Website"]["accept_cookies_button"]).click()

    def select_dropdown(self):
        self.find_element_by_xpath(self.xpath["Coolblue_Website"]["language_dropdown_button"]).click()

    def select_language_from_dropdown(self):
        self.find_element_by_xpath(self.xpath["Coolblue_Website"]["language_button"]).click()

    def select_category_dropdown(self):
        self.find_element_by_xpath(self.xpath["Coolblue_Website"]["dropdown_phones"]).click()

    def select_category_iphone(self):
        self.find_element_by_xpath(self.xpath["Coolblue_Website"]["category_apple_iphone_button"]).click()

    def apple_iphone_deals(self):
        self.find_element_by_xpath(self.xpath["Coolblue_Website"]["apple_iphone_deals_button"]).click()

    def sorting_products(self):
        self.find_element_by_xpath(self.xpath["Coolblue_Website"]["sort_products_dropdown"]).click()

    def sorted_by_highest_rated(self):
        self.find_element_by_xpath(self.xpath["Coolblue_Website"]["sorting_products_by_highest_rated"]).click()

    def add_to_favorites(self):
        self.find_element_by_xpath(self.xpath["Coolblue_Website"]["add_to_favorites_button"]).click()

    def go_back(self):
        self.driver.back()

    def iphone_15_plus_128gb_black(self):
            self.find_element_by_xpath(self.xpath["Coolblue_Website"]["Apple_iPhone_15_Plus_128GB_Black"]).click()

    def iphone_15_plus_128gb_pink(self):
        self.find_element_by_xpath(self.xpath["Coolblue_Website"]["Apple_iPhone_15_Plus_128GB_Pink"]).click()

    def iphone_15_plus_256_green(self):
        self.find_element_by_xpath(self.xpath["Coolblue_Website"]["Apple_iPhone_15_Plus_256GB_Green"]).click()
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
        try:
            element = WebDriverWait(self.driver, self.default_wait_time).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            print(f"Exception occurred while finding element by XPath: {xpath}")
            print(e)
            print(self.driver.page_source)

    def choose_search_engine(self):
        search_engine_options = self.driver.find_elements(By.XPATH, "//cr-radio-button")

        for option in search_engine_options:
            if "google" in option.text:
                option.click()
                break

    def confirm_search_engine(self):
        confirm_button_xpath = self.xpath["Search_engine_choice"]["confirm_search_engine"]
        self.find_element_by_xpath(confirm_button_xpath).click()

    def allow_cookies(self):
        self.find_element_by_xpath(self.xpath["Home_page"]["accept_cookies_button"]).click()

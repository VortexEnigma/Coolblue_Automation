from Utility.browser import Browser
from time import sleep

coolblue_tester = Browser()

coolblue_tester.open_url()
coolblue_tester.choose_search_engine()
coolblue_tester.confirm_search_engine()
sleep (5)
coolblue_tester.allow_cookies()
from Utility.browser import Browser
from time import sleep

coolblue_tester = Browser()

coolblue_tester.open_url()

# select default browser manually
sleep (10)

coolblue_tester.allow_cookies()
coolblue_tester.select_dropdown()
coolblue_tester.select_language_from_dropdown()
coolblue_tester.select_category_dropdown()
coolblue_tester.select_category_iphone()
coolblue_tester.apple_iphone_deals()
coolblue_tester.sorting_products()
coolblue_tester.sorted_by_highest_rated()
coolblue_tester.iphone_15_plus_128gb_black()
coolblue_tester.add_to_favorites()
coolblue_tester.go_back()

sleep(3)

coolblue_tester.iphone_15_plus_128gb_pink()
coolblue_tester.add_to_favorites()
coolblue_tester.go_back()

sleep(3)

coolblue_tester.iphone_15_plus_256_green()
coolblue_tester.add_to_favorites()
coolblue_tester.go_back()

# Review the Automation in the given time
sleep(120)
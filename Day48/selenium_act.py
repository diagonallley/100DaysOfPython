# Finding elements and interacting with them

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
URL = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(URL)


""" First way of clicking"""
# stats = driver.find_element(
#     by=By.CSS_SELECTOR, value="a[title='Special:Statistics']")


# print(stats.click())  # click the anchor tag using this method

"""Second way of clicking using link text"""

# all_portals = driver.find_element(by=By.LINK_TEXT, value="Content portals")

# all_portals.click()

toggle_button = driver.find_element(by=By.CSS_SELECTOR, value="a.cdx-button")

toggle_button.click()
# FINDING THE SEARCH BAR
search_bar = driver.find_element(
    by=By.CSS_SELECTOR, value="input[name='search']")

#TYPING IN THE SEARCH BAR
search_bar.send_keys("Python")
#PRESSING ENTER

search_bar.send_keys(Keys.ENTER)


# driver.quit()

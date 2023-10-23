from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
URL = "https://www.cricbuzz.com/live-cricket-scores/75497/aus-vs-pak-18th-match-icc-cricket-world-cup-2023"

driver.get(URL)


score = driver.find_element(
    By.CSS_SELECTOR, value="div.cb-min-bat-rw")


print(f"this the score {score}")

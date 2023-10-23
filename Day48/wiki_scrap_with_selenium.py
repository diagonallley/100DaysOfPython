from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)
stats = driver.find_element(
    by=By.CSS_SELECTOR, value="a[title='Special:Statistics']") #  #articlecount a
print(stats.text)
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

URL = "https://secure-retreat-92358.herokuapp.com/"

# time.sleep(30)
driver.get(URL)
f_name = driver.find_element(by=By.CSS_SELECTOR, value="input[name='fName']")
l_name = driver.find_element(by=By.CSS_SELECTOR, value="input[name='lName']")
email = driver.find_element(by=By.CSS_SELECTOR, value="input[name='email']")

# f_name = driver.find_element(By.NAME, "fName")
# l_name = driver.find_element(By.NAME, "lName")
# email = driver.find_element(By.NAME, "email")

# submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

f_name.send_keys("this")
l_name.send_keys("is")
email.send_keys("atestemail@email.com")
email.send_keys(Keys.ENTER)
# submit_button.click()

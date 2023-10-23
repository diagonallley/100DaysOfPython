from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36")

URL = "https://www.amazon.com/Sony-WH-1000XM5-Canceling-Headphones-Hands-Free/dp/B09XS7JWHH/ref=sr_1_4?crid=25OEADT2RAIYK&keywords=sony&qid=1697784482&sprefix=son%2Caps%2C359&sr=8-4&th=1"
URL2 = "https://pypi.org/"
URL3 = "https://www.python.org/"
driver.get(URL3)

# price = driver.find_element(by=By.ID, value="price_inside_buybox")

# search_bar = driver.find_element(by=By.NAME, value="q")
# search_bar_by_id = driver.find_element(by=By.ID, value="search")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))


# button = driver.find_element(by=By.CLASS_NAME, value="search-form__button")
# print(button.size)

# print(search_bar_by_id.tag_name)

# doc_link = driver.find_element(
#     By.CSS_SELECTOR, value=".documentation-widget a")


# print(f"this is the doc link:{doc_link.text}")
# print(price.text)
# span id="price_inside_buybox"

# driver.close()  # close single tab

status = driver.find_element(
    By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[4]/a')

print(status)

list = driver.find_elements(By.CSS_SELECTOR, value=".do-not-print")
print(list)
driver.quit()  # close browser

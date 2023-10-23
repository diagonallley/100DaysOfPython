from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import requests

from selenium.webdriver.common.action_chains import ActionChains
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument(
#     "User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
# chrome_options.add_argument("lang=en-US,en;q=0.9")  # Adjust as needed

# driver = webdriver.Chrome(chrome_options)
URL = r"https://www.zillow.com/san-francisco-ca/rentals/"
# URL_2 = ""

data = requests.get(URL, params={
    "User-Agent": "Defined",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-language": "en-US,en;q=0.9"

})
data.raise_for_status()
soup = BeautifulSoup(data.text, "html.parser")

div = soup.find("div", class_="search-page-list-header").find_next_sibling()

# print(div)

list_of_apartments = div.find_all(
    "li", class_="ListItem-c11n-8-84-3__sc-10e22w8-0")


for apartment in list_of_apartments:
    try:
        price = apartment.select_one(
            "span[data-test='property-card-price']").get_text()
        address = apartment.find_all("address")[0].get_text()
        href = apartment.select_one(
            "a[data-test='property-card-link']").get("href")
        print(price, address, href)
        # list_of_apartments.remove(apartment)
    except:
        print("------------------------------------")
        print("IN EXCEPTION!")
        # print(apartment)
        continue


print(len(list_of_apartments))

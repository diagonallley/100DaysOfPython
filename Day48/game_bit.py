from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
import time
URL = "http://orteil.dashnet.org/experiments/cookie/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)
cookie = driver.find_element(by=By.CSS_SELECTOR, value="div#cookie")
num_of_cookies = driver.find_element(by=By.CSS_SELECTOR, value="div#money")
# store = driver.find_element(by=By.CSS_SELECTOR, value="div#store")
upgrades = driver.find_elements(By.CSS_SELECTOR, "#store div")

upgrade_price = 0


def check_upgrades():
    # print(upgrades)
    global upgrades, upgrade_price, num_of_cookies
    price = 0

    upgrades = driver.find_elements(By.CSS_SELECTOR, "#store div")
    # print(len(upgrades))
    num_of_cookies = driver.find_element(by=By.CSS_SELECTOR, value="div#money")
    list_of_affordable_upgrades = []

    # for upgrade in upgrades:
    #     # print(upgrade.get_attribute("class"))
    #     if upgrade and upgrade.get_attribute("class") == None:
    #         print("yes")
    #         price = upgrade.find_element(By.TAG_NAME, "b").text
    #         price = int(price.split(" ")[2])
    #         # if num_of_cookies>
    #         if int(num_of_cookies.text) >= price:
    #             list_of_affordable_upgrades.append({
    #                 price: upgrade
    #             })
    for upgrade in upgrades:
        # print(upgrade)
        try:
            id = upgrade.get_attribute("id")
            upgrade = driver.find_element(By.ID, value=id)
        except:
            continue
        if upgrade and not upgrade.get_attribute("class"):
            price = int((upgrade.find_element(
                By.TAG_NAME, "b").text).split(" ")[2])
            # print(price)
            if int(num_of_cookies.text) >= price:
                list_of_affordable_upgrades.append({
                    price: upgrade.get_attribute("id")
                })

    list_to_return = sorted(list_of_affordable_upgrades,
                            key=lambda d: list(d.keys())[0], reverse=True)
    # print(list_to_return)
    if list_to_return:
        return list_to_return[0]
    return None


check_time = time.time()+5

time_out = time.time()+60*5
while True:
    if not time.time() >= time_out:
        cookie.click()
        # time.sleep(1)
        # print(time.time())
        if int(time.time()) % 5 == 0:
            # print("there getting upgrade")
            click = check_upgrades()

            if click:
                click_obj = list(click.keys())[0]
                id = click[click_obj]
                click_element = driver.find_element(By.ID, value=id)
                click_element.click()
        # print(num_of_cookies.text)
    else:
        break

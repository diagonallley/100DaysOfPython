from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

INSTA_URL = "https://www.instagram.com/"
URL = "https://www.instagram.com/chefsteps/"

USERNAME = ""
PWD = ""


class InstaFollower:
    def __init__(self) -> None:
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chrome_options)

    def login(self):
        # self.chrome_options.add_experimental_option("detach", True)

        # self.driver = webdriver.Chrome()

        self.driver.get(INSTA_URL)
        time.sleep(2)
        login_username = self.driver.find_element(by=By.NAME, value="username")
        login_pwd = self.driver.find_element(by=By.NAME, value="password")
        time.sleep(2)
        login_username.send_keys(USERNAME)
        login_pwd.send_keys(PWD)
        submit = self.driver.find_element(
            by=By.CSS_SELECTOR, value="button[type='submit']")
        submit.click()

    def find_followers(self):
        time.sleep(10)
        # self.driver.get(URL)
        # time.sleep(5)
        self.driver.get(url=URL+"followers")
        time.sleep(5)

        follower_div = self.driver.find_elements(
            by=By.CSS_SELECTOR, value="div.x1dm5mii")
        list_roll = self.driver.find_element(
            by=By.CSS_SELECTOR, value="div.x9f619")

        list_ = self.driver.find_element(
            by=By.CSS_SELECTOR, value="div._aano")

        # for i in range(10):
        #     time.sleep(1)
        #     self.driver.execute_script(
        #         "arguments[0].scrollTop = arguments[0].scrollHeight", list_)
        print(f"this is the length of the list {len(follower_div)}")
        i = 0
        while True:
            print(f"this is the length of the list {len(follower_div)}")

            follower_div[i].find_element(
                by=By.TAG_NAME, value="button").click()
            if int(time.time()) % 5 == 0:
                self.driver.execute_script(
                    "arguments[0].scrollTop=arguments[0].scrollHeight", list_)
            time.sleep(1)
            i += 1
            # break; ==> Add a break condition

        for follower in follower_div:
            print(f"this is the length of the list {len(follower_div)}")

            follower.find_element(by=By.TAG_NAME, value="button").click()

            if int(time.time()) % 3 == 0:
                self.driver.execute_script(
                    "arguments[0].scrollTop = arguments[0].scrollHeight", list_)
                follower_div = self.driver.find_elements(
                    by=By.CSS_SELECTOR, value="div.x1dm5mii")
            time.sleep(1)

    def follow(self):
        pass


insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()

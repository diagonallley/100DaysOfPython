from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(chrome_options)
PROMISED_UP = 40
PROMISED_DOWN = 40
SPEED_URL = "https://www.speedtest.net/"

# driver.get(SPEED_URL)


class InternetSpeedTwitterBot:
    def __init__(self, down, up, url) -> None:
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        # chrome_options.add_argument('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.down = down
        self.up = up
        self.speed_url = url

    def get_internet_speed(self):
        self.driver.get(self.speed_url)
        cookie_button = self.driver.find_element(
            By.CSS_SELECTOR, value="button#onetrust-accept-btn-handler")
        # time.sleep(5)
        # if cookie_button:
        #     cookie_button.click()
        # else:
        #     print("Not found")
        speed_go = self.driver.find_element(
            by=By.CSS_SELECTOR, value="span.start-text")
        speed_go.click()
        print("clicked")
        time.sleep(60)
        down_speed = float(self.driver.find_element(
            By.CSS_SELECTOR, "span.download-speed").text)
        upload_speed = float(self.driver.find_element(
            By.CSS_SELECTOR, "span.upload-speed").text)

        print(down_speed, upload_speed)
        if down_speed < self.down or upload_speed < self.up:
            message = f"Hey ISP, why is my internet speed {down_speed} mbps down/{upload_speed} mbps up when I pay for 30mpbs up/down ?"
            self.tweet_at_provider(message)

    def tweet_at_provider(self, message):
        self.driver = webdriver.Chrome(self.chrome_options)
        self.driver.get("https://twitter.com/home?lang=en")
        time.sleep(5)
        login_btn = self.driver.find_element(
            By.CSS_SELECTOR, "a[href='/login']")
        login_btn.click()
        time.sleep(6)
        email_input = self.driver.find_element(
            by=By.CSS_SELECTOR, value="input[autocomplete='username']")
        email_input.send_keys("pythont481@gmail.com")
        email_input.send_keys(Keys.ENTER)
        time.sleep(3)
        pwd_input = self.driver.find_element(
            by=By.CSS_SELECTOR, value="input[name='password']")
        pwd_input.send_keys("pypy007!")
        pwd_input.send_keys(Keys.ENTER)
        time.sleep(10)

        tweet_input = self.driver.find_element(
            by=By.CSS_SELECTOR, value="br[data-text='true']")
        tweet_input.send_keys(message)
        time.sleep(2)
        tweet_button = self.driver.find_element(
            by=By.XPATH, value=r"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span")
        time.sleep(1)
        tweet_button.click()


speed_bot = InternetSpeedTwitterBot(PROMISED_DOWN, PROMISED_UP, SPEED_URL)
speed_bot.get_internet_speed()

# class="result-data-large number result-data-value download-speed"

# <input autocapitalize="sentences" autocomplete="username"


# //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div/span/span
# /html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div

from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36")

URL = "https://www.python.org"
class_name = "medium-widget event-widget last"


driver.get(URL)

events = driver.find_element(
    by=By.CSS_SELECTOR, value="div.medium-widget.event-widget.last ul")  # here we are getting the div which contains all the elements


dict_of_events = {}

# from the above selected div, we are extracting the li element
li_elements = events.find_elements(by=By.TAG_NAME, value="li")

for i, li in enumerate(li_elements):  # looping over the list of li
    # finding the time element
    time = li.find_element(by=By.TAG_NAME, value="time")
    # finding the anchor element for each li element in ul
    a = li.find_element(by=By.TAG_NAME, value="a")
    dict = {"time": time.get_attribute("datetime").split("T")[
        0], "name": a.text}

    dict_of_events[i] = dict
    # i += 1

# print(events)


print(dict_of_events)  # getting the list of events
driver.quit()

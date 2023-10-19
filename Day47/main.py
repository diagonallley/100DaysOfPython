from bs4 import BeautifulSoup
import requests
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pyperclip
import json
import os
import re
import smtplib

def send_mail(price):
    with smtplib.SMTP("smtp.google.com")


MIN_PRICE = 350.00

URL = "https://www.amazon.com/Sony-WH-1000XM5-Canceling-Headphones-Hands-Free/dp/B09XS7JWHH/ref=sr_1_5?crid=ZK8BHRQZQ0FS&keywords=sony+headphones&qid=1697736306&sprefix=sony+hea%2Caps%2C428&sr=8-5"
# URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
session = requests.Session()

HEADERS = {
    "User-Agent": "Defined",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,km;q=0.5,zh-TW;q=0.4",
}
res = requests.get(URL, headers=HEADERS)


res.raise_for_status()


# print(res.text)


soup = BeautifulSoup(res.text, "html.parser")
# price = soup.select("span.a-price-whole")
price = soup.select("span#price_inside_buybox")[0].get_text()
pattern = re.compile("[0-9]+.[0-9]+")
int_price = float(pattern.search(price).group())
print(int_price)
if int_price < MIN_PRICE:
    send_mail(int_price)

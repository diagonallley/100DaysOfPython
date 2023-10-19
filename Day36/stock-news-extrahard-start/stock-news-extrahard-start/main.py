import os
import requests
from twilio.rest import Client

STOCK = "TATASTEEL.BSE"
COMPANY_NAME = "TATA STEEL"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_KEY = "E4KBIMM5SA7UPZKS"
NEWSAPI_KEY = "fbd8b1d464e744159045f63ff2926b67"
# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
data = requests.get(STOCK_ENDPOINT, params={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_KEY
})

data.raise_for_status()

list_of_stockdata = [v for k, v in data.json()["Time Series (Daily)"].items()]

yest_data = list_of_stockdata[0]
yest_closing_price = yest_data["4. close"]


day_before_yest_data = list_of_stockdata[1]
day_before_yest_closing_price = day_before_yest_data["4. close"]


difference = (float(yest_closing_price) -
              float(day_before_yest_closing_price))
up_down = None
if difference > 0:
    up_down = "⬆️📈"
else:
    up_down = "⬇️📉"
print(difference)

percentage_difference = round(
    (difference/float(yest_closing_price))*100, 2)
print(percentage_difference)

if abs(percentage_difference) > 1:
    print("Get News")

    data = requests.get(NEWS_ENDPOINT, params={
        "apiKey": NEWSAPI_KEY,
        # "language": "English",
        "qInTitle": COMPANY_NAME
    })

    posts = data.json()["articles"]
    articles = posts[0:3]

    ret_arr = [f"{item['title']}:{item['description']}" for item in articles]
    print(ret_arr)

    account_sid = "AC1d880e4709af6139d7198b7a0c60d556"
    auth_token = os.environ.get("TWILIO_TOKEN")
    client = Client(account_sid, auth_token)
    for article in ret_arr:
        message = client.messages.create(
            to="+918369789524", from_="+12245854646", body=f"The stock went {abs(difference)} % {up_down}\n{article}")
# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:c
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

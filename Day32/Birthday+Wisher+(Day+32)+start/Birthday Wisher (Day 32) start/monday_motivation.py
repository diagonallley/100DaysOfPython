import datetime
import smtplib
from random import choice
user = "pythont481@gmail.com"
pwd = "kifq facl nzjw tmqj"

if datetime.datetime.now().weekday() == 0:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()

    quote = choice(quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=user, password=pwd)

        connection.sendmail(from_addr=user, to_addrs="007shubham007@gmail.com",
                            msg=f"Subject:Monday motivation\n\n{quote}")

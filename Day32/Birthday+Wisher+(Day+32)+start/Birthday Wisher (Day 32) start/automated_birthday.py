import datetime
import smtplib
import pandas as pd
from random import randint, choice
import os
user = os.environ.get("GMAIL_USER")
pwd = os.environ.get("GMAIL_PWD")


list_of_letters = []
birthdays_today = []
for i in range(1, 4):
    with open(f"letter_temp/letter_{i}.txt", "r") as file:
        letter = file.read()
        list_of_letters.append(letter)

birthdays = pd.read_csv("birthdays.csv")
# birthdays_ = {(data_row["month"], data_row["day"]): data_row
#               for (index, data_row) in birthdays.iterrows()}

# print(birthdays_)

dict_ = birthdays.to_dict(orient="records")
# print(dict_)

for el in dict_:
    if ((el["month"] == datetime.datetime.now().month) and (el["day"] == datetime.datetime.now().day)):
        birthdays_today.append({
            "name": el["name"],
            "email": el["email"]
        })


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=user, password=pwd)
    for birthday in birthdays_today:
        letter = choice(list_of_letters)
        letter = letter.replace("[NAME]", birthday["name"])
        message = f"Subject:HBD!\n\n{letter}"

        connection.sendmail(
            from_addr=user, to_addrs=birthday["email"], msg=message)

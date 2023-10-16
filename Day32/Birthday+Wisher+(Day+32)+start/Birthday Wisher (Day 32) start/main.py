# import smtplib


# my_email = "pythont481@gmail.com"
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     pwd = "kifq facl nzjw tmqj"
#     connection.starttls()  # encryption
#     connection.login(user=my_email, password=pwd)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="007shubham007@gmail.com", msg="Subject:Hello\n\nThis is the mail")

#     # connection.close()

import datetime as dt

now = dt.datetime.now()
print(now.year)  # int
print(now.weekday())
if now.year == 2023:
    print("Yes")


date_of_birth = dt.datetime(year=1998, month=10, day=3)

print(date_of_birth)

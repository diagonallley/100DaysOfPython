import requests
from datetime import datetime
import smtplib
import time
MY_LAT = 19.075983  # Your latitude
MY_LONG = 72.877655  # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.

    if MY_LAT <= iss_latitude <= MY_LAT and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    user = "pythont481@gmail.com"
    pwd = "kifq facl nzjw tmqj"
    print(is_night())
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=user, password=pwd)
            connection.sendmail(from_addr=user, to_addrs=user,
                                msg=f"Subject:Look Up🛰️\n\nThe ISS is above you.")

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

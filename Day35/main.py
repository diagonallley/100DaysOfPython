import requests
import os
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {"https": os.environ["https_proxy"]} # for hosted code

# region Constants used for the weather API
API_KEY = os.environ.get("OWM_API_KEY")
LONG = 72.8479
LAT = 19.0144
city = "Mumbai"

# URL = "https://api.openweathermap.org/data/2.5/weather"
URL = "https://api.openweathermap.org/data/2.5/onecall"
ACCOUNT_SID = "AC1d880e4709af6139d7198b7a0c60d556"
AUTH_TOKEN = os.environ.get("TWILIO_TOKEN")
# endregion


def get_hourly_weather() -> list:
    '''
    Gets weather data using the openweather api, excludes minutely, daily and gets hourly weather data. Strips irrelvant data and compiles weather condition codes into a list.
    '''
    data = requests.get(URL, params={
        "lat": LAT,
        "lon": LONG,
        "appid": API_KEY,
        "exclude": "minutely,daily,current",
        "units": "metric"
    })
    data.raise_for_status()

    # Takes data only for the first twelve hours
    weather_data = data.json()["hourly"][0:12]
    return weather_data


def send_message() -> None:
    '''
    Makes use of the twilio api to send a sms
    '''
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        to="+918369789524", from_="+12245854646", body="Hi,\nIt will rain🌧️ today.Remember to take an umbrella ☂️ today!")

    print(message.sid)


def will_it_rain(weather_data) -> None:
    '''
    Takes a list of hourly weather data and iterates over it to check if any of the hourly weather data indicates a weather condition code less than 700 (rain).
    '''
    will_it_rain = False

    for hour in weather_data:
        weather_condition_code = hour["weather"][0]["id"]
        print(weather_condition_code)
        if int(weather_condition_code) < 700:
            will_it_rain = True
            break
    if will_it_rain:
        print("It will rain! Bring an Umbrella")
        send_message()
    else:
        print("Does not look like it will rain!")


weather_data = get_hourly_weather()
# print(weather_data)
will_it_rain(weather_data)

send_message()

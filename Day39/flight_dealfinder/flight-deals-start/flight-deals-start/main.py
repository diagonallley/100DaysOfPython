# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import json
import requests
import pyperclip
import datetime
from dateutil.relativedelta import relativedelta
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "BOM"
# SHEETY

AUTH = "Basic ZGlhZ29uYWxsZXk6ZWV3cnF5dXRpd3J0eQ"
END_POINT_SHEETY = "https://api.sheety.co/68fbf06139fe3354aae967c6b57d5bc3/flightDeals/prices"

sheety_res = requests.get(END_POINT_SHEETY, headers={
    "Authorization": "Basic ZGlhZ29uYWxsZXk6ZWV3cnF5dXRpd3J0eQ=="
})

sheety_res.raise_for_status()


flight_search = FlightSearch()
data_manager = DataManager()
# pprint(sheety_res.json())
sheet_data = sheety_res.json()["prices"]
is_iata_code = None
for city in sheet_data:
    if city["iataCode"] == "":
        is_iata_code = False
        city_name = city["city"]
        # print(city_name)
        iata_code = flight_search.get_iata_code(
            city_name)["locations"][0]["code"]
        city["iataCode"] = iata_code
        # print(city["iataCode"])
        data_manager.put_row(city)
    else:
        is_iata_code = True

pprint(sheet_data)

tommorrow = datetime.datetime.now()+datetime.timedelta(days=1)
six_monts_from_today = datetime.datetime.now()+datetime.timedelta(days=(6*30))

notification_manager = NotificationManager()
for destintation in sheet_data:
    flight = flight_search.search_flights(
        ORIGIN_CITY_IATA, destintation["iataCode"], from_time=tommorrow, to_time=six_monts_from_today)

    if flight:
        print(f" THis is the flight price found {flight.price}")
        print(
            f"This is  the price in original price {destintation['lowestPrice']}")
        if flight.price < destintation["lowestPrice"]:
            notification_manager.send_sms(
                message=f"Low price alert! Only Rs.{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}"
            )
    else:
        print("UGHHH")

import requests
import datetime
from dateutil.relativedelta import relativedelta
from flight_data import FlightData
import pyperclip
import json


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_iata_code(self, city):
        TEQUILA_KEY = "COTCSllKS6jtVUmf61oSXmkeirFDbW7L"
        URL = "https://api.tequila.kiwi.com/locations/query"

        auth = {
            "apikey": TEQUILA_KEY
        }

        iata_res = requests.get(URL, params={
            "term": city
        }, headers=auth)

        iata_res.raise_for_status()
        return iata_res.json()

    def search_flights(self, origin_city_IATA, destination_city_code, from_time, to_time):
        TEQUILA_KEY = "COTCSllKS6jtVUmf61oSXmkeirFDbW7L"
        URL = "https://api.tequila.kiwi.com/v2/search"

        auth = {
            "apikey": TEQUILA_KEY
        }

        params = {
            "fly_from": origin_city_IATA,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR"
        }
        try:
            flight_deal_res = requests.get(URL, params=params, headers=auth)
            pyperclip.copy(json.dumps(flight_deal_res.json()))
            data = flight_deal_res.json()["data"][0]
        except IndexError:
            print(f"No flights round for {destination_city_code}")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        print(f"{flight_data.destination_city}:Rs.{flight_data.price}")
        return flight_data

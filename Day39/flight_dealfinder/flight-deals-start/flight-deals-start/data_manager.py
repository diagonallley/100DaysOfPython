import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self) -> None:
        self.URL = "https://api.sheety.co/68fbf06139fe3354aae967c6b57d5bc3/flightDeals/prices/"

        pass

    def put_row(self, city):
        put_res = requests.put(self.URL+str(city["id"]), json={
            "price": {
                "city": city["city"],
                "iataCode": city["iataCode"],
                "lowestPrice": city["lowestPrice"]
            },
        }, headers={
            "Authorization": "Basic ZGlhZ29uYWxsZXk6ZWV3cnF5dXRpd3J0eQ=="
        })
        # print(put_res.json())

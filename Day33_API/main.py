import requests
import time
URL = "http://api.open-notify.org/iss-now.json"

data = requests.get(URL)
data.raise_for_status()

lat_long = data.json()
# print(lat_long["iss_position"])
lat_long = (lat_long["iss_position"]["latitude"],
            lat_long["iss_position"]["longitude"])

print(lat_long)

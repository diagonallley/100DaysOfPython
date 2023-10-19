import datetime
import requests
API__KEY = "2c1f1e85a1d272c2dab17e9e6179107f"
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
gender = "Male"
APP_ID = "b60367f9"
query = input("What did you do today?: ")
AUTH = {
    "x-app-id": APP_ID,
    "x-app-key": API__KEY
}
post_res = requests.post(URL, json={
    "query": query,

}, headers=AUTH)

ex = post_res.json()["exercises"]
print(type(ex))

SHEETY_UTL = "https://api.sheety.co/68fbf06139fe3354aae967c6b57d5bc3/myWorkouts/workouts"

date_to = datetime.datetime.now()
date_to_str = date_to.strftime("%d/%m/%Y")
time_ = datetime.datetime.now()
time_str = time_.strftime("%H:%M:%S")

print(date_to_str, time_str)
for exercise in ex:
    row = {
        "workout": {
            "date": date_to_str,
            "time": time_str,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    post_sheet_res = requests.post(SHEETY_UTL, json=row, headers={
        "Authorization": "Basic c2h1YmhhbTppb3dvZWZld2l2amVkdg"
    })

    print(post_sheet_res.json())

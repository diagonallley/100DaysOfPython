
import datetime
import requests
USER_URL = "https://pixe.la/v1/users"

API_TOKEN = "hjwikqwjejqjqjqjwkq1"
USER_NAME = "diag0nalley"
AUTH = {
    "X-USER-TOKEN": API_TOKEN
}

# user_params = {
#     "token": API_TOKEN,
#     "username": "diag0nalley",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# create_user = requests.post(USER_URL, json=user_params)

# print(create_user.json())

# {'message': "Success. Let's visit https://pixe.la/@diag0nalley , it is your profile page!", 'isSuccess': True}


# Create a graph :
# $ curl -X POST https://pixe.la/v1/users/a-know/graphs -H 'X-USER-TOKEN:thisissecret' -d '{"id":"test-graph","name":"graph-name","unit":"commit","type":"int","color":"shibafu"}'
# {"message":"Success.","isSuccess":true}


# CREATE A GRAPH
# GRAPH_URL = f"https://pixe.la/v1/users/{USER_NAME}/graphs"
# graph_config = {
#     "id": "graph1",
#     "name": "Reading Graph",
#     "unit": "pages",
#     "type": "int",
#     "color": "ajisai"

# }
# create_graph = requests.post(GRAPH_URL, json=graph_config, headers={
#                              "X-USER-TOKEN": API_TOKEN})

# graph_create = create_graph.json()
# print(graph_create)

GRAPH_ID = "graph1"
# $ curl -X POST https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5"}'
# {"message":"Success.","isSuccess":true}

VAL_URL = f"https://pixe.la/v1/users/{USER_NAME}/graphs/{GRAPH_ID}"

# data_time = datetime.datetime(year=2023, month=10, day=17)
data_time = datetime.datetime.now()
date = data_time.strftime("%Y%m%d")
print(date)
update_graph = requests.post(VAL_URL, json={
    "date": date,
    "quantity": input("How many pages did you read today?")
}, headers={
    "X-USER-TOKEN_": API_TOKEN
})

print(update_graph.json())


# PUT A PIXEL
date_put = datetime.datetime(year=2023, month=10, day=17)
date_time_put = date_put.strftime("%Y%m%d")
PUT_URL = f"https://pixe.la/v1/users/{USER_NAME}/graphs/{GRAPH_ID}/{date_time_put}"

# print(date_time_put)
# put_res = requests.put(PUT_URL, json={
#     "quantity": "36"
# }, headers={
#     "X-USER-TOKEN": API_TOKEN
# })

# print(put_res.json())

# AUTHORIZATION = {
#     "X-USER-TOKEN": API_TOKEN
# }
# # DELETE A PIXEL
# DEL_URL = PUT_URL

# del_res = requests.delete(DEL_URL, headers={
#     "X-USER-TOKEN": API_TOKEN
# })

# print(del_res.json())

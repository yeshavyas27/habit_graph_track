import requests
from datetime import datetime
USERNAME = "yeshaha"
TOKEN = "ndjsdfebhfb"
GRAPH_ID = "graphsteps"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
ADD_PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
DATE = "20221120"
UPDATE_ENDPOINT = f"{ADD_PIXEL_ENDPOINT}/{DATE}"

user_parameters = {
    "token":"ndjsdfebhfb",
    "username": "yeshaha",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#set up user name and then commented it
# response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
# print(response.text)
graph_config = {
    "id":"graphsteps",
    "name": "mysteps",
    "unit": "steps",
    "type": "int",
    "color": "ajisai"
}

header={
    "X-USER-TOKEN": TOKEN
}

# # set up graph
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=header)
# print(response.text)


# post a pixel
today = datetime().now()
post_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many steps did you walk today?")
}
response = requests.post(url=ADD_PIXEL_ENDPOINT, json=post_pixel_params, headers=header)
print(response.text)
#
# update_parameters = {
#     "quantity": "1000",
#
# }
# response = requests.put(url=UPDATE_ENDPOINT, json=update_parameters, headers=header)
# print(response.text)

#delete a datapoint or pixel
# response = requests.delete(url=UPDATE_ENDPOINT, headers=header)
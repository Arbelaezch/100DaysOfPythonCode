# Habit tracker using Pixela API. Run code and input how many hours you coded today.
# Graph can be viewed at https://pixe.la/v1/users/arbelaezch/graph1.html
# New graphs can be created by modifying the Create a Graph commented out code.

import json
import requests
import datetime
from datetime import date, timedelta

USERNAME = "arbelaezch"
TOKEN = "wrfarfrafrewf"
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
coding_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

user_params = {
	"token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_config = {
	"id": 'graph1',
	"name": "Coding Graph",
	"unit": "hours",
	"type": "int",
	"color": "ajisai",
}

headers = {
	"X-USER-TOKEN": TOKEN
}


# Correctly formats today's date.
today = (date.today())
yesterday = today - timedelta(days=2)
today = today.strftime('%Y%m%d')




graph1_params = {
	"date": today,
	"quantity": input("How many hours did you spend coding today? "),
}


# Creates user on pixela.
# response = requests.post(url=pixela_endpoint, json=user_params)

# Creates new graph at https://pixe.la/v1/users/arbelaezch/graph1.html
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)


# Posts initial data input.
response = requests.post(url=coding_graph_endpoint, json=graph1_params, headers=headers)
# print(response)




# UPDATES GRAPH
new_pixel_data = {
	"quantity": "2"
}


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{yesterday.strftime('%Y%m%d')}"

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response)
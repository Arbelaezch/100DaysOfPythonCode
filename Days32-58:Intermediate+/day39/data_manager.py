import os
import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/25a373f2cdc1020608b07ae17070e3a4/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/25a373f2cdc1020608b07ae17070e3a4/flightDeals/users"
header = {"Authorization": "Bearer iouwbefvpunpwefv"}	



class DataManager:
# Interactions between google sheet and flight data.
 
	def __init__(self) -> None:
		self.destination_data = {}

	def get_destination_data(self):
	# GETs and returns google sheet data.
		response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=header)
		data = response.json()
		self.destination_data = data["prices"]
		return self.destination_data

	def update_destination_code(self):
    # PUTs updated cities' IATA codes in google sheet.
		for city in self.destination_data:
			new_data = {
				"price": {
					"iataCode": city["iataCode"]
				}
			}

			response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",json=new_data,headers=header)
			print(response)

	def get_user_data(self):
		response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=header)
		return response.json()["users"]
		
		



import os
import requests
from pprint import pprint




#This class is responsible for talking to the Google Sheet.
class DataManager:
    
	def __init__(self) -> None:
		self.API_TOKEN = os.environ.get("SHEETY_TOKEN")
		self.API_ENDPOINT = "https://api.sheety.co/25a373f2cdc1020608b07ae17070e3a4/flightDeals/prices"
  
		self.header = {
			"Authorization": "Bearer iouwbefvpunpwefv"
		}
		self.destination_data = {}

	def get_cuttoff_price(self):
		response = requests.get(url=self.API_ENDPOINT, headers=self.header)
		data = response.json()
		self.destination_data = data["prices"]
		return self.destination_data

	def update_iataCodes(self, sheet_data):
		# print(sheet_data)
		for city in sheet_data:
			# print(city["iataCode"])
			new_data = {
				"price": {
					"iataCode": city["iataCode"]
				}
			}

			response = requests.put(url=f"{self.API_ENDPOINT}/{city['id']}",json=new_data,headers=self.header)
			print(response)
		



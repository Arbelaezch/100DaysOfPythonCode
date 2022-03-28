import json
import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
	def __init__(self) -> None:
		self.API_KEY = "bMwOt5MqY14A8fwJrzn_2Da6umQ_Y92W"
		self.API_ID = "arbelaezchflightsearch"
		self.API_ENDPOINT = "https://tequila-api.kiwi.com"
	
	def get_iataCode(self, sheet_data):
		for city in sheet_data:
			header = {
				"apikey": self.API_KEY
			}
			params = {
				"term": city["city"],
				"location_types": "city"
			}
			response = requests.get(url=f"{self.API_ENDPOINT}/locations/query",headers=header,params=params)
			data = response.json()
			city["iataCode"] = data["locations"][0]["code"]
			
		
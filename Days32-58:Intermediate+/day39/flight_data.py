from email import header
from time import strftime
import requests
from datetime import timedelta, datetime

class FlightData:
    #This class is responsible for structuring the flight data.
    
	def __init__(self) -> None:
		self.departure_city = "Edmonton"
		self.departure_airport_code = "YEG"
		self.ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
		self.API_KEY = "bMwOt5MqY14A8fwJrzn_2Da6umQ_Y92W"
		self.header = {"apikey": self.API_KEY}
		self.price = 0
		self.today = datetime.now()
		self.today = self.today.strftime("%d/%m/%Y")
		self.date_cutoff = datetime.now() + timedelta(weeks=26)
		self.date_cutoff = self.date_cutoff.strftime("%d/%m/%Y")
	
	def get_flight(self, city):
		params = {
			"fly_from": f"airport:{self.departure_airport_code}",
			"fly_to": city["iataCode"],
			"date_from": self.today,
			"date_to": self.date_cutoff,
			"nights_in_dst_from": 5,
			"nights_in_dst_to": 14,
			"flight_type": "round",
			"one_for_city": 1,
			"adults": 2,
			"curr": "CAD"
		}
		response = requests.get(url=self.ENDPOINT, headers=self.header, params=params)
		data = response.json()
		return data["data"][0]

#   we're looking only for direct flights, that leave anytime between tomorrow and in 6 months (6x30days) time. We're also looking for round trips that return between 7 and 28 days in length. The currency of the price we get back should be in GBP.
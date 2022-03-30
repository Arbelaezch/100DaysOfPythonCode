import json
from pprint import pprint
import requests
from datetime import timedelta, datetime
from time import strftime
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "bMwOt5MqY14A8fwJrzn_2Da6umQ_Y92W"
header = {"apikey": TEQUILA_API_KEY}


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
	def __init__(self):
		pass
	

	def get_destination_code(self, city_name):
		# Returns the IATA code of the provided city.
		query = {
			"term": city_name,
			"location_types": "city"
		}
		response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query",headers=header,params=query)

		results = response.json()["locations"]
		code = results[0]["code"]


	def get_flight(self, departure_city_code, destination_city_code, from_time, to_time):
		query = {
			"fly_from": departure_city_code,
			"fly_to": destination_city_code,
			"date_from": from_time.strftime("%d/%m/%Y"),
			"date_to": to_time.strftime("%d/%m/%Y"),
			"nights_in_dst_from": 5,
			"nights_in_dst_to": 20,
			"flight_type": "round",
			"one_for_city": 1,
			"adults": 1,
			"max_stopovers": 0,
			"curr": "CAD"
		}
		response = requests.get(
		    url=f"{TEQUILA_ENDPOINT}/v2/search", headers=header, params=query)

		try:
			data = response.json()["data"][0]
			print(f"{destination_city_code} {data['price']}")
		except IndexError:
			try:
				query = {
					"fly_from": departure_city_code,
					"fly_to": destination_city_code,
					"date_from": from_time.strftime("%d/%m/%Y"),
					"date_to": to_time.strftime("%d/%m/%Y"),
					"nights_in_dst_from": 5,
					"nights_in_dst_to": 20,
					"flight_type": "round",
					"one_for_city": 1,
					"adults": 1,
					"max_stopovers": 3,
					"curr": "CAD"
				}
				response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=header, params=query)

				data = response.json()["data"][0]
				print(f"{destination_city_code} {data['price']}")

			except IndexError:
				print(f"No flights found for {destination_city_code}.")
				return None
			else:
				flight_data = FlightData (
					price=data["price"],
					origin_city=data["route"][0]["cityFrom"],
					origin_airport=data["route"][0]["flyFrom"],
					destination_city=data["route"][1]["cityTo"],
					destination_airport=data["route"][1]["flyTo"],
					out_date=data["route"][0]["local_departure"].split("T")[0],
					return_date=data["route"][2]["local_departure"].split("T")[0],
					stop_overs=1,
					via_city=data["route"][0]["cityTo"]
				)
				return flight_data
			
		else:
			flight_data = FlightData (
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                via_city=""
            )
			return flight_data
			
		
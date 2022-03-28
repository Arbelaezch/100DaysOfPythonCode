import os
from  data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch
from flight_data import FlightData
from pprint import pprint
from datetime import datetime

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


data_manager = DataManager()
sheet_data = data_manager.get_cuttoff_price()

twilio = NotificationManager()

# flight = FlightSearch()

# FlightSearch.get_iataCode(flight, sheet_data)

# DataManager.update_iataCodes(data_manager, sheet_data)
# pprint(sheet_data)


flight_data_manager = FlightData()
for city in sheet_data:
	flight = flight_data_manager.get_flight(city)
	if flight["price"] <= city["lowestPrice"]:
		from_date = flight["route"][0]["local_departure"].split("T")
		to_date = flight["route"][1]["local_arrival"].split("T")
		twilio.send_sms(flight["price"], city["city"], city["iataCode"], from_date[0], to_date[0])







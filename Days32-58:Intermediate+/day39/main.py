import os
from  data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch
from flight_data import FlightData
from pprint import pprint
from datetime import datetime, timedelta

# Have users sign up through https://replit.com/@arbelaezch/FlightClub#main.py

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "YEG"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        data_manager.destination_data = sheet_data
        data_manager.update_destination_code()


tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6 * 30))


for city in sheet_data:
	flight = flight_search.get_flight(ORIGIN_CITY_IATA, city["iataCode"], from_time=tomorrow, to_time=six_months_from_today)

	if flight is None:
		continue
 
	# Sends text message if price is lower than requirement.
	if flight.price <= city["lowestPrice"]:
		from_date = flight.out_date
		to_date = flight.return_date
		# notification_manager.send_sms(flight.price, city["city"], city["iataCode"], from_date, to_date, via_city=flight.via_city)
		user_data = data_manager.get_user_data()
		for user in user_data:
			# link = f"https://www.google.com/flights?hl=en#flt={city['city']}.{city['iataCode']}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

			notification_manager.send_emails(user["email"], flight.price, city["city"], city["iataCode"], from_date, to_date, via_city=flight.via_city)







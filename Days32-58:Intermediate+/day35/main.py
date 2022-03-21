import requests
import os
from twilio.rest import Client

API_KEY = os.environ['OWM_API_KEY']
lat = 53
lon = -113
TWILIO_PHONE = "16592072604"
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# ENTER DESIRED PHONE NUMBER TO RECEIVE MESSAGES
to_phone = "123456"



OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_parameters = {
    "lat":  53.637020,
    "lon": -113.620071,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

# response = requests.get(url="https://api.openweathermap.org/data/2.5/weather?", params=parameters)




one_call_response = requests.get(OWM_Endpoint, params=weather_parameters)

data = one_call_response.json()
one_call_response.raise_for_status()
weather_slice = data["hourly"][:12]

is_rain = False

for hour_data in weather_slice:
	condition_code = hour_data["weather"][0]["id"]
	if int(condition_code) < 700:
		is_rain = True

if True:
	client = Client(account_sid, auth_token)

	message = client.messages \
					.create(
						body="It's going to rain today. Remember to bring an umbrella.",
						from_=TWILIO_PHONE,
						to=to_phone
					)

	print(message.status)

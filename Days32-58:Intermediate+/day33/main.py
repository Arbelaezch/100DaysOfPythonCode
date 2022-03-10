import requests
from datetime import datetime
from dateutil import tz
import re
import smtplib
import time

my_email = "christian.arbelaez2@gmail.com"
password = "\F*r6MD6be,qFSQ^"


response = requests.get(url="http://api.open-notify.org/iss-now.json")

data = response.json()
response.raise_for_status()

latitude = float(data["iss_position"]["latitude"])
longitude = float(data["iss_position"]["longitude"])

iss_position = (latitude, longitude)


MY_LAT = 53.637
MY_LONG = -113.62


parameters = {
    "lat":  MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(
    url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]


# Hardcode zones:
from_zone = tz.gettz('UTC')
to_zone = tz.tzlocal()

sunrise_list = re.split('[T+]', sunrise)
utcSunrise = str(sunrise_list[0]) + " " + str(sunrise_list[1])
utc_sunrise_datetime = datetime.strptime(utcSunrise, '%Y-%m-%d %H:%M:%S')

sunset_list = re.split('[T+]', sunset)
utcSunset = str(sunset_list[0]) + " " + str(sunset_list[1])
utc_sunset_datetime = datetime.strptime(utcSunset, '%Y-%m-%d %H:%M:%S')


# Tell the datetime object that it's in UTC time zone since
# datetime objects are 'naive' by default
utc_sunrise_datetime = utc_sunrise_datetime.replace(tzinfo=from_zone)
utc_sunset_datetime = utc_sunset_datetime.replace(tzinfo=from_zone)

# Convert time zone
sunrise_mst = utc_sunrise_datetime.astimezone(to_zone)
sunset_mst = utc_sunset_datetime.astimezone(to_zone)

time_now = datetime.now()

while 1:
	time.sleep(60)
	if int(time_now.hour) <= int(sunrise_mst.hour) or int(time_now.hour) >= int(sunset_mst.hour):
		if ((MY_LAT - 5) < latitude < (MY_LAT + 5)) and ((MY_LONG - 5) < longitude < (MY_LONG + 5)):
			with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
				connection.starttls()

				connection.login(user=my_email, password=password)

				connection.sendmail(
					from_addr=my_email,
					to_addrs="arbelaezch@gmail.com",
					msg="Subject:Look Up! :)\n\nThe ISS is overhead! :)"
				)

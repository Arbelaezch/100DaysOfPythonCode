import os
import requests
from twilio.rest import Client
import smtplib




# Sends notifications with the deal flight details.
class NotificationManager:
	def __init__(self) -> None:
		self.API_SID = "ACa9ee87edff08ce5fac674f90afd7213a"
		self.API_TOKEN = "1af8265843341b73a97494c05819e4c2"
		self.TWILIO_PHONE = "16592072604"
		self.to_phone = "7806684816"
  
	def send_sms(self, price, destination, dst_code, from_date, to_date, via_city=""):
		if via_city != "":
			via_city = f" via {via_city}"

		client = Client(self.API_SID, self.API_TOKEN)

		message = client.messages \
						.create(
							body=f"Low price alert! Only ${price} CAD to fly from Edmonton-YEG to {destination}-{dst_code}{via_city}, from {from_date} to {to_date}.",
							from_=self.TWILIO_PHONE,
							to=self.to_phone
						)

		print(message.status)

	def send_emails(self, email, price, destination, dst_code, from_date, to_date, via_city=""):
		my_email = "christian.arbelaez2@gmail.com"
		password = "\F*r6MD6be,qFSQ^"
  
		if via_city != "":
			via_city = f" via {via_city}"

		# Connect to your email.
		with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
			connection.starttls()
			
			connection.login(user=my_email, password=password)
   
			contents = f"Low price alert! Only ${price} CAD to fly from Edmonton-YEG to {destination}-{dst_code}{via_city}, from {from_date} to {to_date}."


			connection.sendmail(
				from_addr=my_email,
				to_addrs=email,
				msg=f"Subject:Cheap Flights\n\n{contents}"
        )
  



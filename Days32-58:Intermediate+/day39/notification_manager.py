import os
import requests
from twilio.rest import Client


#This class is responsible for sending notifications with the deal flight details.

class NotificationManager:
	def __init__(self) -> None:
		self.API_SID = "ACa9ee87edff08ce5fac674f90afd7213a"
		self.API_TOKEN = "d7b96958416f5b439ef2a453bce8770c"
		self.TWILIO_PHONE = "16592072604"
		self.to_phone = "7806684816"
  
	def send_sms(self, price, destination, dst_code, from_date, to_date):
		client = Client(self.API_SID, self.API_TOKEN)

		message = client.messages \
						.create(
							body=f"Low price alert! Only ${price} CAD to fly from Edmonton-YEG to {destination}-{dst_code}, from {from_date} to {to_date}.",
							from_=self.TWILIO_PHONE,
							to=self.to_phone
						)

		print(message.status)
  



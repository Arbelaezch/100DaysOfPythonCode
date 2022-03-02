# Sends motivational emails every tuesday.

from asyncore import read
import smtplib
import datetime as dt
import random


my_email = "christian.arbelaez2@gmail.com"
password = "\F*r6MD6be,qFSQ^"
test_email = "arbelaezch@gmail.com"



# Can access year, month, day, hour, minute, second, weekday, etc
now = dt.datetime.now()
# now = now.year
# date_of_birth = dt.datetime(year=1996, month=9, day=14, hour=4)


if now.weekday() == 0:
	with open("Days32-58:Intermediate+/day32/quotes.txt", "r") as file:
		quotes_line = file.readlines()
		quote = random.choice(quotes_line)
	
	# Connect to your email.
	with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
		# Makes connection secure.
		connection.starttls()

		# Log in to email account.
		connection.login(user=my_email, password=password)

		# Send
		connection.sendmail(
			from_addr=my_email,
			to_addrs=test_email,
			msg=f"Subject:Monday Motivation\n\n{quote}"
		)


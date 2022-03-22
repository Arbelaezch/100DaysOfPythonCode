import requests
import csv
import os
from twilio.rest import Client
from datetime import datetime, timedelta, date

# Determines the last weekday.
def prev_weekday(adate):
    adate -= timedelta(days=1)
    while adate.weekday() > 4: # Mon-Fri are 0-4
        adate -= timedelta(days=1)
    return adate


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Stock keys
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
alpha_vintage_key = "3UQOYM3PX66LP6E1"

# News keys
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
newsapi_key = "46715393d46a4b6dacbf5f98ad46baaf"

# Twilio Keys and information.
API_KEY = os.environ['OWM_API_KEY']
TWILIO_PHONE = "16592072604"
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']


# ENTER DESIRED PHONE NUMBER TO RECEIVE MESSAGES
to_phone = "7806684816"


stock_parameters = {
    "function":  "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": alpha_vintage_key
}


yesterday = prev_weekday(date.today())
day_before_yesterday = prev_weekday(yesterday)

# Gets the closing prices of a stock for the last two week days.
stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()
stock_response.raise_for_status()
stock_yesterday = stock_data["Time Series (Daily)"][str(yesterday)]["4. close"]
stock_day_before_yesterday = stock_data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"]

# Determines the movement of the stock.
price_difference = float(stock_day_before_yesterday) - float(stock_yesterday)
abs_price_difference = abs(float(stock_day_before_yesterday) - float(stock_yesterday))
percentage_difference = (abs_price_difference/float(stock_yesterday))*100
percentage_difference = round(percentage_difference)
    

# Gets the most recent three news articles on the desired stock.
news_parameters = {
    "q": COMPANY_NAME,
    "sortBy": "publishedAt",
    "pageSize": 3,
    "apikey": newsapi_key
}
news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
news_data = news_response.json()
news_response.raise_for_status()
news_headline_1 = news_data["articles"][0]["title"]
news_headline_2 = news_data["articles"][1]["title"]
news_headline_3 = news_data["articles"][2]["title"]


# Sends SMS with recent news headlines if the price of stock changed by 5% or more.
if percentage_difference >= 5:
	if float(stock_yesterday) < float(stock_day_before_yesterday):
		percentage_difference *= -1
	else:
		percentage_difference = str(f"+{percentage_difference}")
	client = Client(account_sid, auth_token)

	message = client.messages \
					.create(
         				body=f"TSLA: {percentage_difference}%\nHeadline: {news_headline_1}.\n\nHeadline: {news_headline_2}.\n\nHeadline: {news_headline_3}.",
						from_=TWILIO_PHONE,
						to=to_phone
					)

	print(message.status)




# Workout tracker using Nutrition IX Natural Language parsing API and Google Sheets.
# Program accepts a natural language input string and posts the information to a google sheets db.

from time import strftime
import requests
from datetime import date, datetime
import os


# To create environment variables type into console: "export VAR_NAME=VAR_VALUE"
# Ex: export NUTRITIONIX_ID=124rrfiounwerf # NO QUOTES ON VALUE!!
APP_ID = os.environ["NUTRITIONIX_ID"]
APP_KEY = os.environ["NUTRITIONIX_KEY"]

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")



exercise_text = input("Tell me what exercise you did: ")

gender = "male"
weight = 90
height = 200
age = 25

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2"
NUTRITIONIX_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_ENDPOINT = "https://api.sheety.co/25a373f2cdc1020608b07ae17070e3a4/workoutTracker/workouts"



exercise_headers = {
	"x-app-id": APP_ID,
	"x-app-key": APP_KEY,
}

nutritionix_parameters = {
	"query": exercise_text,
	"gender": gender,
	"weight_kg": weight,
	"height_cm": height,
	"age": age
}

sheety_header = {
	"Authorization": "Bearer werfrefqwrfqrf"
}

exercise_response = requests.post(url=NUTRITIONIX_EXERCISE_ENDPOINT, json=nutritionix_parameters, headers=exercise_headers)
data = exercise_response.json()
# print(exercise_response)

now = datetime.now()

for exercise in data["exercises"]:
	sheety_inputs = {
		"workout": {
			"date": now.strftime("%d/%m/%Y"),
			"time": now.strftime("%H:%M:%S"),
			"exercise": exercise["user_input"].title(),
			"duration": exercise["duration_min"],
			"calories": exercise["nf_calories"]
		}
	}

	sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_inputs, headers=sheety_header)
# print(sheety_response)






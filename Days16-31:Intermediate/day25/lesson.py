# When you encounter a csv file, use pandas library

import pandas
import csv


# Use csv library to read data from csv files.
with open("Days16-31:Intermediate/day25/weather_data.csv") as data_file:
	data = csv.reader(data_file)
	temps = []

	# Saves a specific column of data from a table.
	for row in data:
		if row[1] != "temp":
			temps.append(int(row[1]))

# Using Pandas to get data from csv file
data = pandas.read_csv("Days16-31:Intermediate/day25/weather_data.csv")
print(data)
print(data["temp"]) # Get a specific column
print(data.temp) # Also gets a specific column by name

data_dict = data.to_dict()	# Also a to_list() function

# Return mean of a row
print(data["temp"].mean())

# Get max of column
print(data["temp"].max())

# Get Data in a row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# Create a dataframe from scratch
data_dict = {
	"students": ["Amy", "James", "Angela"],
	"scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
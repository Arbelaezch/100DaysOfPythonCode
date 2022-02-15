# Gets the number of squirrels in central park with Gray, Cinnamon, and Black fur
# and outputs to squirrel_count.csv file

import csv
import pandas as pd


data = pd.read_csv("Days16-31:Intermediate/day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = (len(data[data["Primary Fur Color"] == "Gray"]))
red = (len(data[data["Primary Fur Color"] == "Cinnamon"]))
black = (len(data[data["Primary Fur Color"] == "Black"]))


data_dict = {
	"Fur Color": ["Gray", "Red", "Black"],
	"Count": [gray, red, black]
}
squirrel_count = pd.DataFrame(data_dict)
print(squirrel_count)
squirrel_count.to_csv("Days16-31:Intermediate/day25/squirrel_count.csv")






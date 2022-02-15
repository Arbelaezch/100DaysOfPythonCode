# United States Memory Game

import csv
import pandas as pd
import turtle

IMAGE = "Days16-31:Intermediate/day25/blank_states_img.gif"


screen = turtle.Screen()
screen.setup(700, 500)
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pd.read_csv("Days16-31:Intermediate/day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")






screen.exitonclick()




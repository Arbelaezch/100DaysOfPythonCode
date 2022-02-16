# United States Memory Game
# Try to remember all of the states in the U.S. Any missed states will be exported
# to states_to_learn.csv

import csv
import pandas as pd
import turtle
from state import State

IMAGE = "Days16-31:Intermediate/day25/blank_states_img.gif"


screen = turtle.Screen()
screen.setup(700, 500)
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pd.read_csv("Days16-31:Intermediate/day25/50_states.csv")

state_list = data.state.to_list()
state_list = [x.title() for x in state_list]

correct = 0

is_game_on = 1
while is_game_on:
    answer_state = screen.textinput(
        title=f"Guess the State {correct}/50", prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state in state_list:
        del state_list[state_list.index(answer_state)] # Makes sure state can't be guessed again.
        correct += 1
        row = data[data.state == answer_state]
        name = str(row.state.values[0])
        x = int(row.x.values)
        y = int(row.y.values)

        screen.tracer(0)
        a = State(name, x, y)
        screen.tracer(1)
        screen.update()
    
    if correct == 50:
        screen.tracer(0)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.color("black")
        tim.goto((-275, 0))
        tim.write("You guessed all the states, good job!", font=("Courier", 24, "normal"))
        screen.tracer(1)
        screen.update()
        is_game_on = 0
    
    if answer_state == "Exit":
        missing_states = pd.DataFrame(state_list)
        missing_states.to_csv("Days16-31:Intermediate/day25/states_to_learn.csv")
        is_game_on = 0
        

screen.exitonclick()

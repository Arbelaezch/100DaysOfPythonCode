# Turtle Race

from turtle import Turtle, Screen
import random


WIDTH = 500
HEIGHT = 400

start_pos = -70


screen = Screen()
winner = ""

is_race_on = False
screen.setup(WIDTH, HEIGHT)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
colors = ["red", "yellow", "blue", "purple", "black", "green", "orange"]
all_turtles = []

is_race_on = True

for i in range(0,6):
	new_turtle = Turtle()
	new_turtle.shape("turtle")
	new_turtle.color(colors[i])
	new_turtle.penup()
	new_turtle.goto(x=-230, y=start_pos)
	start_pos += 30
	all_turtles.append(new_turtle)


while is_race_on:
	for turtle in all_turtles:
		random_distance = random.randint(0, 10)
		turtle.forward(random_distance)
		if turtle.xcor() >= 220:
			winner = turtle.pencolor()
			is_race_on = False


print(winner)

if winner == user_bet:
	print("Congrats, you picked the right turtle!")
else:
	print("Sorry, your turtle lost the race.")
	print(f"The winner was the {winner} turtle.")



screen.exitonclick()
from re import X
from turtle import Turtle, Screen, forward, colormode, setworldcoordinates
import random


def random_color():
	R = random.randint(0,255)
	G = random.randint(0,255)
	B = random.randint(0,255)
	random_color = (R, G, B)
	return random_color



TURTLE_SIZE = 20


screen = Screen()

colormode(255)
tim = Turtle()
tim.color("DarkGreen")


up = 0
rl = 0
x = -225
y = -225
end = 0

tim.speed(1000)
tim.hideturtle()

while end < 10:
	while up < 10:
		tim.hideturtle()
		tim.penup()
		tim.goto(x, y)
		tim.pendown()
		c = random_color()
		tim.pencolor(c)
		tim.fillcolor(c)

		tim.begin_fill()
		tim.dot(20, c)
		tim.end_fill()
		up += 1
		x += 50
	
	x = -225
	y += 50
	up = 0
	end += 1






screen.exitonclick()


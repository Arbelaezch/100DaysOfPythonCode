# Quick and dirty implementation for having the turtle draw increasing sided
# shapes, each shape as a random color. No functions created, just wanted to 
# do it quickly.

from turtle import Turtle, Screen, forward, colormode
import random



tim = Turtle()
tim.shape("turtle")
tim.color("DarkGreen")


tim.pendown()
sides = 3
i = 0
R = random.randint(0,255)
G = random.randint(0,255)
B = random.randint(0,255)
colormode(255)
tim.pencolor(R,G,B)
tim.color
end = 0
while end <= 6:
	tim.right(360/sides)
	tim.forward(100)
	i += 1
	if i == sides:
		sides += 1
		i = 0
		R = random.randint(0,255)
		G = random.randint(0,255)
		B = random.randint(0,255)
		tim.pencolor(R,G,B)
		end += 1





screen = Screen()
screen.exitonclick()
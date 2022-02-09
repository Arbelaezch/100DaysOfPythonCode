#Functions for drawing a spirograph or a random walk. 

from turtle import Turtle, Screen, forward, colormode
import random

directions = [90, 180, 270, 0]


def random_color():
	R = random.randint(0,255)
	G = random.randint(0,255)
	B = random.randint(0,255)
	random_color = (R, G, B)
	return random_color


def random_direction():
	turn = random.choice(directions)
	return turn

def random_walk():
	'''Lets turtle randomly walk for a while. Randomly changes color each time.'''
	tim.pensize(10)
	tim.speed(7)

	end = 0
	while end <= 100:
		tim.forward(20)
		tim.color(random_color())
		tim.right(random_direction())
		end += 1

def draw_spirograph():
	'''Draws a spirograph. Duh. Could increase the turn degree for different shapes.'''
	tim.pensize(1)
	tim.speed(100)

	for i in range(90):
		tim.circle(100)
		tim.left(4)
		tim.color(random_color())




colormode(255)
tim = Turtle()
tim.shape(name=None)
tim.color("DarkGreen")




draw_spirograph()






screen = Screen()
screen.exitonclick()
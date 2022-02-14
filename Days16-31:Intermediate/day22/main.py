# The Pong Game

from turtle import Turtle, Screen
import random
import time
from ball import Ball
from scoreboard import Scoreboard
from player import Player


XSIZE = 800
YSIZE = 600

screen = Screen()
screen.title("Pong")
screen.setup(width=XSIZE, height=YSIZE, startx=None, starty=None)
screen.bgcolor("black")
screen.tracer(0)

ball = Ball()
p1 = Player((-350, 0))
p2 = Player((350, 0))
score1 = Scoreboard((-100, 250))
score2 = Scoreboard((100, 250))


screen.tracer(1)
screen.update()


screen.listen()
screen.onkey(key="w", fun=p1.move_up)
screen.onkey(key="s", fun=p1.move_down)
screen.onkey(key="Up", fun=p2.move_up)
screen.onkey(key="Down", fun=p2.move_down)


is_game_on = True
while is_game_on:
	time.sleep(0.001)
	screen.update()
	ball.move()

	# Detect ball collision with paddles.
	if (ball.distance(p1) < 60 and ball.xcor() < -320) or (ball.distance(p2) < 60 and ball.xcor() > 320):
		ball.bounce_x()
	
	#Detect ball collision with wall.
	if (ball.ycor() > 280) or (ball.ycor() < -280):
		ball.bounce_y()
	

	if ball.xcor() < -380 or ball.xcor() > 380:
		if ball.xcor() < -380:
			score2.increase_score()
		elif ball.xcor() > 380:
			score1.increase_score()
		screen.tracer(0)
		screen.update()
		ball.reset()
		screen.tracer(1)
		screen.update()
	


screen.exitonclick()



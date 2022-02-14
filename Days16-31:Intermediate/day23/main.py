# Capstone Project: Turtle Crossing Game

from turtle import Turtle, Screen
from player import Player
import time
from car_manager import CarManager
from scoreboard import Scoreboard
import random

FINISH_LINE_Y = 280
XSIZE = 600
YSIZE = 600

screen = Screen()
screen.title("Frogger")
screen.setup(width=XSIZE, height=YSIZE, startx=None, starty=None)
screen.tracer(0)

# class instantiations go here
tim = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.tracer(1)


screen.listen()
screen.onkey(key="w", fun=tim.move_up)
screen.onkey(key="s", fun=tim.move_down)


speed = 0.05

is_game_on = True
while is_game_on:
	time.sleep(speed)
	screen.update()

	screen.tracer(0)
	
	car_manager.create_cars()
	car_manager.move_cars()

	# Detect car collision with turtle.
	for car in car_manager.all_cars:
		if car.distance(tim) < 20:
			scoreboard.game_over()
			car_manager.stop_cars()
			is_game_on = False
			screen.onkey(key="w", fun=tim.dead)
			screen.onkey(key="s", fun=tim.dead)
	
	# Detect turtle crosses finish line
	if tim.ycor() > FINISH_LINE_Y:
		tim.reset()
		#speed *= 0.85
		car_manager.level_up()
		scoreboard.increase_level()


	screen.tracer(1)






screen.exitonclick()
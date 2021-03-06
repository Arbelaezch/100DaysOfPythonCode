from turtle import Turtle, Screen
import random
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


XSIZE = 600
YSIZE = 600

screen = Screen()
screen.title("Snake Game")
screen.setup(width=XSIZE, height=YSIZE, startx=None, starty=None)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=snake.turn_up)
screen.onkey(key="s", fun=snake.turn_down)
screen.onkey(key="a", fun=snake.turn_left)
screen.onkey(key="d", fun=snake.turn_right)



is_game_on = True
while is_game_on:
	screen.update()
	time.sleep(0.1)
	snake.move()

	# Detect collision with food.
	if snake.head.distance(food) <= 15:
		food.refresh()
		scoreboard.increase_score()
		snake.extend()

	# Detect collision with wall.
	if (snake.head.xcor() >= 290) or (snake.head.xcor() < -295) or (snake.head.ycor() >= 295) or (snake.head.ycor() <= -290):
		scoreboard.reset()
		snake.reset()

	# Detect collision with tail.
	for segment in snake.segments:
		if segment == snake.head:
			pass
		elif snake.head.distance(segment) < 10:
			scoreboard.reset()


screen.exitonclick()




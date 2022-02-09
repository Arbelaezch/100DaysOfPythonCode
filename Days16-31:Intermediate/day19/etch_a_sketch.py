# Simulates an Etch-A-Scetch
# "w" key moves forward
# "s" key moves backward
# "a" key turns left
# "d" key turns right
# "c" key clears the screen

from turtle import Turtle, Screen

ANGLE = 15


def move_forward():
	tim.forward(10)

def move_backward():
	tim.backward(10)

def turn_left():
	tim.left(ANGLE)

def turn_right():
	tim.right(ANGLE)

def clear():
	tim.clear()
	tim.penup()
	tim.home()
	tim.pendown()


tim = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)







screen.exitonclick()



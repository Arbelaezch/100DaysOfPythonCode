from turtle import Turtle
import random

class Ball(Turtle):

	def __init__(self) -> None:
		super().__init__()
		self.penup()
		self.shape("circle")
		self.color("white")
		self.shapesize(0.5, 0.5, 1)
		self.x_move = 10
		self.y_move = 10

	def move(self):
		new_x = self.xcor() + self.x_move
		new_y = self.ycor() + self.y_move
		self.goto(new_x, new_y)
	
	def bounce_y(self):
		self.y_move *= -1

	def bounce_x(self):
		self.x_move *= -1

	def reset(self):
		self.x_move *= -1
		self.goto(self.x_move, self.y_move)


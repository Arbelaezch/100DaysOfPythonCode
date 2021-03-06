from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):

	def __init__(self) -> None:
		super().__init__()
		self.penup()
		self.shape("turtle")
		self.color("green")
		self.setheading(90)
		self.goto(0, -270)


	def move_up(self):
		self.forward(30)
	
	def move_down(self):
		self.backward(30)

	def reset(self):
		self.goto(0, -270)

	def dead(self):
		pass
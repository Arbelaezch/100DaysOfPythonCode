from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Player(Turtle):

	def __init__(self, position) -> None:
		super().__init__()
		self.speed("fastest")
		self.color("white")
		self.shapesize(1, 5, 1)
		self.setheading(90)
		self.shape("square")
		self.penup()
		self.goto(position)

	def move_up(self):
		self.forward(30)
	
	def move_down(self):
		self.backward(30)
	



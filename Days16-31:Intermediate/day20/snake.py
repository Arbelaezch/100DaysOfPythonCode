from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake(Turtle):

	def __init__(self) -> None:
		self.segments = []
		self.create_snake()
		self.head = self.segments[0]
		
		
	def create_snake(self):
		for position in STARTING_POSITIONS:
			self.add_segment(position)
	
	def move(self):
		for seg_num in range(len(self.segments) - 1, 0, -1):
			new_x = self.segments[seg_num - 1].xcor()
			new_y = self.segments[seg_num - 1].ycor()
			self.segments[seg_num].goto(new_x, new_y)
		self.head.forward(MOVE_DISTANCE)

	def turn_up(self):
		if self.head.heading() == 270:
			return
		self.head.setheading(90)
	
	
	def turn_down(self):
		if self.head.heading() == 90:
			return
		self.head.setheading(270)
	

	def turn_right(self):
		if self.head.heading() == 180:
			return
		self.head.setheading(0)

	def turn_left(self):
		if self.head.heading() == 0:
			return
		self.head.setheading(180)

	def add_segment(self, position):
		tim = Turtle("square")
		tim.color("white")
		tim.penup()
		tim.goto(position)
		self.segments.append(tim)

	def extend(self):
		self.add_segment(self.segments[-1].position())

		
from turtle import Turtle, position
import random

COLORS = ["red", "yellow", "blue", "purple", "green", "orange"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager(Turtle):

	def __init__(self):
		super().__init__()
		self.all_cars = []
		self.hideturtle()
		self.penup()
		self.car_speed = STARTING_MOVE_DISTANCE

	
	def create_cars(self):
		spawn = random.randint(1,6)
		if spawn == 1:
			new_car = Turtle("square")
			new_car.color(random.choice(COLORS))
			new_car.penup()
			new_car.shapesize(1, 2, 1)
			position = random.randint(-250, 250)
			new_car.goto((290, position))
			self.all_cars.append(new_car)
	

	def move_cars(self):
		'''Moves cars in constant stream. Also removes cars that are off the 
		screen, improving performance.'''
		for car in self.all_cars:
			car.backward(self.car_speed)
			if car.xcor() < -340:
				self.all_cars.pop(0)
	
	def stop_cars(self):
		for car in self.all_cars:
			car.backward(0)

	def level_up(self):
		self.car_speed += MOVE_INCREMENT



	
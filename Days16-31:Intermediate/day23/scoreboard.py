from turtle import Turtle
import random

FONT = ("Courier", 24, "normal")
DEAD = ["*squish*", "*crunch*"]

class Scoreboard(Turtle):
	
	def __init__(self) -> None:
		super().__init__()
		self.level = 1
		self.color("black")
		self.hideturtle()
		self.penup()
		self.goto((-200, 250))
		self.update_scoreboard()

	def update_scoreboard(self):
		self.write(f"Level: {self.level}", align="left", font=FONT)

	def game_over(self):
		self.goto(0,0)
		self.write(random.choice(DEAD), align="center", font=FONT)

	def increase_level(self):
		self.level += 1
		self.clear()
		self.update_scoreboard()
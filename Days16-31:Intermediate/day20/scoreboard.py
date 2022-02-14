from asyncore import read
from turtle import Turtle



class Scoreboard(Turtle):

	def __init__(self) -> None:
		super().__init__()
		self.score = 0
		self.color("white")
		self.hideturtle()
		self.penup()
		file = open("Days16-31:Intermediate/day20/high_score.txt")
		self.high_score = int(file.read())
		file.close()
		self.goto(0, 270)
		self.update_scoreboard()		

	def update_scoreboard(self):
		file = open("Days16-31:Intermediate/day20/high_score.txt")
		self.high_score = int(file.read())
		file.close()
		self.clear()
		self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))


	def reset(self):
		if self.score > self.high_score:
			self.high_score = self.score
			self.new_high = str(self.high_score)
			file = open("Days16-31:Intermediate/day20/high_score.txt", mode="w")

			file.write(self.new_high)
			file.close()

		self.score = 0
		self.update_scoreboard()
	# def game_over(self):
	# 	self.goto(0,0)
	# 	self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))

	def increase_score(self):
		self.score += 1
		self.clear()
		self.update_scoreboard()
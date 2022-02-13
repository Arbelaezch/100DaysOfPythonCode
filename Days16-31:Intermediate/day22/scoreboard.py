from turtle import Turtle

class Scoreboard(Turtle):

	def __init__(self, position) -> None:
		super().__init__()
		self.score = 0
		self.color("white")
		self.hideturtle()
		self.penup()
		self.goto(position)
		self.update_scoreboard()		


	def update_scoreboard(self):
		self.write(f"{self.score}", align="center", font=("Arial", 34, "normal"))

	# def game_over(self):
	# 	self.goto(0,0)
	# 	self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))

	def increase_score(self):
		self.score += 1
		self.clear()
		self.update_scoreboard()
		
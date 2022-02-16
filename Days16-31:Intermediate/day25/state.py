from turtle import Turtle

FONT = ("Courier", 12, "normal")


class State(Turtle):
    
    def __init__(self, state_name, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto((x, y))
        self.write(state_name, font=FONT)

	
        

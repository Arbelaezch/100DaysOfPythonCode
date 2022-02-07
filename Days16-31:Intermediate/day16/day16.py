import os
from turtle import Turtle, Screen
import os
from prettytable import PrettyTable



def screen_clear():
	'''Clears terminal screen'''
	if os.name == 'posix':
		_ = os.system('clear')
	else:
		# for windows platfrom
		_ = os.system('cls')



screen_clear()

x = PrettyTable()
x.field_names = ["Pokemon Name", "Type"]
x.add_row(["Pikachu", "Electric"])
x.add_row(["Squirtle", "Water"])
x.add_row(["Bulbasoar", "Grass"])
x.align = "l"

print(x)

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("DarkGreen")
# timmy.forward(100)
# print(timmy)
# my_screen = Screen()
# my_screen.exitonclick()









# Calculator
'''
For a better Implementation use Dictionaries where the key is the symbol: +,-,*,/ and the value is the 
word add, sub, mult, div. You can use this value to call the appropriate function. This removes the need
for if/elif statements.

'''

from ast import operator
from struct import calcsize
from turtle import rt


def calc_art():
	print(''' 
 _____________________
|  _________________  |
| | Calculator App  | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________| 
''')

def add(num1, num2):
	'''Adds two integers and returns result'''
	return num1+num2

def sub(num1, num2):
	'''Subtracts two integers and returns result'''
	return num1-num2

def mult(num1, num2):
	'''Multiplies two integers and returns result'''
	return num1*num2

def div(num1, num2):
	'''Divides two integers and returns result'''
	return num1/num2



def calculator():
	'''Calculator program'''

	calc_art()

	run = "y"

	num1 = float(input("What's the first number?: "))

	while run == "y":
		# Continues calculation if user desires
		op = input("+\n-\n*\n/\nPick an operation from the line above: ")
		# Loop ensures op is appropriate operator
		while not (op == "/" or op == "*" or op == "-" or op == "+"):
			op = input("Please pick an operation: ")

		num2 = float(input("What's the next number?: "))

		if op == "+":
			result = add(num1, num2)
		elif op == "-":
			result = sub(num1, num2)
		elif op == "*":
			result = mult(num1, num2)
		elif op == "/":
			result = div(num1, num2)
		else:
			print("How'd you do that??")
			exit()


		print(f"{num1} {op} {num2} = {result}")
		run = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: ")
		num1 = result

		# Loop ensures run is appropriate response
		while not (run == "n" or run == "y"):
			run = input(f"Please type 'y' to continue calculating with {result}, or 'n' to start a new calculation: ")
		
		if run == 'n':
			calculator()

calculator()





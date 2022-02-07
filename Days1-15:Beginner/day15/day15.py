# Virtual Coffee Machine


from menu import MENU, resources
from time import sleep
import os


def screen_clear():
	'''Clears terminal screen'''
	if os.name == 'posix':
		_ = os.system('clear')
	else:
		# for windows platfrom
		_ = os.system('cls')


def get_money(drink, resources):
	'''Receives and checks money, then dispenses change.
	Returns updated money resources dictionary or 0 if fail.'''
	print("Please insert coins.")
	p = 0
	q = 0
	d = 0
	n = 0


	q = int(input("How many quarters?: "))
	d = int(input("How many dimes?: "))
	n = int(input("How many nickles?: "))
	p = int(input("How many pennies?: "))

	money_deposited = (q*0.25)+(d*0.1)+(n*0.05)+(p*0.01)

	if money_deposited < MENU[drink]["cost"]:
		print("Sorry that's not enough money. Money refunded.")
		return 0
	else:
		resources["money"] += MENU[drink]["cost"]
		money_deposited -= MENU[drink]["cost"]
		money_deposited = round(money_deposited, 2)
		print(f"Here is ${money_deposited} in change.")
		return resources


def drink(resources, command):
	'''Checks that there are sufficient resources to brew coffee, then pours coffee.'''
	if resources["water"] >= MENU[command]["ingredients"]["water"] and resources["coffee"] >= MENU[command]["ingredients"]["coffee"] and resources["milk"] >= MENU[command]["ingredients"]["milk"]:
		money_check = get_money(command, resources)
		if not money_check == 0:
			print(f"Here is your {command}, enjoy!")
			resources["water"] -= MENU[command]["ingredients"]["water"]
			resources["coffee"] -= MENU[command]["ingredients"]["coffee"]
			resources["milk"] -= MENU[command]["ingredients"]["milk"]
			return resources
		else:
			return 0
	else:
		print("Sorry, not enough available resources.")
		return 0
			
		
		
money = 0

screen_clear()

while 1:
	command = input("What would you like? (espresso/latte/cappuccino): ")

	if command == "report":
		print("Water: " + str(resources["water"]) + ", Coffee: " + str(resources["coffee"]) + ", Milk: " + str(resources["water"]) + ", Money: $" + str(resources["money"]) + "\n")
	elif command == "espresso" or command == "latte" or command == "cappuccino":
		result = drink(resources, command)
		if not result == 0:
			resources = result
	else:
		print("Please input a valid command.")
		
			
		
#TODO: round money returned to 2 dec


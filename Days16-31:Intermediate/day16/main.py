# OOP Coffee Machine

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

def screen_clear():
	'''Clears terminal screen'''
	if os.name == 'posix':
		_ = os.system('clear')
	else:
		# for windows platfrom
		_ = os.system('cls')

money = MoneyMachine()
menu = Menu()
machine = CoffeeMaker()


screen_clear()
while 1:
	decision = input("What would you like?: ")

	if decision == "report":
		machine.report()
	else:
		drink = menu.find_drink(decision)
		if machine.is_resource_sufficient(drink):
			if money.make_payment(drink.cost):
				machine.make_coffee(drink)





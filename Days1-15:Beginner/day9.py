# Secret/Silent Auction Program
# Works as though each bidder was using the same computer/program to privately
# input their bid.
# Python Dictionaries and nesting

import random
import os
from time import sleep


def gavel_art():
	print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\ ''')


def screen_clear():
	# for mac and linux(here, os.name is 'posix')
	if os.name == 'posix':
		_ = os.system('clear')
	else:
		# for windows platfrom
		_ = os.system('cls')


run = "yes"
bidders_dict = {}



while run == "yes":
	screen_clear()
	print("Welcome to the secret auction program.")
	bidder = input("What is your name?: ")
	bidders_dict[bidder] = input("What's your bid?: $")
	

	run = input("Are there any other bidders? Type 'yes' or 'no'.\n")


	if not (run == "yes" or run == "no"):
		while not (run == "yes" or run == "no"):
			run = input("Please enter either 'yes' to enter more bidders or 'no' to end auction.\n")


	if run == "no":
		for key in bidders_dict:
			max_key = max(bidders_dict, key=bidders_dict.get)
			highest_bid = bidders_dict[max_key]
			print(f"{max_key} wins with a bid of ${highest_bid}.")
			exit()

		

	
	



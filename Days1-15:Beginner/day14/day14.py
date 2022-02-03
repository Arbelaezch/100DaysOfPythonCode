# Higher/Lower Game (Who Has More Followers?)
# I could have probably made this a little more efficient, but I designed it so 
# that the more popular combatant would stay as Combatant A until they were 
# dethroned by a more popular combatant B. This of course means that once you
# determine who the most popular combatant in the list is, they will always be 
# there and you can just collect points. So i decided to slightly change the code
# so that combatant B becomes combatant A after each round. This method would
# have been easier to implement and would have required more streamlined code, but
# I'm not going back to change it.

import random
from time import sleep
import os
from game_data import data

def logo_art():
	logo = """
	    __  ___       __             
	   / / / (_)___ _/ /_  ___  _____
	  / /_/ / / __ `/ __ \/ _ \/ ___/
	 / __  / / /_/ / / / /  __/ /    
	/_/ ///_/\__, /_/ /_/\___/_/     
	   / /  /____/_      _____  _____
	  / /   / __ \ | /| / / _ \/ ___/
	 / /___/ /_/ / |/ |/ /  __/ /    
	/_____/\____/|__/|__/\___/_/     
	"""
	print(logo)

def vs_art():
	vs = """
	 _    __    
	| |  / /____
	| | / / ___/
	| |/ (__  ) 
	|___/____(_)
	"""
	print(vs)

def screen_clear():
	'''Clears terminal screen'''
	if os.name == 'posix':
		_ = os.system('clear')
	else:
		# for windows platfrom
		_ = os.system('cls')

def select_combatant():
	combatant = data[random.randint(0, 49)]
	return combatant

def print_combatant(combatant, ab):
	if ab == 1:
		print("Compare A:", combatant["name"] + ", " + combatant["description"] 
		+ ", from " + combatant["country"] + ".")
	else:
		print("Against B:", combatant["name"] + ", " + combatant["description"] 
		+ ", from " + combatant["country"] + ".")

def winning_combatant(combatant1, combatant2):
	if combatant1["follower_count"] > combatant2["follower_count"]:
		return combatant1
	else:
		return combatant2


combatantA = {}
combatantB = {}
correct = 1
guess = ""
answer = {}
score = 0

screen_clear()

combatantA = select_combatant()

while correct == 1:
	logo_art()

	combatantB = select_combatant()
	while combatantA["name"] == combatantB["name"]:
		combatantB = select_combatant()

	print_combatant(combatantA, 1)
	vs_art()
	print_combatant(combatantB, 2)
	
	answer = winning_combatant(combatantA, combatantB)

	guess = input("Who has more followers? Type 'A' or 'B': ")
	if guess == "B" and combatantB["name"] == answer["name"]:
		combatantA = combatantB
		score += 1
		screen_clear()
		print(f"You're right! Current score: {score}.")
	elif guess == "A" and combatantA["name"] == answer["name"]:
		combatantA = combatantB
		score += 1
		screen_clear()
		print(f"You're right! Current score: {score}.")
	else:
		screen_clear()
		print(f"Sorry, that's wrong. Final score: {score}.")
		correct = 0
		exit()
	

		













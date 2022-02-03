# Blackjack Program

from audioop import add
import random
from tabnanny import check
from time import sleep
import os

def blackjack_art():
	'''Prints Blackjack ascii art to terminal'''
	print('''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/                 ''')


def screen_clear():
	'''Clears terminal screen'''
	if os.name == 'posix':
		_ = os.system('clear')
	else:
		# for windows platfrom
		_ = os.system('cls')


def remove_from_deck(deck, index):
	'''Removes drawn card from the deck'''
	deck[index] = 0
	return deck


def draw_card(deck):
	'''Draws a single cards from the deck and returns the card drawn.'''
	card = 1
	index = random.randint(0,51)
	card = deck[index]
	while card == 0:
		index = random.randint(0,51)
		card = deck[index]
	remove_from_deck(deck, index)
	return card

def repair_deck(deck):
	'''Re-fills the deck'''
	deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 
8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q",
"K", "K", "K", "K", "A", "A", "A", "A"]
	return deck

def game_setup(deck):
	'''Draws two cards for the player and one for the dealer.'''
	player_hand.append(draw_card(deck))
	player_hand.append(draw_card(deck))
	dealer_hand.append(draw_card(deck))


def add_hand(cards_dict, hand):
	'''Adds up total of cards from given hand.'''
	total = 0
	for cards in range(0, len(hand)):
		total += cards_dict[hand[cards]]
	
	#Checks if hand has any Aces and is over 21, setting the total to 10 less per Ace.
	if ("A" in hand) and (total > 21):
		total -= hand.count("A")*10

	return total


def check_hand(total, game_over):
	'''Checks that the player's hand is not 21 or greater.'''
	if total == 21:
		print("You got 21, you win!")
		game_over = "y"
		return game_over
	elif total > 21:
		print(f"You bust with {total}, dealer wins.")
		game_over = "y"
		return game_over
	else:
		return "n"
	


	




cards_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "J": 10, "Q": 10, "K": 10, "A": 11}

deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 
8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q",
"K", "K", "K", "K", "A", "A", "A", "A"]


continue_game = "y"
player_hand = []
dealer_hand = []
hit_me = ""
game_over = "n"

screen_clear()
blackjack_art()

while continue_game == "y":
	game_setup(deck)
	print("Your cards:", player_hand)
	print("Your Total: ", add_hand(cards_dict, player_hand))
	print("Dealer's first card:", dealer_hand)
	check_hand(add_hand(cards_dict, player_hand), game_over)

	hit_me = input("Type 'y' to get another card, type 'n' to pass: ")

	while hit_me == "y":
		game_over = "n"
		player_hand.append(draw_card(deck))
		game_over = check_hand(add_hand(cards_dict, player_hand), game_over)
		if game_over == "y":
			hit_me = "n"
		else:
			print("Your cards:", player_hand)
			print(add_hand(cards_dict, player_hand))
			hit_me = input("Type 'y' to get another card, type 'n' to pass: ")
	
	hit_me = "y"

	while (hit_me == "y") and (game_over == "n"):
		player_total = add_hand(cards_dict, player_hand)
		dealer_hand.append(draw_card(deck))
		total = add_hand(cards_dict, dealer_hand)
		print("Dealer's cards:", dealer_hand)
		print(add_hand(cards_dict, dealer_hand))
		if total > 21:
			print("Dealer busts, you win!")
			game_over = "y"
		elif (total == 21) and (player_total == 21):
			print("Dealer has 21, tie.")
			game_over = "y"
		elif total == 21:
			print("Dealer has 21, you lose.")
			game_over = "y"
		elif total > player_total:
			print(f"Dealer has {total}, you lose.")
			game_over = "y"


	continue_game = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
	repair_deck(deck)
	player_hand = []
	dealer_hand = []
	hit_me = ""
	game_over = "n"





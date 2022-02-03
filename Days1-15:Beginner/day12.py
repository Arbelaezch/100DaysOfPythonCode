# Number Guessing Game
# Scope

import random



play_again = "y"


while play_again == "y":
	number = random.randint(1, 100)
	print(number)
	attempts = 5
	win = 0


	print("Welcome to the Number Guessing Game!")
	print("I'm thinking of a number between 1 and 100.")
	difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
	if difficulty == "easy":
		attempts = 10
	elif difficulty == "hard":
		attempts = 5
	else:
		print("You dun goofed.")
		exit()


	while attempts > 0:
		if attempts > 1:
			print(f"You have {attempts} attempts remaining to guess the number")
		else:
			print(f"You have {attempts} attempt remaining to guess the number")
		guess = int(input("Make a guess: "))
		print("")
		if guess == number:
			win = 1
			print(f"You win! The number was {guess}.")
			play_again = input("Type 'y' to play again or 'n' to exit: ")
			attempts = 0
		elif guess > number:
			print("Too high.")
			attempts -= 1
			print("Guess again.")
		elif guess < number:
			print("Too low.")
			attempts -= 1
			print("Guess again.")
		
		
	
	if not win == 1:
		print("You have run out of guesses. You lose.")
		play_again = input("Type 'y' to play again or 'n' to exit: ")








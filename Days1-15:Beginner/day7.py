# Hangman

from gettext import find
import os
from time import sleep
import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
   # print out some text

def game_over(deaths, word):
	screen_clear()
	if deaths == 6:
		print(f"You lose. The word was {word}.")
		print(HANGMANPICS[6])
	else:
		print(word)
		print("You win! Good job :)")
		print(HANGMANPICS[deaths])

	quit()

word = words[random.randint(0,64)]
length = len(word)
isPlaying = True
deaths = 0
uncovered = "-"*length
uncovered_list = list(uncovered)
new_uncovered = "".join(uncovered_list)
position = 0



screen_clear()
print(word)
word_list = list(word)
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')

letter = input("Guess a letter: ")


while isPlaying:
	screen_clear()
	position = 0
	

	if letter in word:
		
		position = word.find(letter, position, length-1)
		uncovered_list[position] = letter

		while not (position == -1):
			position += 1
			position = word.find(letter, position, length-1)
			if not position == -1:
				uncovered_list[position] = letter
		
		new_uncovered = "".join(uncovered_list)
		print(new_uncovered)
		print(f"You guessed the letter {letter}.")


	else:
		print(new_uncovered)
		print(f"You guessed {letter}, that's not in the word. You lose a life")
		deaths += 1
		if deaths == 6:
			isPlaying = False
			game_over(deaths, word)
	

	if new_uncovered.find("-") == -1:
		game_over(deaths, word)
	else:
		print(HANGMANPICS[deaths])
		letter = input("Guess a letter: ")







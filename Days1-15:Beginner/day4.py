# Rock Paper Scissors

import random


print("Welcome to Rock, Paper, Scissors!")
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
random_int = random.randint(0,2)

if choice < 0 or choice > 2:
    print('You dun goofed. Try typing either "0", "1", or "2".')
    exit()


hand = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

row1 = ['Tie', 'You Win', 'You Lose']
row2 = ['You Lose', 'Tie', 'You Win']
row3 = ['You Win', 'You Lose', 'Tie']
rps = [row1, row2, row3]


print(hand[choice])
print(f"Computer chose: {random_int}")
print(hand[random_int])

print(rps[random_int][choice])
print("-")












print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".')

if choice1 == "left":
	choice2 = input('You come to a lake, what do you want to do? Type "swim" or "wait".')
	if choice2 == "wait":
		choice3 = input('After a few hours, three different colored, free-standing doors manifest in front of you. Do you go through the "blue", "red", or "yellow" door?')
		if choice3 == "yellow":
			print("You found the treasure, you win!")
		elif choice3 == "red":
			print("You grab the red handle and it feels warm to the touch. You walk through the door into a room engulfed in flame. Unfortunately, the door behind you is now gone and you are trapped. You spend your final minutes contemplating why you walked through the door when you could clearly see there was fire on the other side.\nGame Over.")
		else:
			print("You walk through the blue door and find a shark-man twice your size standing upright before you wearing a lab coat and spectacles. It is hunched over examining something through a microscope and has yet to notice your presense. Behind it is a large board with formulas and drawings all over it. As you approach it you accidentally step on and crush a glass vial that was carelessly left on the floor. The resulting crack of the glass alerts the shark-man to your presense who turns out of shock. In his eyes you see curiosity, fear, and intrigue. You imagine you must be giving a similar response. You begin to speak when the shark man lurches forward and eats you whole.\nGame Over.")
	else:
		print("You decide to swim across the lake even though you cannot see the other side. After hours of swimming in the same direction without getting tired you finally see land ahead. Alas, before you reach the shore a shark wakes from its mid-day siesta and eats you as a post-nap snack.\nGame Over.")
else:
	print("You encounter a pack of wolves that had a bad day at work so they choose to eat you.\nGame over")




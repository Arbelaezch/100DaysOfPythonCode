# Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #0-51
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] #0-8

print("Welcome to the PyPassword Generator")
length = int(input("How many letters would you like in your password?\n"))
num_of_symbols = int(input("How many symbols would you like?\n"))
num_of_nums = int(input("How many numbers would you like?\n"))


if num_of_nums + num_of_symbols > length:
	print("You have too many numbers and symbols for your password length. Try again.")
	exit()

password = []

if num_of_symbols > 0:
	for n in range(0,num_of_symbols):
		index = random.randint(0, 8)
		password.append(symbols[index])

if num_of_nums > 0:
	for n in range(0,num_of_nums):
		index = random.randint(0, 9)
		password.append(numbers[index])

for n in range(0,length-(num_of_symbols+num_of_nums)):
	index = random.randint(0, 51)
	password.append(letters[index])

random.shuffle(password)

password_string = ""
for n in range(0,len(password)):
	password_string += str(password[n])


print(f"Here is your password: {password_string}")
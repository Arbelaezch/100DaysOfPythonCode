# Caesar Cipher

from email import message
from gettext import find
from turtle import pensize


def art():
	print('''
░█████╗░░█████╗░███████╗░██████╗░█████╗░██████╗░  ░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗  ██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░╚█████╗░███████║██████╔╝  ██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══██║██╔══██╗  ██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗██████╔╝██║░░██║██║░░██║  ╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
''')

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = "abcdefghijklmnopqrstuvwxyz"
run = "yes"


art()

def caesar(alphabet, type):
	message = input('Type your message:\n')
	message_list = list(message)

	shift = int(input("Type the shift number:\n"))
	
	for i in range(0, len(message_list)):
		if message_list[i] in alphabet_list:
			letter = str(message_list[i])
			position = int(alphabet.find(letter))
			if type == "encode":
				new_position = position + shift
				if new_position > 25:
					new_position -= 26
			else:
				new_position = position - shift
				if new_position < 0:
					new_position += 26
			message_list[i] = alphabet[new_position]

	encoded = "".join(message_list)
	return encoded




while run == "yes":
	type = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

	if type == "encode" or type == "decode":
		result = caesar(alphabet, type)
		print(f"Here's the encoded result: {result}")
		run = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")
	else:
		print("Try again.")














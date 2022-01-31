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

def encode1(alphabet):
	message = input('Type your message:\n')
	message_list = list(message)

	shift = int(input("Type the shift number:\n"))
	
	for i in range(0, len(message_list)):
		letter = str(message_list[i])
		position = int(alphabet.find(letter))
		new_position = position + shift
		if new_position > 25:
			new_position -= 26
		message_list[i] = alphabet[new_position]

	encoded = "".join(message_list)
	return encoded


def decode1(alphabet):
	message = input('Type your message:\n')
	message_list = list(message)

	shift = int(input("Type the shift number:\n"))
	
	for i in range(0, len(message_list)):
		letter = str(message_list[i])
		position = int(alphabet.find(letter))
		new_position = position - shift
		if new_position < 0:
			new_position += 26
		message_list[i] = alphabet[new_position]

	decoded = "".join(message_list)
	return decoded





while run == "yes":
	encode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

	if encode == "encode":
		encoded_result = encode1(alphabet)
		print(f"Here's the encoded result: {encoded_result}")
	else:
		decoded_result = decode1(alphabet)
		print(f"Here's the decoded result: {decoded_result}")

	run = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")











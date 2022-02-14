# Mail Merge Project
# Takes names from one file, then inserts each name into an email, and
# saves each version of the email.

with open("Days16-31:Intermediate/day24/Input/names/invited_names.txt") as name_file:
	names = name_file.readlines()

	i = 0
	for i in range(0, len(names)):
		names[i] = names[i].strip("\n")


with open("Days16-31:Intermediate/day24/Input/Letters/starting_letter.txt") as letter_file:
	letter = letter_file.read()

	for name in names:
		new_letter = letter.replace("[name]", name)
		f = open("Days16-31:Intermediate/day24/Output/ReadyToSend/"+ name + ".txt", "w")
		f.write(new_letter)
		f.close()




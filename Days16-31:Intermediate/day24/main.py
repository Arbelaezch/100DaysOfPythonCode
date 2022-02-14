# Open and close a file to read/write/append its content
file = open("Days16-31:Intermediate/day24/my_file.txt")
content = file.read()
print(content)

# Can open a file under pseudonym and for a specific set of actions. Closes automatically.
with open("Days16-31:Intermediate/day24/my_file.txt", mode="a") as file:
	file.write("\ntest")
	print(file)




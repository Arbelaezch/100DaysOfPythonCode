# List Comprehension
# item is what is placed in the new list, item is each item in list, list is the original list, and test is the conditional for if item is added to new_list.
test = 1
new_list = [item for item in list if test]

# Dictionary Comprehension
new_dict = {new_key:new_value for (key,value) in dict.items() if test}

# Adds 1 to each number in list, adds results to new list.
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]

# Puts each letter from string into a list.
name = "Angela"
letters_list = [letter for letter in name]

# Iterates through 1, 2, 3, 4 and multiplies each by 2.
range_list = [num*2 for num in range(1, 5)]

# Conditional List Comprehension: returns names less than 5 characters, also 
# uppercases names.
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name.upper() for name in names if len(name) < 5]

# Squares the numbers in a list.
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number*number for number in numbers]

# Put the numbers that appear in both files into the results list.
with open("file1.txt") as f1:
    f1_data = f1.readlines()
with open("file2.txt") as f2:
    f2_data = f2.readlines()
result = [int(num) for num in f1_data if num in f2_data]


# Creates a dictionary where the key is the word of the string, and the value
# is the length of the word.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split(" ")}


# Looping through Panda DataFrames
import pandas
student_dict = {
	"student": ["Angela", "James", "Lily"],
	"score": [56, 76, 98]
}
student_data_frame = pandas.DataFrame(student_dict)

# Looping through dictionaries:
for (key, value) in student_data_frame.items():
    print(key)
# Loops through rows of a data frame, returns scalar value
for(index, row) in student_data_frame.iterrows():
    print(row.student)








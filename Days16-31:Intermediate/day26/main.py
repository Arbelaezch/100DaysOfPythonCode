import pandas

# nato_dict = {"A": "Alfa", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliett", "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee", "Z": "Zulu"}

data = pandas.read_csv(
    "Days16-31:Intermediate/day26/nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ")

    try:
        new_list = [nato_dict[letter] for letter in word.upper()]
    except KeyError:
        print("Sorry, only letters in the alphabet.")
        generate_phonetic()
    else:
        print(new_list)


generate_phonetic()

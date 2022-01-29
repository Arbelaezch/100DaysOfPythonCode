# Tip Calculator program

print("Welcome to the tip calculator.")
total = float(input("What was the total bill?\n$"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
num_of_people = int(input("How many people split the bill?\n"))



total += (total*(tip_percent/100))
cost_per_person = total/num_of_people
final_amount = "{:.2f}".format(cost_per_person) # Rounds number to 2 decimal places


print(f"Each person should pay: ${final_amount}")

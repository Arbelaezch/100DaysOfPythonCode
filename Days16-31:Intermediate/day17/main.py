# OOP Quiz

import os
from re import T
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def screen_clear():
	'''Clears terminal screen'''
	if os.name == 'posix':
		_ = os.system('clear')
	else:
		# for windows platfrom
		_ = os.system('cls')
  

question_bank = []
screen_clear()
i = 0

for q in question_data:
	question = Question(question_data[i]["text"], question_data[i]["answer"])
	question_bank.append(question)
	i += 1

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
	quiz.next_question()

print(f"You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")
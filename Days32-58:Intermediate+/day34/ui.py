from cgitb import text
from tkinter import *
from numpy import pad
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

	def __init__(self, quiz_brain: QuizBrain) -> None:
		self.quiz = quiz_brain
		self.window = Tk()
		self.window.title("Quizzler")
		self.window.config(bg=THEME_COLOR)
		self.score_int = 0

		self.score_label = Label(text="This is old text", padx=20, pady=20, bg=THEME_COLOR)
		self.score_label.config(text=f"Score: {self.score_int}")
		self.score_label.grid(column=1, row=0)

		self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
		self.canvas.grid(column=0, row=1, columnspan=2, padx=20)
		self.question_text = self.canvas.create_text(
			150, 125, text="This is the question", fill=THEME_COLOR, font=("arial", 20, "italic"), width=280)

		true_img = PhotoImage(file="Days32-58:Intermediate+/day34/images/true.png")
		self.true_btn = Button(image=true_img, highlightthickness=0,
				highlightbackground=THEME_COLOR, command=self.true_pressed)
		self.true_btn.grid(column=0, row=2, padx=20, pady=20)

		false_img = PhotoImage(file="Days32-58:Intermediate+/day34/images/false.png")
		self.false_btn = Button(image=false_img, highlightthickness=0,
				highlightbackground=THEME_COLOR, command=self.false_pressed)
		self.false_btn.grid(column=1, row=2, padx=20, pady=20)
  
		self.get_next_question()

		self.window.mainloop()
   
	def get_next_question(self):
		if self.quiz.still_has_questions():
			self.canvas.config(bg="white")
			q_text = self.quiz.next_question()
			self.canvas.itemconfig(self.question_text, text=q_text)
		else:
			self.canvas.itemconfig(self.question_text, text=f"You reached the end of the quiz. You scored {self.score_int}")

	def true_pressed(self):
		is_right = self.quiz.check_answer("True")
		print(is_right)
		self.give_feedback(is_right)

	def false_pressed(self):
		is_wrong = self.quiz.check_answer("False")
		self.give_feedback(is_wrong)

  
	def give_feedback(self, is_right):
		if is_right:
			self.canvas.config(bg="green")
			self.score_int += 1
			self.score_label.config(text=f"Score: {self.score_int}")
		else:
			self.canvas.config(bg="red")
		self.window.after(1000, self.get_next_question())
		


		




	

	

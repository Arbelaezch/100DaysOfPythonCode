# Flashcard app for learning words of a language. Card flips after 3 seconds.
# If user got the card correct, it removes it from the deck, otherwise it stays
# in rotation.

from cgitb import text
from tkinter import *
from tkinter import font
from tkinter import messagebox
import math
from turtle import color
import pyperclip
import json
import pandas as pd
import random


# ---------------------------- DATA DICT ------------------------------- #

data = pd.read_csv("Days16-31:Intermediate/day31/data/french_words.csv")
data_dict = data.to_dict(orient="records")

# ---------------------------- CARD HANDLING ------------------------------- #

# Displays new word.
def next_card():
    canvas.itemconfig(canvas_image, image=card_front_img)
    word_list = [item["French"] for item in data_dict]
    word = random.choice(word_list)
    canvas.itemconfig(french_word, text=word, fill="black")
    canvas.itemconfig(canvas_language, text="French", fill="black")
    window.after(3000, func=flip_card)
    wrong_button.config(state="disabled")
    right_button.config(state="disabled")


# Removes completed word from dictionary and calls next word.
def correct():
    word = canvas.itemcget(french_word, 'text')
    data_dict[:] = [d for d in data_dict if d['English'] != word]
    if len(data_dict) > 0:
        next_card()
    else:
        canvas.itemconfig(french_word, text="Good job!")
        wrong_button.config(state="disabled")
        right_button.config(state="disabled")


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    word = canvas.itemcget(french_word, 'text')
    english_word = [item["English"]
                    for item in data_dict if item["French"] == word]
    canvas.itemconfig(french_word, text=english_word, fill="white")
    canvas.itemconfig(canvas_language, text="English", fill="white")
    wrong_button.config(state="normal")
    right_button.config(state="normal")


BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# Image
canvas = Canvas(width=800, height=526,
                highlightthickness=0, bg=BACKGROUND_COLOR)
card_back_img = PhotoImage(
    file="Days16-31:Intermediate/day31/images/card_back.png")
card_front_img = PhotoImage(
    file="Days16-31:Intermediate/day31/images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)
canvas_language = canvas.create_text(
    400, 150, text="French", font=("Ariel", 40, "italic"), fill="black")
french_word = canvas.create_text(
    400, 263, text="word", font=("Ariel", 60, "bold"), fill="black")


# Button
wrong_img = PhotoImage(file="Days16-31:Intermediate/day31/images/wrong.png")
right_img = PhotoImage(file="Days16-31:Intermediate/day31/images/right.png")

wrong_button = Button(image=wrong_img, highlightthickness=0,
                      highlightbackground=BACKGROUND_COLOR, command=next_card, state="disabled")
wrong_button.grid(column=0, row=1)
right_button = Button(image=right_img, highlightthickness=0,
                      highlightbackground=BACKGROUND_COLOR, command=correct, state="disabled")
right_button.grid(column=1, row=1)


canvas.itemconfig(french_word, text=next_card())


window.mainloop()

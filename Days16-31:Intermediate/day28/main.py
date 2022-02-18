from tkinter import *
from tkinter import font
from turtle import color
import math

from matplotlib import image
from matplotlib.pyplot import text

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_count():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_count():
    count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
    	window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# LABELS:
# Header
header = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 50, "bold"), fg=GREEN)
# header.config(text="Timer")
header.grid(column=1, row=0)

# Checkmarks
checkmarks = Label(text="✔", bg=YELLOW, fg=GREEN)
checkmarks.grid(column=1, row=3)

# Tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Days16-31:Intermediate/day28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# Buttons
start_btn = Button(text="Start", highlightthickness=0, bg=YELLOW, highlightbackground=YELLOW, command=start_count)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, highlightbackground=YELLOW, command=reset_count)
reset_btn.grid(column=2, row=2)












window.mainloop()
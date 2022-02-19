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
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1

round = [WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN,
         WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, LONG_BREAK_MIN]

reps = 0
checks = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_count():
    global checks, reps
    
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    header.config(text="Timer", bg=YELLOW, font=(FONT_NAME, 50, "bold"), fg=GREEN)
    checks = 0
    checkmarks.config(text="✔"*checks, bg=YELLOW, fg=GREEN)
    reps = 0
    start_btn["state"]= "normal"

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_count():
    start_btn.config(state="disabled")
    global reps, checks
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        header.config(text="Break", fg=RED)
        checks += 1
        checkmarks.config(text="✔"*checks, bg=YELLOW, fg=GREEN)
        reps = 0
        count_down(long_break_sec)
    elif reps % 2 == 0:
        header.config(text="Break", fg=PINK)
        checks += 1
        checkmarks.config(text="✔"*checks, bg=YELLOW, fg=GREEN)
        count_down(short_break_sec)
    else:
        header.config(text="WORK", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_count()

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
checkmarks = Label(text="", bg=YELLOW, fg=GREEN)
checkmarks.grid(column=1, row=3)

# Tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Days16-31:Intermediate/day28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# Buttons
start_btn = Button(text="Start", highlightthickness=0, bg=YELLOW,
                   highlightbackground=YELLOW, command=start_count)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0,
                   highlightbackground=YELLOW, command=reset_count)
reset_btn.grid(column=2, row=2)


window.mainloop()

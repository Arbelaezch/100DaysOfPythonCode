# Password Manager
# Saves username/password for websites, as well as generates random passwords
# and copies them to clipboard for easy use.


from tkinter import *
from tkinter import font
from tkinter import messagebox
import math
from password_generator import generate_password
import pyperclip


FONT = ("Courier", 50, "bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    pass_entry.delete(0, 'end')
    password_string = generate_password()
    pass_entry.insert(0, password_string)
    pyperclip.copy(password_string)
    
    

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or (email) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message=f"Please don't leave any fields empty!")
    else:
        entry = f"{website} | {email} | {password}\n"

        is_okay = messagebox.askokcancel(
            title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it okay to save?")

        if is_okay:
            f = open("Days16-31:Intermediate/day29/data.txt", "a")
            f.write(entry)
            f.close()

            clear_setup()


# ---------------------------- UI SETUP ------------------------------- #

def clear_setup():
    website_entry.delete(0, 'end')
    pass_entry.delete(0, 'end')
    website_entry.focus()


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# Image
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="Days16-31:Intermediate/day29/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "arbelaezch@gmail.com")
pass_entry = Entry(width=20)
pass_entry.grid(column=1, row=3)

# Button
generate_pass_button = Button(
    text="Generate Password", width=11, command=generate)
generate_pass_button.grid(column=2, row=3)
save_pass_button = Button(text="Add", width=33, command=save_password)
save_pass_button.grid(column=1, row=5, columnspan=2)


window.mainloop()

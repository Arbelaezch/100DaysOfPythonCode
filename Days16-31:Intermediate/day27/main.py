from tkinter import *

def convert():
    a = float(entry.get())*1.609
    answer.config(text=a)
    

#Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)

#Labels

label = Label(text="This is old text")
label.config(text="is equal to")
label.grid(column=0, row=1)
answer = Label(text=" ")
answer.grid(column=1, row=1)

miles = Label(text="Miles")
miles.grid(column=2, row=0)
km = Label(text="Km")
km.grid(column=2, row=1)

#calls action() when pressed
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

#Entries
entry = Entry(width=10)
#Add some text to begin with
entry.insert(END, string="")
entry.grid(column=1, row=0)









# Keep this at the end of your code
window.mainloop()

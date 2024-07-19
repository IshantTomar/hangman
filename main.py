import random
from customtkinter import *
from words import words
app = CTk()
app.title("Hangman")

word = random.choice(words).upper()

wordvar = StringVar()
guess_en_var = StringVar()


def check_input():
    user_input = guess_en_var.get()
    if len(user_input) > 1:
        guess_en_check.configure(text="Please enter only 1 character.")
        guess_en.delete(1, END)
    elif user_input.isdigit():
        guess_en_check.configure(text="Please only enter alphabets.")
        guess_en.delete(0)
    app.after(500, check_input)


wordlabel = CTkLabel(app, textvariable=wordvar)
wordlabel.grid(row=0, column=0)
guesslabel = CTkLabel(app, text="Guess: ")
guesslabel.grid(row=1, column=0)
guess_en = CTkEntry(app, textvariable=guess_en_var, width=30)
guess_en.grid(row=1, column=1, sticky="w")
guess_en_check = CTkLabel(app, text="", justify=LEFT)
guess_en_check.grid(row=2, column=1)

check_input()
app.mainloop()

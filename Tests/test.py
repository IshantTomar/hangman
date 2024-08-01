import random
from customtkinter import *

# Ensure words.py exists with a list of words
i = ["mine"]

app = CTk()
app.title("Hangman")
set_appearance_mode("dark")

# Global variables
word = random.choice(i).upper()
right_guess = ""
wrong_guess = 0
chance = 6
guessedvar = StringVar()
wordvar = StringVar()
guess_en_var = StringVar()


def game():
    global right_guess, chance
    display_word = ""

    user_input = guess_en_var.get().upper()
    guess_en_var.set("")  # Clear the entry after reading

    if len(user_input) != 1 or not user_input.isalpha():
        alreadylabel.configure(text="Invalid input")
        return

    if user_input in word:
        if user_input not in right_guess:
            right_guess += user_input
            alreadylabel.configure(text="Correct guess")
        else:
            alreadylabel.configure(text="You have already guessed it!")
    else:
        alreadylabel.configure(text="Wrong")
        chance -= 1

    for char in word:
        if char in right_guess:
            display_word += char + " "
        else:
            display_word += "_ "

    wordlabel.configure(text=display_word)

    if chance == 0:
        guessedlabel.configure(text=f"You lost! The word was {word}")

    if all(char in right_guess for char in word):
        guessedlabel.configure(text="You guessed it!")


def check_input():
    user_input = guess_en_var.get()
    if len(user_input) > 1:
        guess_en_check.configure(text="Please enter only 1 character.", text_color="red")
    elif user_input.isdigit():
        guess_en_check.configure(text="Please only enter alphabets.", text_color="red")
    else:
        guess_en_check.configure(text="")

    app.after(500, check_input)


def reset_game():
    global word, right_guess, wrong_guess, chance
    word = random.choice(i).upper()
    right_guess = ""
    wrong_guess = 0
    chance = 6
    wordlabel.configure(text="_ " * len(word))
    guessedlabel.configure(text="")
    alreadylabel.configure(text="")
    guess_en_var.set("")


wordlabel = CTkLabel(app, text="_ " * len(word), font=("Arial", 50))
wordlabel.grid(row=0, column=0, columnspan=3)
guessedlabel = CTkLabel(app, text="", font=("Arial", 50))
guessedlabel.grid(row=1, column=0, columnspan=3)
guesslabel = CTkLabel(app, text="Guess: ", font=("Arial", 30))
guesslabel.grid(row=2, column=0)
guess_en = CTkEntry(app, textvariable=guess_en_var, width=40, font=("Arial", 30))
guess_en.grid(row=2, column=1, sticky="w")
alreadylabel = CTkLabel(app, text="", font=("Arial", 20))
alreadylabel.grid(row=2, column=2, sticky="w")
guess_en_check = CTkLabel(app, text="", justify=LEFT)
guess_en_check.grid(row=3, column=1)
guessbutton = CTkButton(app, text="Guess", font=("Arial", 15), width=40, command=game)
guessbutton.grid(row=4, column=1, sticky="w")

resetbutton = CTkButton(app, text="Reset", font=("Arial", 15), width=40, command=reset_game)
resetbutton.grid(row=6, columnspan=2)

check_input()
app.mainloop()

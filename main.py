import random
from customtkinter import *
from PIL import Image
from words import words
from hangmandesign import *

app = CTk()
app.title("Hangman")
set_appearance_mode("dark")

i = ["mine"]
word = random.choice(i).upper()
right_guess = ""
wrong_guess = 0
chance = 0
guessedvar = StringVar()
wordvar = StringVar()
guess_en_var = StringVar()

def game():
    global right_guess, chance, wrong_guess
    update_wordlabel = ""
    w = 0

    user_input = guess_en_var.get().upper()

    if user_input in word:
        if user_input not in right_guess:
            right_guess += user_input
            guess_en_check.configure(text="Correct guess!", text_color="lightblue")
            guess_en.delete(0)
        else:
            guess_en_check.configure(text="You have already guessed it!", text_color="white")
            guess_en.delete(0)
    else:
        guess_en_check.configure(text="Wrong guess.", text_color="white")
        guess_en.delete(0)
        wrong_guess += 1

    for char in word:
        if char in right_guess:
            update_wordlabel += char + " "
        else:
            update_wordlabel += "_ "
            w += 1
    wordlabel.configure(text=update_wordlabel)

    image_update()

    if w == 0:
        guessedlabel.configure(text="You guessed it!", text_color="lightblue")
        chance_label.configure(text="")
        image_label.configure(image=image0)

def image_update():
    a = wrong_guess
    b = a - 6
    chances = "You have " + str(abs(b)) + " chances left"
    if wrong_guess == 1:
        image_label.configure(image=image1)
        chance_label.configure(text=chances)
    elif wrong_guess == 2:
        image_label.configure(image=image2)
        chance_label.configure(text=chances)
    elif wrong_guess == 3:
        image_label.configure(image=image3)
        chance_label.configure(text=chances)
    elif wrong_guess == 4:
        image_label.configure(image=image4)
        chance_label.configure(text=chances)
    elif wrong_guess == 5:
        image_label.configure(image=image5)
        chance_label.configure(text=chances)
    elif wrong_guess == 6:
        image_label.configure(image=image6)
        chance_label.configure(text=chances)

def check_input():
    user_input = guess_en_var.get()
    if len(user_input) > 1:
        guess_en_check.configure(text="Please enter only 1 character.", text_color="red")
        guess_en.delete(1, END)
    elif user_input.isdigit():
        guess_en_check.configure(text="Please only enter alphabets.", text_color="red")
        guess_en.delete(0)
    app.after(500, check_input)

wordlabel = CTkLabel(app, text="_ " * len(word), font=("Arial", 50))
wordlabel.grid(row=0, columnspan=2)
guessedlabel = CTkLabel(app, text="", font=("Arial", 20))
guessedlabel.grid(row=1, columnspan=2)
guesslabel = CTkLabel(app, text="Guess: ", font=("Arial", 30))
guesslabel.grid(row=3, column=0)
guess_en = CTkEntry(app, textvariable=guess_en_var, width=40, font=("Arial", 20))
guess_en.grid(row=3, column=1, pady=10, sticky="w")
app.bind("<Return>", lambda event: game())
alreadylabel = CTkLabel(app, text="", font=("Arial", 20))
alreadylabel.grid(row=2, column=3, sticky="w")
guess_en_check = CTkLabel(app, text="", justify=LEFT)
guess_en_check.grid(row=4, column=1)
guessbutton = CTkButton(app, text="Guess", font=("Arial", 15), width=40, command=game)
guessbutton.grid(row=5, columnspan=2, pady=5)
chance_label = CTkLabel(app, text="", font=("Arial", 15), text_color="red")
chance_label.grid(row=6, columnspan=2)
image_label = CTkLabel(app, text="", image=image0)
image_label.grid(row=7, columnspan=2, pady=10)
resetbutton = CTkButton(app, text="Reset", font=("Arial", 15), width=40)
resetbutton.grid(row=8, columnspan=2)
check_input()
app.mainloop()

import random
from customtkinter import *
from PIL import Image
from words import *

def center_window(window, width, height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y coordinates to position the window in the center
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Set the window size and position
    window.geometry(f"{width}x{height}+{x}+{y}")

app = CTk()
app.title("Hangman")
set_appearance_mode("dark")
center_window(app, 300, 680)
# Need Icon to make icon

hint = random.choice(category)
hint_name = variable_name(hint)
word = random.choice(hint).upper()
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
        guess_en_check.configure(text="")
        chance_label.configure(text="Well done!", text_color="lightblue")

def image_update():
    a = wrong_guess
    b = a - 6
    chances = "You have " + str(abs(b)) + " chances left"
    word_text = "The word was " + word + "."
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
        chance_label.configure(text="Game Over.", text_color="red")
        guessedlabel.configure(text=word_text, text_color="white")

image0 = CTkImage(light_image=Image.open('stickman/0.png'), size=(188,256))
image1 = CTkImage(light_image=Image.open('stickman/1.png'), size=(188,256))
image2 = CTkImage(light_image=Image.open('stickman/2.png'), size=(188,256))
image3 = CTkImage(light_image=Image.open('stickman/3.png'), size=(188,256))
image4 = CTkImage(light_image=Image.open('stickman/4.png'), size=(188,256))
image5 = CTkImage(light_image=Image.open('stickman/5.png'), size=(188,256))
image6 = CTkImage(light_image=Image.open('stickman/6.png'), size=(188,256))

def check_input():
    user_input = guess_en_var.get()
    if len(user_input) > 1:
        guess_en_check.configure(text="Please enter only 1 character.", text_color="red")
        guess_en.delete(1, END)
    elif user_input.isdigit():
        guess_en_check.configure(text="Please only enter alphabets.", text_color="red")
        guess_en.delete(0)
    app.after(500, check_input)

def reset_game():
    global hint, hint_name, word, right_guess, wrong_guess, chance
    hint = random.choice(category)
    hint_name = variable_name(hint)
    word = random.choice(hint).upper()
    right_guess = ""
    wrong_guess = 0
    chance = 0
    hintlabel.configure(text=hint_name)
    wordlabel.configure(text="_ " * len(word))
    alreadylabel.configure(text="", text_color="white")
    chance_label.configure(text="", text_color="red")
    image_label.configure(image=image0)
    guessedlabel.configure(text="", text_color="white")
    guess_en_var.set("")
    guess_en_check.configure(text="")

# Create a frame to hold the hint label and center it
border_frame = CTkFrame(app, border_width=2, border_color="white")
border_frame.grid(row=0, column=0, columnspan=2, pady=20, padx=10)

hintlabel = CTkLabel(border_frame, text=hint_name, font=("Arial", 40))
hintlabel.pack(padx=10, pady=10)

# Center word label and other components
wordlabel = CTkLabel(app, text="_ " * len(word), font=("Arial", 30))
wordlabel.grid(row=1, column=0, columnspan=2, pady=10)

guessedlabel = CTkLabel(app, text="", font=("Arial", 20))
guessedlabel.grid(row=2, column=0, columnspan=2, pady=5)

guesslabel = CTkLabel(app, text="Guess: ", font=("Arial", 30))
guesslabel.grid(row=4, column=0, padx=5, pady=10, sticky="e")

guess_en = CTkEntry(app, textvariable=guess_en_var, width=40, font=("Arial", 20))
guess_en.grid(row=4, column=1, sticky="w")

app.bind("<Return>", lambda event: game())

alreadylabel = CTkLabel(app, text="", font=("Arial", 2))
alreadylabel.grid(row=3, column=0, pady=10, padx=5, sticky="w")

guess_en_check = CTkLabel(app, text="", justify=LEFT)
guess_en_check.grid(row=5, column=0, columnspan=2)

guessbutton = CTkButton(app, text="Guess", font=("Arial", 15), width=40, command=game)
guessbutton.grid(row=6, column=0, columnspan=2, pady=5)

chance_label = CTkLabel(app, text="", font=("Arial", 15), text_color="red")
chance_label.grid(row=7, column=0, columnspan=2)

image_label = CTkLabel(app, text="", image=image0)
image_label.grid(row=8, column=0, columnspan=2, pady=10)

resetbutton = CTkButton(app, text="Reset", font=("Arial", 15), width=40, command=reset_game)
resetbutton.grid(row=9, column=0, columnspan=2, pady=4)

# Configure the grid to expand properly
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_rowconfigure(3, weight=1)
app.grid_rowconfigure(4, weight=1)
app.grid_rowconfigure(5, weight=1)
app.grid_rowconfigure(6, weight=1)
app.grid_rowconfigure(7, weight=1)
app.grid_rowconfigure(8, weight=1)
app.grid_rowconfigure(9, weight=1)

check_input()
app.mainloop()

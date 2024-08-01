import random
from words import words

word = random.choice(words).upper()
right_guess = ""
chance = 6
wrong_guess = 0

def game():
    global chance
    global wrong_guess
    global guess
    global right_guess
    w = 0
    while chance > 0:
        for char in word:
            if char in right_guess:
                print(char, end=" ")
            else:
                print("_", end=" ")
                w += 1

        if w == 0:
            print(f"You won! {word}")

        guess = input("\nMake a guess: ").upper()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in word:
            if guess not in right_guess:
                print("correct guess")
                right_guess += guess
            else:
                print("You have already guessed it!")
        else:
            print("Wrong")
        chance -= 1
        if chance == 0:
            print(f";( word was {word}")


game()


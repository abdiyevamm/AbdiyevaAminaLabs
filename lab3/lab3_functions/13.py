"""Write a program able to play the "Guess the number" - game,
where the number to be guessed is randomly chosen between 1 and 20.
This is how it should work when run in a terminal:"""
import random

def game():
    print("Hello! What is your name?")
    name = input()

    print("Well, ", name, ", I am thinking of a number between 1 and 20.")
    num = random.randint(1, 20)
    count = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        count += 1

        if guess < num:
            print("Your guess is too low.")
        elif guess > num:
            print("Your guess is too high.")
        else:
            print("Good job, ", name, "! You guessed my number in ", count, " guesses!")
            break

game()
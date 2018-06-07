#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right
import random

target = random.randint(1,10)

print("Welcome to my guessing game!")

print("I've randomly selected a number between 1 and 10. Try and guess it. I will tell you if you are high or low")



while True:
    
    while True:
        try:
            guess = int(input("Input a number between 1 and 10 \n"))
            break
        except ValueError:
            print("Value must be an integer")
            pass
    if target == guess:
        print("Great guess that was it!")
        break
    elif target > guess:
        print("Guess higher")
    elif guess > target:
        print("Guess lower")
    
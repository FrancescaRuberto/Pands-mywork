# This program promts the user to guess a number, and the goal of the program is to make the user keep guessing the number until gets it right. 
# Author: Francesca Ruberto

import random

lower = 0
upper = 100

random_number = random.randint(lower, upper)
guess = int(input("Please guess the number: "))
while guess != random_number:
    if guess < random_number:
        print("Too low")
    else:
        print("Too high")
 
    guess = int(input("Please guess again:" ))

print("Well done. Yes the number was", random_number)
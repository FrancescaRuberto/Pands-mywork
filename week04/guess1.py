# This program promts the user to guess a number, and the goal of the program is to make the user keep guessing the number until gets it right. 
# Author: Francesca Ruberto

correct_number = 30
guess = int(input("Please guess the number: "))
while guess != correct_number:
    print("Wrong")
    guess = int(input("Please guess again:" ))

print("Well done. Yes the number was", correct_number)



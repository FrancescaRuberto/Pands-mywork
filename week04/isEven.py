# This program permits a user to enter a name and will tell the user if the number is even or odd
# Author: Francesca Ruberto

number = int(input("Enter an int: "))
if (number % 2) == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")
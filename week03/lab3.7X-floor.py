# This program takes in a float and give as output an int rounded down
# Author: Francesca Ruberto

# To complete this program I will need the math.floor() formula 
# I will start with the float number part

import math

number = float(input("Enter a float number:"))
flooredNumber = math.floor(number)
print("Number {} floored is {}: " .format(number, flooredNumber))


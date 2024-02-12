# This program print a random number between 1 and 10
# Author: Francesca Ruberto

import random

#number = random.randint(1, 10)
#print("random number {}" .format(number))

#Allow user to inpur range
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
random_number = random.randint(lower, upper)


print("random number between {} and {} is: {} " .format(lower, upper, random_number))
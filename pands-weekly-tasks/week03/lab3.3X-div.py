# This program divide the first number by the second and give integer result and remainder.
# Author: Francesca Ruberto

x = int(input("Enter first number: "))
y = int(input("Enter second number you want to divide by: "))
answer = (x/y)
remainder = x%y

print("{} divided by {} is {} with remainder {}" .format(x, y, answer, remainder))

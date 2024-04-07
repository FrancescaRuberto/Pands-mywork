# This program keeps reading number until the user enters a 0
# the program will print them back out again and their average
#Author: Francesca Ruberto

numbers = []

number = int(input("enter number(0 to quit): "))

while number != 0:
    numbers.append(number)

    number = int(input("enter another(0 to quit): "))

for value in numbers:
    print (value)

average = float(sum(numbers)) / len(numbers)
print(f"The average is {average}")


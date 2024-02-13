# This program takes is a float amount of dollars and gives as output its absolute amount in cents
# Author: Francesca Ruberto

numberInDollar = float(input("Please enter an amount: "))

#So now I have to add the "cent" specification
convertNumber = int(abs(numberInDollar) *100)

print("Absolute number in cents of {} is {}:" .format(numberInDollar, convertNumber))


# This program reads in a student percentage mark and prints out corresponding grade
# the program should check that the percentage is valid
# Author: Francesca Ruberto

grade = float(input("Enter the percentage: "))
if grade <= 40:
    print("Fail")
elif 40 <= grade <= 49:
    print("Pass") 
elif 50 <= grade <= 59:
    print("Merit 2")
elif 60 <= grade <= 69:
    print("Merit 1")
elif grade >= 70:
    print("Distincion")
else:
    print("not classificable")

"""
Program: sum.py
Project 4.3

Computes the sum and average of a series of input numbers.
"""

theSum = 0
count = 0
while True:
    number = input("Enter a number or press Enter to quit: ")
    if number == "":
        break
    theSum += float(number)
    count += 1

print("The sum is", theSum)
if count > 0:
    print("The average is", theSum / count)

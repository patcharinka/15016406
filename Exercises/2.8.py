"""
Program: fivestar.py
Project 2.8

Calculate the total charge for a customer's video rentals,
given the number of each type of video.

New video rental = $3.00
Oldie rental = $2.00

"""
               
# Initialize constants
NEW_RENTAL = 3.00
OLDIE_RENTAL = 2.00

# Request the inputs
newOnes = int(input("Enter the number of new videos: "))  
oldOnes = int(input("Enter the number of oldies: ")) 

# Compute the results
totalCost = NEW_RENTAL * newOnes + OLDIE_RENTAL * oldOnes

# Display the results
print("The total cost is $" + str(round(totalCost, 2)))

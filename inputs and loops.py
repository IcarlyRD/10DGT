# To learn how to use inputs and loops
# Author: Elaine labuschagne 
# Date: 09/05/2025
# Version 2

#Ask the user a question and store their answer in a variable
# Ask the user for their name and Store 
name = input ("Hi, what is your name? ") # Stores answer as a string
print()# This adds a linne break
# Test that input was stored correctly
print(F"Nice to meet you {name}\n") #\n is a line breakE
# to comment code out, use crtl+/

# Ask the user for two numbers and then add them togther.
num1 = int (input(" what is your first number please? "))
num2 = int (input("what is your second number please? "))
print(f"You entered your first number as {num1}")
print(f"You entered your second number as { num2}")

# Adding the answers togther 
sum =num1+ num2
print(f"The two numbers added togther will result in {sum},")

#Multiply the two input number
multiply=num1*num2
print(f"The two numbers multiplied will result in {multiply},")


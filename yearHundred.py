#!/Users/fktadros/anaconda3/bin/python
"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines.
"""

name = input("Please enter your name: ") # Ask user for their name, will not manipulate this or use it in further operations
age = int(input("Please enter your age: ")) # Force age input to be an integer

import datetime
now = datetime.datetime.now()
year = int(now.year)
yearHundred = year - age + 100
print("You will turn 100 years old in", yearHundred)

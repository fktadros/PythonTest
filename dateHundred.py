"""
Similar to yearHundred.py, this file will calculate the date the user will turn 100.
But instead of asking the user for their age, it will ask them for their birthday in the
format 'dd/mm/yyyy' and output the exact date the turn 100.
"""

name = input("Please enter your name: ") # Ask user for their name, will not manipulate this or use it in further operations
age = int(input("Please enter your birthday (dd/mm/yyyy): ")) # Force age input to be an integer

import datetime
now = datetime.datetime.now()
year = int(now.year)
yearHundred = year - age + 100
print("You will turn 100 years old in", yearHundred)

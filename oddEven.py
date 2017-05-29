#!/Users/fktadros/anaconda3/bin/python
"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""
"""This is my second python program. If given any number, it can output if the number is odd or even."""

str = input("Please enter an integer:") #ask user to input an integer
num = int(float(str)) #force user input into an integer

if num % 2 == 0:
	print("Your number is EVEN")
else:
	print("Your number is ODD")

if num % 4 == 0:
	print("Your number is also divisble by 4")
else:
	print("Your number is also NOT divisble by 4")

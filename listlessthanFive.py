#!/Users/fktadros/anaconda3/bin/python

"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements
less than 5 from this list in it and print out this new list.

Write this in one line of Python.

Ask the user for a number and return a list that contains only elements from the original
list a that are smaller than that number given by the user.
"""

nums = int(input("Enter a list of integers (seperated by commas): ")) # user will input a list of numbers
cutoff = int(input("Enter a number that will act as the upper cutoff for the list: "))
mynums = []
for i in nums:
    if i <= cutoff:
        mynums.append(i)
    else:
        break

print("List containing numbers less than", cutoff, ":", mynums)

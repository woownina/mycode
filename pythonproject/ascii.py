#!usr/bin/python3
""" create program that prints user selected ASCII art"""

#offer the user a menu of possible ASCII art to view
menu =["Sailor Moon", "Sailor Mars", "Sailor Mercury", "Sailor Jupiter", "Sailor Venus"]
print("Welcome to ASCII Art Selector! Please make your selection:", menu)

#take user selection and display art
selection = input()

f = open(selection.lower(), "r")
print(f.read())
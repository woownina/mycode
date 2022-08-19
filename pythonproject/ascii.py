#!usr/bin/python3
""" create program that prints user selected ASCII art"""

def main():
    """run time code"""
    #offer the user a menu of possible ASCII art to view
    menu =["SailorMoon", "Sailor Mars", "Sailor Mercury", "Sailor Jupiter", "Sailor Venus"]
    print("Welcome to ASCII Art Selector! Please make your selection:", menu)

    #take user selection and display art
    selection = input()

    with open(selection.lower() + ".txt", "r", encoding="utf-8") as file:
        print(file.read())

main()

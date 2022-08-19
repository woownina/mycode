#!usr/bin/python3
# pylint: disable=R1727
""" create program that prints user selected ASCII art"""

def main():
    """run time code"""
    #offer the user a menu of possible ASCII art to view
    menu ={
          "A": "Sailor Moon",
          "B": "Sailor Mars",
          "C": "Sailor Mercury",
          "D": "Sailor Jupiter",
          "E": "Sailor Venus"}

    print("Welcome to ASCII Art Selector! Please make your selection:", menu)


    #take user selection and display art
    selection = input(menu.keys)

    if selection == 'A' or 'a':
        with open("sailormoon.txt","r", encoding="utf-8") as file:
            print(file.read())
    elif selection == 'B' or 'b':
        with open("sailormars.txt","r", encoding="utf-8") as file:
            print(file.read())
    elif selection == 'C' or 'c':
        with open("sailormercury.txt","r", encoding="utf-8") as file:
            print(file.read())
    elif selection == 'D' or 'd':
        with open("sailorjupiter.txt","r", encoding="utf-8") as file:
            print(file.read())
    elif selection == 'E' or 'e':
        with open("sailorvenus.txt","r", encoding="utf-8") as file:
            print(file.read())
    else:
        print("Sorry try again")
main()

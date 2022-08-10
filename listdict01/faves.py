#!/usr/bin/env python3

#create first list of favorite foods
faveFoods1 = ["Pizza", "Tacos", "Sushi"]

#create second list of favorite foods 
faveFoods2 = ["Pasta", "Cake", "Ice Cream"]

#create third lost of favorite foods
faveFoods3 = ["Chocolate", "Oatmeal", "Kale"]

#combine lists into single list
faveFoods1.extend(faveFoods2)
faveFoods1.extend(faveFoods3)

#display combined list
print(faveFoods1)

#create dictionary defining three shared qualities of your favorite fictional heroes

heroes = { "gender": "women", "costume": "fierce", "attitude": "badass"}

# printing keys and values separately
print(heroes.keys())
print(heroes.values())

#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""



#accepts decimals as numbers
score = float(input("What is your score?"))

# if input value was higher or equal to 25
if score <=59:
    print("F")
elif score >=60 and <=69:
    print("D")
elif score >=70 and <=79:
    print("C")
elif score >=80 and  <=89:
    print("B")
elif score >=90 and <=100 :
    print("A")    
else:
    print("Enter valid score")


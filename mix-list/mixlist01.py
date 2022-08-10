#!/usr/bin/env python3
#creates a list with three items
my_list = [ "192.168.0.5", 5060, "UP" ]

#returns IP address from list
print("The first item in the list (IP): " + my_list[0] )

#returns port 5060. str() forces integer to be a string
print("The second item in the list (port): " + str(my_list[1]) )

#returns the last item in the list
print("the last item in the list (state): " + my_list[2] )

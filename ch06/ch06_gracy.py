# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:15:12 2018

@author: 612383423
"""

#                        ***Debugging chapter***
#
#userInput = input('please give a number ')
#result = userInput - 2
#we get an error because user input hasn't been converted to an integer

userInput = input('please give a number ')
print(type(userInput))
#we get an error because the user input still hasn't been converted to an integer

userInput = input('please give a number ')

def simpleOperation(userInput):
    intInput = int(userInput)
    result = intInput - 2
    return result
#breakpoint is added at line 21 (double click next to number)
def nestedOperation(result):
    result = simpleOperation(userInput)
    result2 = result * 2
    return result2

result = simpleOperation(userInput)
result2 = nestedOperation(result)
print(result2)

#debug guide 
# first button - start running your code until the break point.
# second button allows you to run your code line-by-line until the breakpoint.
# third button is for stepping into the sections (class and functions) that you would
#  like to dig into more 
# fourth button is for you to step out when you feel that the error is not related to the current section.
#  it allows you to go to the next breakpoint (if you have setup multiple ones) 
# last, square shaped button is for you to exit debugging mode and go
#  back to normal coding mode.
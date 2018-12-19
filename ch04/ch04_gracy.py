# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 11:09:43 2018

@author: 612383423
"""
### Chapter 4: Conditionals

# task 3-5 - using conditional statments 
number=input("enter a number between 1 and 10: ")
number=int(number)
if number > 10:
    print("too high!")
elif number <=0:
    print("too low!")
else:
    print("thanks!")
#    
# elif statements are used because otherwise, if you enter a value such as 30, the
# computer will print two statements.
#
#number=input("enter a number between 1 and 10: ")
#number=int(number)
#if number > 10:
#    print("too high!")
#elif number <=0:
#    print("too low!")
#else:
#    print("thanks!")

#can also do it this way:
#    
#number=input("enter a number between 1 and 10: ")
#number=int(number)
#if number > 10:
#    print("too high!")
#if number <=0:
#    print("too low!")
#if 0 < number <=10:
#    print("thanks!")
#
# however, the else statement is useful for debugging/to catch anything in your 
# program that you might have missed. 

age=15
isaTeen = age>=13 and age<=19
print (isaTeen)

age =20
isaTeen = age>=13 or age <=19
print (isaTeen)

if 1>=10:
    print(False)
else:
    print(True)
    
age = 60     
if age<13:
    print ("child")    
elif age<65:
    print("adult")
elif age <18:
    print("teen")
else:
    print("pensioner")

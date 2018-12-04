# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:59:11 2018

@author: 612383423
"""

age=15
isaTeen = age>=13 and age<=19

#print (isaTeen)

age =20
isaTeen = age>=40 or age <=19
#print (isaTeen)


if 1>=10:
    print(False)
else:
    print(True)
    

#number=input("enter a number between 1 and 10: ")
#number=int(number)
#if number > 10:
#    print("too high!")
#if number <=0:
#    print("too low!")
#else:
#    print("thanks!")
    
#if you enter a value such as 30, the computer will print two statements. this is why elif statements are used! the else can only pair up 
#with the last if.

#number=input("enter a number between 1 and 10: ")
#number=int(number)
#if number > 10:
#    print("too high!")
#elif number <=0:
#    print("too low!")
#else:
#    print("thanks!")

#can also do it this way:
    
#number=input("enter a number between 1 and 10: ")
#number=int(number)
#if number > 10:
#    print("too high!")
#if number <=0:
#    print("too low!")
#if 0 < number <=10:
#    print("thanks!")

#but elif statements are preferable
age = 60    
    
if age<13:
    print ("child")
    
elif age<65:
    print("adult")
elif age <18:
    print("teen")
else:
    print("pensioner")


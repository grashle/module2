# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 15:21:06 2018

@author: 612383423
"""
### Exercises fom Learn Python the Hard Way on conditionals
#11, 12, 27, 29, 30, 31

tabby_cat = ("\tI'm tabbed in.")
persian_cat = ("I'm split\non a line.")
backslash_cat = ("I'm \\\ a \\ cat.")

print (tabby_cat)
print (persian_cat)
print (backslash_cat)


print ("www.facebook.com/home" + "folders\images")

#age = raw_input("How old are you? ")
#height = raw_input("How tall are you? ")
#weight = raw_input("How much do you weigh? ")
#print ("So, you're %r old, %r tall and %r heavy." % (age, height, weight))

#raw_input is obsolete in python 3

people = 20
cats = 30
dogs = 15
birds = 20

if people < cats:
    print ("Too many cats! The world is doomed!")

else:
    print ("Not many cats! The world is saved!")

if people < dogs:
    print ("The world is drooled on!")

else:
    print ("The world is dry!")

dogs += 22

if people >= dogs:
    print ("People are greater than or equal to dogs.")

elif people <= dogs:
    print ("People are less than or equal to dogs.")

else:
    print ("People are dogs.")
    
if people >= birds:
    print ("People are greater than or equal to dogs.")

elif people <= birds:
    print ("People are less than or equal to b.")

else:
    print ("People are birds.")
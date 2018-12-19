# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
###Chapter 2: Operations, Strings, and Variables

### Task 1 - simple operations
print (8*9)
print(6/2)
print (5/2)
print (5.0/2)
print (5%2)
print(2*(10+3))
print (2**4)

A=(5-6)
B=(8*9)
print (A, B)
print (A* -B)

### Task 2 - practising with variables 
age = 5
age ="almost three"
age =29.5
age = 'i really don\'t know'
print (age)
# the age variable is now updated to the second assignment

### Task 3 - basic string manipulation
print('hello'+'world')
print ("Joke " *3)
print("Chen" + str(3))
print("hello".upper())
print("GOODBYE".lower())
print("the lord of the rings".title())

print(type(3.5))

S1='hello' + 'world'
S2="Joke"*3
S3=5

print ((S1+S2)*10)
print('\n')
print((S1+S2*10).split('J'))

#print(S1+S2+str(S3))

### Task 4 - String formatting
age=5
like="painting"
name='bob'

age_description = "my name is {0} my age is {1} and I like {2}.".format(name, age,like)
print (age_description)

name = 'julie'
age_description = "my name is {0} my age is {1} and I like {2}.".format(name, age,like)

print(age_description)

my_name='Gracy'
print ("Let's talk about %s." % my_name)
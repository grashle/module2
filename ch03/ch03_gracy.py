# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 12:20:06 2018

@author: 612383423
"""
"""
print("What's your name? ")
name=input().title()
print("Hello "+ "{}! where are you from, {}?".format(name, name))
#print("where are you from, {}?".format(name))
location=input()
print("wow! i am from {} too, {}!".format(location, name))"""

def hello_world():
    print("Hello World!")
    name_print()

def name_print():
    print("computer says: what is your name?")
    name=input().title()
    print (('ok, so your name is {}. What year were you born?'.format(name)))
    year=int(input())
    age=2018-year
    try: 
        print ("so you are...{}. ".format(age)  + "that's old!" )
    except ValueError:
        print ("i need a number please")
    
hello_world()    


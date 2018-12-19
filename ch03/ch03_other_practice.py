# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 10:09:25 2018

@author: 612383423
"""

def hello_world_2args (c,d):
    print ("{} {}".format(c,d))

a1 ='hello'
b1='world'
a2='love'
b2 = 'coding'

#hello_world_2args (a1, b1)

def add_two_numbers (num1, num2):
    answer = num1 + num2
    print ("{} + {} is {}".format(num1, num2, answer))

#add_two_numbers (2.5, 3)
#add_two_numbers ('dog', 'cat')

def convert_distance(miles):
    kilometers = (miles * 8.0) / 5.0
    
    print ("Converting distance in miles to kilometers:")
    print ("Distance in miles:", miles)
    print ("Distance in kilometers:", kilometers)
    #return kilometers
    

#kilometers = convert_distance(miles)
#convert_distance (105)

def convert_temp ():
    centigrade = int(input("what temperature in Celsius do you want to convert? "))
    kelvin = centigrade + 273.15
    fahrenheit = centigrade*9.0/5.0 + 32
    print ("converting temp in c to farenheit and kelvin...")    
    print("The temperaure in fahrenheit is {}, and the temperature in kelvin is {}".format(fahrenheit, kelvin))
    return (kelvin, fahrenheit)

#kelvin, fahrenheit =convert_temp() 


def add_two_numbers_and_return ():
    number1= 1
    number2 = 2
    answer = number1 + number2
    answer2 = number2/number1
    return (answer, answer2)

returned_value=add_two_numbers_and_return()
#print (returned_value)

def cheese_and_crackers (cheese_count, boxes_of_crackers):
    print ("You have {} cheeses!".format(cheese_count))
    print ("You have {} boxes of crackers!".format(boxes_of_crackers))
    print ("Man that's enough for a party!")
    print ("get a blanket. \n")
    
#print ("We can just give the function numbers directly:")
#cheese_and_crackers (20,30)

amount_of_cheese = 10
amount_of_crackers =50

#cheese_and_crackers (amount_of_cheese, amount_of_crackers)

def add (a,b):
    print ("ADDING {} + {}".format(a,b))
    return a + b

def subtract (a, b):
    print ("SUBTRACTING {} - {}".format (a,b))
    return a-b
def multiply (a, b):
    print ("MULTIPLYING {} * {}".format (a,b))
    return a*b
def divide (a,b):
    print ("DIVIDING {} / {}".format(a,b))
    return a/b

#age = add (30,5)
#height = subtract (78,4)
#weight=multiply(90,2)
#iq = divide (100,2)

#print ("my age is {}, height is {}, weight is {}, iq is {}".format(age, height, weight, iq))

from pylab import sin, cos, pi
#print (sin(2.2))

import datetime
import time

print ("date and time", datetime.datetime.now())

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 09:48:29 2018

@author: 612383423
"""

### Chapter 3: Functions and importing modules

# task 1 & 2 - writing a function with user input
def hello_world():
    print("Hello World!")

def my_name():
    print("computer says: what is your name? ")
    name=input().title()
    print (('Hi {}. What year were you born?'.format(name)))
    year=int(input())
    age=2018-year
    print ("so you are...{}. ".format(age)  + "that's old!" )
    return (name, age)

# task 4    
def add_two_numbers (num1, num2):
    answer = num1 + num2
    print ("{} + {} is {}".format(num1, num2, answer))
def hello_world_2args (c,d):
    print ("{} {}".format(c,d))


        
# task 5 
def convert_temp():
    centigrade = int(input("What temperature in Celsius do you want to convert? "))
    kelvin = centigrade + 273.15
    fahrenheit = centigrade*9.0/5.0 + 32
    print ("Converting temperature in Celsius to Farenheit and Kelvin... \n")    
    print("The temperaure in Fahrenheit is {}, and the temperature in Kelvin is {}".format(fahrenheit, kelvin))
    return (kelvin, fahrenheit)

def convert_distance(miles):
    kilometers = (miles * 8.0) / 5.0
    print ("Converting distance in miles to kilometers:")
    print ("Distance in miles:", miles)
    print ("Distance in kilometers:", kilometers)
    return kilometers


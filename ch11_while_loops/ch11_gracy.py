# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:18:57 2018

@author: 612383423
"""

# while loops may be better for user input. The loop continues to repeat so long
# as the condition is satisfied. 

x=33
while x>=1:
    print(x,': ', end='') #the end parameter means that everything is printed on the same line 
    x=x/2
print(x)
#when the condition is no longer fulfilled, the computer exits the while loop.
   
def triangular(n):
    triangular_num=0
    while n>0:
        triangular_num=triangular_num +n
        n=n-1
        print (n)
    print (triangular_num)

triangular(6)

def factorial(f):
    factorial=1 #this assignment must be outside the while loop
    while f>0:
        factorial=factorial*f
        print(factorial)
        f-=1
    print (factorial)
    
factorial (10)

def auto_marker():
    n=1
    while n>0:
        n=int(input('what mark do you have? '))#put user input inside the while loop so that the value can be continually updated.
        if n>70: 
            print('you got a first class')
        elif n>=40 and n<70:
            print ('you passed!')
        else: 
            print ('you failed')
#auto_marker()

i=55
while i>10:
    print(i)
    i=i*0.8
    if i==35.2:
        break
# an example of using a break loop    
def greeting():
    name= ' '
    while name!='done':
        name=(input('what\'s your name? '))
        if name=='done':
            break
        else:
            print ('hello', name)
        
greeting()

# this 
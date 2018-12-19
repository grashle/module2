# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 12:13:15 2018

@author: 612383423
"""

from random import randint

def guess(endrange,attempts):
    
    number = randint(0,endrange)
#    print('the secret number is', number)
    print("Welcome! Can you guess my secret number? ")
    while attempts>0:
        
        user_guess=int(input("Enter your number: "))
        if user_guess < number:   
            print('you guessed {}. Here\'s a hint - it was too low! You have {} attempts left.'.format(user_guess, attempts))
        elif user_guess > number: 
            print('you guessed {}. Here\'s a hint - it was too high! You have {} attempts left.'.format(user_guess, attempts))
        elif user_guess ==number:
            print('That\'s the right number. You won!')
            break
        attempts-=1
    print ("Thanks for playing!")

#guess(100,8)

#watch MIT lecture 9 for why it isn't good for a while loop to be nested

def dicegame():
    total=2
    print('welcome to my game!') 
    if total%2==0:
        result= 'even'
    else:
        result= 'odd'
    while total>0:
        dice1=randint(0,6)
        dice2=randint(0,6)
        total=dice1+dice2    
        response=input('Guess even, odd, or type quit to quit. ')
        if response == result:
            print('you won')
            print('i rolled two dice with values {} and {}. the total was {}.'.format(dice1,dice2,total))
        elif response != result:
            print('you lost, sorry')
            print('i rolled two dice with values {} and {}. the total was {}.'.format(dice1,dice2,total))
            print('try again?')
        elif response == 'quit':
            print('you left the game')
            break

dicegame()
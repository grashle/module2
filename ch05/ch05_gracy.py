## -*- coding: utf-8 -*-
#"""
#Created on Wed Dec  5 10:07:55 2018
#
#@author: 612383423
#"""
#
#class Customer(object):
#    """A customer of ABC bank with a checking account. customers have the following properties: 
#        Attributes:
#            name: a string representing the customer's name.
#            balance: a float tracking the current balance of the customer's account. """
#    
#    def __init__(self,name,balance=0.0):
#        """Return a Customer object whose name is *name* and starting balance is *balance*."""
#        self.name=name
#        self.balance=balance
#    
#    def withdraw(self, amount):
#        """Return the balance remaining after withdrawing *amount* dollars."""
#        if amount > self.balance:
#            raise RuntimeError ('Amount greater than available balance.')
#        self.balance -=amount
#        return self.balance
#
#    def deposit (self, amount):
#        """Return the balance remaining after depositing *amount* dollars."""
#        self.balance += amount
#        return self.balance
#    
#jason = Customer('Jason Taylor', 1000.0)
#
#gracy = Customer('gracy de', 500.0)
#
#jason.withdraw(100.0)
#
##Customer.__init__('susie de',balance=0.0)  - the init fucntion cannot be called in this way
#
#jon = Customer('jon Taylor',1000.0)
#
#class Animal():
#    def eat (self):
#        print ('yum')
#    def __init__(self, habitat, age=1.0):
#        self.habitat=habitat
#        self.age=age
#
#class Dog(Animal):
#    def bark(self):
#        print('Woof!')
#        
#class Cat(Animal):
##    def __init__ (self, habitat, age=1.0, furballs):
##        self.furballs=furballs
##       # Animal.__init__(self, furballs)
##    #    def __init__ (self, furballs=3):
###        self.furballs=furballs
##    def __init__(self, furballs=1.0):
##        self.furballs=furballs
#    def cough(self):
#        print('coughed up', self.furballs, 'furballs!')             
#    def meow(self):
#        print ('Meow')
#    def climb(self):
#        print('cat climbs curtain')
#    def milk(self):
#        print('cat drinks milk')
#        
##furballs=input('type a number:')
#        
#Snoopy=Dog('kennel', age=5.0)
#Snoopy.bark()
#Snoopy.eat()
#
##Mabon = Cat()
##Mabon.meow()
#
##Snoopy.meow() - this cannot be done because snoopy is not in the cat subclass
#
#class Kitten(Cat):
#    def purr(self):
#        print ('kittens are cute')
#        
#frank=Kitten('pillow', age=0.5, furballs=0.5)
#frank.purr()
#frank.eat()
#frank.milk()
#
#print(frank.habitat)
#print(frank.age)
class Animal():
    def eat(self):
        print('yum')
class Dog(Animal):
    def bark(self):
        print('Woof!')
class Robot():
    def move(self):
        print('...move move move...')
class CleanRobot(Robot):
    def clean(self):
        print('I vacuum dust')
class SuperRobot():
    def __init__(self):
        self.o1 = Robot()
        self.o2 = Dog()
        self.o3 = CleanRobot()
    def playGame(self):
        print('alphago game')
    def move(self):
        return self.o1.move()
    def bark(self):
        return self.o2.bark()
    def clean(self):
        return self.o3.clean()
machineDog=SuperRobot()
machineDog.move()

#-*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:07:55 2018

@author: 612383423
"""
### Chapter 5: Object Oriented Programming 

### Task 1 - Using classes 

class Customer(object):
    """A customer of ABC bank with a checking account. customers have the following properties: 
        Attributes:
            name: a string representing the customer's name.
            balance: a float tracking the current balance of the customer's account. """
    
    def __init__(self,name,balance=0.0):
        """Return a Customer object whose name is *name* and starting balance is *balance*."""
        self.name=name
        self.balance=balance
    
    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount* dollars."""
        if amount > self.balance:
            raise RuntimeError ('Amount greater than available balance.')
        self.balance -=amount
        return self.balance

    def deposit (self, amount):
        """Return the balance remaining after depositing *amount* dollars."""
        self.balance += amount
        return self.balance
    
jason = Customer('Jason Taylor', 1000.0)

gracy = Customer('gracy de', 500.0)

jason.withdraw(100.0)

#Customer.__init__('susie de',balance=0.0)  - the init fucntion cannot be called in this way

jon = Customer('jon Taylor',1000.0)

### Task 2 & 3 - Using inheritance 

class Animal():
    def __init__(self, name, age=1.0):
        self.name=name
        self.age=age
    def eat (self):
        print ('yum')

class Dog(Animal):
    def bark(self):
        print('Woof!')
        
class Cat(Animal):
    def __init__(self, name, age, furballs=1.0):
        Animal.__init__(self, name, age)
        self.furballs=furballs
    def cough(self):
        print(self.name,'coughed up', self.furballs, 'furballs!')             
    def meow(self):
        print ('Meow')
    def climb(self):
        print('cat climbs curtain')
    def milk(self):
        print('cat drinks milk')
             
firstdog=Dog('snoopy', age=5.0)
firstdog.bark()
firstdog.eat()

firstcat = Cat('mabon', age=6.0, furballs=2)
firstcat.meow()
firstcat.cough()

#firstdog.meow() - this cannot be done because firstdog is not in the cat subclass

class Kitten(Cat):
    def purr(self):
        print ('kittens are cute')
# here, any objects in the Kitten class inherit the properties of the Cat class (which
# in turn inherit the properties of the Animal class.)
        
firstkitten=Kitten('frank', age=1, furballs=3)
firstkitten.purr()
firstkitten.eat()
firstkitten.milk()

print(firstkitten.furballs)
print(firstkitten.age)

### Task 4 - Using association

class Animal2():
    def eat(self):
        print('yum')
class Dog(Animal2):
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

# here, a superclass has been created which can take on properties of multiple child 
# classes 

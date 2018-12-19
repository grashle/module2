# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:21:41 2018

@author: 612383423
"""
phonebook_dict={}
count=0
def ask_user(count):
    
    name = input('what\'s your name? ')
    phone_no= input('what are the last three digits of your phone number? ')
    lucky_no = int(input ('lucky number? '))
    postcode = input('postcode? ')
    town = input ('town? ')
    age = int(input('what year are you born? '))
    QueenAgeDiff = (age-1926)
    phonebook_dict[name.title()]=(phone_no, lucky_no, postcode.upper(), town.title(), age, QueenAgeDiff)
    yes_no = input('add another person? y/n ')  
    max_people = 3
    if count < max_people:
        while yes_no == "y" :
            count+=1
            print(count)
            ask_user(count)
            return phonebook_dict
    return True  
    
ask_user(count)

#phonebook_dict={'Gracy': ('0121', 12, 'B43', 'Birmingham'), 'Dave': ('0122', 7, 'B21', 'Yardley'), 'Matt': ('1244', 56, 'S23', 'Sheffield'), 'Sally': ('4456', 9, 'E17', 'London')}

def lucky_list():
    lucky_no_list = (sorted(phonebook_dict.items(), key = lambda kv:kv[1][1]))
    print('lucky numbers ascending: ')
    for l in lucky_no_list:
        print (l[0], l[1][1])
lucky_list()

def names_alphabetical():
    alphabetical_namelist = (sorted(phonebook_dict.items(), key = lambda kv:kv))
    print ('names in alphabetical order: ')
    for l in alphabetical_namelist:
        print(l)#using the for loop because it puts each key value pair on a new line and so easier to read
        
names_alphabetical()

def city_alphabetical():
    city_namelist = (sorted(phonebook_dict.items(), key = lambda kv:kv[1][3]))
    print ('cities in alphabetical order: ')
    for l in city_namelist:
        print(l)
city_alphabetical()


f = open("phonebook_dict.txt","w")
f.write(str(phonebook_dict))
f.close()

 



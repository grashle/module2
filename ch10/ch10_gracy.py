# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:54:05 2018

@author: 612383423
"""

## dictionary syntax is {key1: value1, key2: value2, etc} 
#{'gracy':50000, 'chen': 20000, 7: ('Muna','Gracy', 'Joke')}
#
## an new dictionary is created by assigning {} to a variable. you can also empty
## dictionaries this way!
#
#salary={}
#salary['gracy de']=500
## type 'salary' into the console to view the new dictionary. 
#salary['dacey de']=1000
## if you want to use a number as a key value, it cannot start with 0 (eg 007)
## python will just convert that to '7'.
#
## you can use operations on mutable data types. 
#salary['gracy de']+=100
#print (salary['gracy de'])
#
#tel={'muna':856, 'gracy':680, 'joke': 665, 'leanne': 511}
#
#tel['gracy']=1680
#tel['muna']='0856'
#
#newtel = {x:'same number' for x in tel}
##print (newtel)
#
#del tel['leanne'] #this deletes a value/key pair from dictionary
#print (tel)
#
#print (tel.keys()) #gets list of dictionary keys only
#print (tel.values()) #gets list of dictionary values only
#
## however (see console) these lists are not standardised and will need to be 
## cast into the list data type as below in order to access by index ([0],[1]): 
#
#list_of_names = list(tel.keys())
#print (list_of_names)
#
#list_of_numbers = list(tel.values())
#print(list_of_numbers)
## now, the list can be accessed by index
#print(list_of_numbers[0])
## checking if a key is present in a dictionary using if/else:
#
#if 'gracy' in tel:
#    print('gracy', ':', tel['gracy'])
#else: 
#    print('gracy', 'not found!')
#g='eric'    
#if g in tel:
#    print(g,':', tel[g])
#else:
#    print(g, 'not found!')

counts={'a':3, 'c':1, 'b':5}
labels=list(counts.keys())
print(labels)
#prints an unsorted list of keys pulled from the dictionary - acb
labels.sort(key=lambda x:counts[x])
print(labels)
# prints a list of keys sorted by their assigned value from the dictonary - cab/135 
print ('original dictionary')
luckynumbers={'muna': (7,19), 'gracy':(8,13), 'leanne':(1,4), 'rachel': (4,56)}
print (luckynumbers)
print('--DICTIONARY KEYS--')
namelist=list(luckynumbers.keys())
print (namelist)
valuelist=list(luckynumbers.values())
print ('--DICTIONARY VALUES--')
print (valuelist, '\n')

valuelist.sort(key=lambda x:x[1])
print ('values sorted by fav number, second item of list')
print(valuelist, '\n')

namelist.sort(key=lambda x:luckynumbers[x])
print ('list of names sorted by first value (birth month, 1 4 7 8)')
print (namelist, '\n')

namelist.sort(key=lambda x:luckynumbers[x][1])
print ('list of names sorted by second value (fav number, 4, 13, 19, 56)')
print (namelist, '\n')
# this sorts by favourite number which is at position [1] (second) in the list

#namelist.sort(key=lambda x:luckynumbers x[1])

print(sorted(valuelist, key = lambda xy:xy[1]))

#sorted(counts.items(), key=lambda kv:kv[1])
print(sorted(luckynumbers.items(), key = lambda xy:xy[1]))#,reverse=True))



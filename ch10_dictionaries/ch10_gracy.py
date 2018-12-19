# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:54:05 2018

@author: 612383423
"""
### Chapter 10: Dictionaries 

### Task 1&2 - Creating a dictionary: assigning, retrieving and updating values

# The dictionary syntax is {key1: value1, key2: value2, etc} 
{'gracy':50000, 'chen': 20000, 7: ('Muna','Gracy', 'Joke')}

# A new dictionary is created by assigning {} to a variable. you can also empty
# dictionaries this way.

salary={}
salary['gracy de']=500
salary['dacey de']=1000
# If you want to use a number as a key value, it cannot start with 0 (eg 007)
# python will just convert that to '7'.

## you can use operations on mutable data types. 
salary['gracy de']+=100
print (salary['gracy de'])

### Task 2 (creating another dictionary) and Task 3 - Looking up and deleting values
tel={'muna':856, 'gracy':680, 'joke': 665, 'leanne': 511}

tel['gracy']='1680'
tel['muna']='0856'

del tel['leanne']          # this deletes a value/key pair from dictionary
print (tel)

### Task 4 - Getting keys and values from a dictionary

print (tel.keys()) #gets list of dictionary keys only
print (tel.values()) #gets list of dictionary values only

# however these lists are not standardised and will need to be 
# cast into the list data type as below in order to access by index ([0],[1]): 
list_of_names = list(tel.keys())
print (list_of_names)
list_of_numbers = list(tel.values())
print(list_of_numbers)
# now, the lists can be accessed by index.

### Task 5 - Retrieving the first key from the dictionary
print(list_of_names[0])

###Task 6 - Avoiding key errors ###

# checking if a key is present in a dictionary using if/else:
g= 'gracy'
if g in tel:
    print(g,':', tel[g])
else: 
    print(g, 'not found!')
e='eric'    
if e in tel:
    print(e,':', tel[e])
else:
    print(e, 'not found!')


### Task 7 - Sorting a dictionary ####
    
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
print ('values only sorted by lucky numer (second number)')
namelist.sort(key=lambda x:luckynumbers [x])

print(sorted(valuelist, key = lambda xy:xy[1]))

#sorted(counts.items(), key=lambda kv:kv[1])
print(sorted(luckynumbers.items(), key = lambda xy:xy[1]))#,reverse=True)


### Task 8 - Sorting a dictionary ### 

metals = {'iron': (7.8, 100, 3), 'gold':(19.3, 400, 1), 'zinc':(7.13, 50, 6), 'lead':(11.4, 300, 1)}
# --metal: (density, share price, experiments)
metalnames = list(metals.keys()) #pulls dictionary keys into list
metal_properties = list(metals.values()) # pulls dictionary values into list

# sorting by descending share price using .sort() 
sorted_metal_shareprice = metal_properties.sort(reverse=True, key=lambda x:x[1]) 
print(sorted_metal_shareprice) #<- does not work as .sort does not return an iterable value

# sorting the metal names (keys) by descending share price using .sort(), 
metalnames.sort(key=lambda x:metals[x][1], reverse=True)

# sorting by descending share price using sorted() 
print(sorted(metals.items(), key=lambda x:x[1][1], reverse=True))
# this will convert both the keys and values into list items because metals.items() is called.

# sorting by descending price using sorted(), but only showing the keys
l = (sorted(metals.items(), key=lambda x:x[1], reverse=True))
for key in l:
    print (key[0], key[1][1])




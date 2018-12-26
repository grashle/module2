# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:56:24 2018

@author: 612383423
"""

# Task 1 and 2 - iterative loops

my_shopping_cart= ["cake", "plates", "plastic forks", "juice", "cups"]
for item in my_shopping_cart:
    print (item)
    
values = [875, 23, 451]
for val in values:
    print ('---> ' + str(val))

for val in values:
    print ('---> ' + str(val+50)) # have to convert it to a string to concatenate using + sign

for val in values:
    print('-->  ', val+50)
    
# Task 3 - Looping through a compound list

values=['this', 55, 'that']
for item in values:
    print('***', item)
        
# Task 4 - looping through other data types    

for char in "yes":
    print(char)

for char in 'i like code code'.split():
    print (char)
    
# Task 5 - looping through a tuple 
    
newtuple=('keyboard', 'mouse', 'computer')
for i in newtuple:
    print (i)
   
# Task 6 and 7 - create and sort through a dictionary using for loops
metals = {'iron': (7.8, 100, 3), 'gold':(19.3, 400, 1), 'zinc':(2.13, 50, 6), 'lead':(4.4, 300, 1)}

l = (sorted(metals.items(), key=lambda x:x[1][1], reverse=True ))
print ('2 highest share values:')
for key in l:
    print (key[0],'=', key[1][1])
    
print(sorted(metals.items(), key=lambda x:x[1][2]))

metal_list = list(metals.keys())
print(metal_list)
metal_list.sort(key=lambda x:x[-2])
print(metal_list)

# there are two different methods: using the sorted function and getting the key/value
# pair together 

# Task 8 - using an if/else statement to filter results 
total=0
l = (sorted(metals.items()))
print ('which densities are above 6?')
for key in l:
    if key[1][0]>6:
        print (key[0],'=', key[1][0])
    else:
        print (key[0], 'has a density below 6. ')

print('\n adding up values for certain conditions using a \'total\' line:')

print ('which densities are above 6?')
for key in l:
    if key[1][0]>6:
        print (key[0],'=', key[1][0])
        total+=key[1][0]
    else:
        print (key[0], 'has a density below 6.')
print ('the total density above 6 is', total)

# Task 9 - using a for loop to sum a list 

values=[3,12,9]

total=0 
for val in values:
    total+= val
print('TOTAL: '+ str(total))

# Task 10 - using the len() function with a for loop
for index in range (len(values)):
    values[index] = values[index]*2
print(values)

# Task 11 - using the range function with a for loop
for i in range (3,10,2):
    print(i)
        
for v in values:
    print(values)
#print(len(values))
for index in range (len(values)):
    print (index)
    
for index in range (len(values)):
    print (values[index])
    
#note that each of these three for loops has the same output
    

values=[3,12,9, 2, 3,45,6]
for index in range (0, len(values),3):
    print (values[index]) #this prints 3, 2, 6


values=['milly', 'sarika','fabi','amina','joke','chen','loren']
for index in range (0,len(values)):
    if values[index]=='fabi':
        print('found fabi', values[index])
        break
    else:
        print('not fabi')
        
# Task 12 - scanning a list to check if any are over 100
        
test_list=[1,5,30,200,101,100,22]
for no in test_list:
    if no>100:
        print (no, 'is greater than 100.')
        break
for index in range(len(test_list)):
    if test_list[index]>100:
        print('break :', test_list[index], 'which has an index of', index)
        break

colours=['red','green','red','green','blue','green','green']
d={}
for item in colours:
    if item not in d:
        d[item]=1
        print(d,'first time')
    else: 
        d[item]=d[item]+1
        print(d)
        
        
# Task 13 - Nested loops 
        
outer_vals_list=[1,2,3]
inner_vals_list=['A','B','C']
dictionary={}

for outer_val in outer_vals_list:
    print(outer_val, inner_vals_list)
    dictionary[outer_val]=inner_vals_list
    
print(dictionary)
print()
for outer_val in outer_vals_list:
    print(outer_val)
    for innerval in inner_vals_list:
        print(innerval)
        dictionary[outer_val]=innerval
        print(dictionary)
    #dictionary[outer_val]=inner_vals_list
print(dictionary)
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 10:00:01 2018

@author: 612383423
"""

my_favourite_fruits=['apple', 'orange', 'banana']
x = ['this', 55, 'that', my_favourite_fruits, 'that', 'very']

x.remove(my_favourite_fruits)

#print (x)
#x[1]='and'
#print(x)
#x.append('again')
#print(x)

x[1]='and' #updates the list item value

x.append('again')

y=x
y.append('Katie')
x.append('gracy')
#both x and y are updated with the same list items. 

# x.remove([-2]) this doesn't work because you can't reference index items using 
# the remove.() method. instead, del or pop can be used.  

print(x)

a = ['the', 'cat', 'sat']
b = ['on', 'the', 'mat']

c = set(a+b)
print (c)
# set() removes duplicate items. also returns the output in a random order
# sets are unordered and unindexed

setx= (set(x))

#print (c+setx)
# can't use the + operator on sets 

unsliced_list = ['this', 'and', 'that', 'once', 'again']

#unsliced_list[0:2]
#Out[58]: ['this', 'and']
#
#unsliced_list[-3:-1]
#Out[59]: ['that', 'once']
#
#unsliced_list[2:0]
#Out[60]: []
#
#unsliced_list[-1:-3]
#Out[61]: []

#unsliced_list[0:0]
#Out[65]: []
#
#unsliced_list[0:2]
#Out[62]: ['this', 'and']

# blank output in above examples shows that the computer only reads left to right
# it will not output anything for a range given in reverse order

#unsliced_list[-3:]
#Out[67]: ['that', 'once', 'again']

d = [7, 11, 3, 9, 3, 2]
e = sorted(d)
#print(e)

#d.sort()
#print(d.sort())#returns none because sort is just a function/action
#
#x = [7,11,3,9,2]
#sorted(x)
#Out[79]: [2, 3, 7, 9, 11]
#sorted(x,reverse=True)
#Out[80]: [11, 9, 7, 3, 2]
#x.sort()
#x
#Out[82]: [2, 3, 7, 9, 11]
#x.sort(reverse=True)
#x
#Out[84]: [11, 9, 7, 3, 2]

###
#--------x.sort() makes a change to stored variable but sorted(x) doesn't--------

#x = [7,11,3,9,2]
#print (sorted(x))
#print(sorted(x,reverse=True))

d.append('z')
print(d)
f=(0,1,2,3,4,5,6)
#f.append('z')
print(f)

# Tuples can be converted to lists & vice versa. this is one way to change
# the contents of the tuple.
# for example: 
##list(f)
##Out[112]: [0, 1, 2, 3, 4, 5, 6]
#
##tuple(d)
##Out[113]: (7, 11, 3, 9, 3, 2, 'z')
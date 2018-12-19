# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 10:00:01 2018

@author: 612383423
"""
### Chapter 9: Lists & Tuples

### Task 1 - Creating a list  
my_favourite_fruits=['apple', 'orange', 'banana']
x = ['this', 55, 'that', my_favourite_fruits, 'that', 'very']
print(x)



### Task 2 - Modifying a list ###
x.remove(my_favourite_fruits)

# x.remove([-3]) <--- doesn't work because you can't reference index items using 
# the remove.() method. instead, del or pop can be used.
print (x)
x.append('again')
print(x)
x[1]='and' #updates the list item value
y=x
y.append('Katie')
x.append('gracy')
# note that both x and y are updated with the same list items. 
print(x)





### Task 3 - Slicing a list  ###
print(x[1:4]) #[index inclusive:index exclusive]

#unsliced_list[-1:-3]
#Out[61]: []

#unsliced_list[0:0]
#Out[65]: []
#
#unsliced_list[0:2]
#Out[62]: ['this', 'and']

# The blank output in above examples shows that the computer only reads left to right.
# It will not output anything for a range given in reverse order.




### Task 4 - Sorting a list  ###
d = [7, 11, 3, 9, 3, 2]
e = sorted(d)
print(e)
# reverse sort
print(sorted(d,reverse=True))
d.sort()
print(d.sort()) 
# the above returns None because .sort is a method. 
# x.sort() makes a change to stored variable but sorted(x) doesn't





### Task 5 - Using tuples ###

f=(0,1,2,3,4,5,6)
#f.append('z')     # you cannot alter an item inside a tuple
#del f [-1]        # you cannot delete an item inside a tuple
#f[0]=10           # you cannot assign a new value to a position in an existing tuple
print(f)

# Tuples can be converted to lists & vice versa. this is one way to change
# the contents of the tuple.
# for example: 
##list(f)
##Out[112]: [0, 1, 2, 3, 4, 5, 6]
#
##tuple(d)
##Out[113]: (7, 11, 3, 9, 3, 2, 'z')





### Task 6 - Using lambda to sort a list ###

j = ['aa', 'sb', 'lf', 'hw', 'ed', 'fy']
k = ['zs', 'yw', 'hd', 'cs', 'ab']
l=sorted(j)
x2=[('a',3,l), ('c', 1, k), ('b', 5, j)] # this is a list of tuples


print (sorted(x2, key=lambda s:s[2]))    # this sorts by second value in tuple
#print (sorted(x2, key=lambda s:s[2][-1][-2]))

a = ['the', 'cat', 'sat']
b = ['on', 'the', 'mat']
c = set(a+b)
print (c)
# set() removes duplicate item and also returns the output in a random order
# sets are unordered and unindexed.
#print (c+set(x))                        #you can't use the + operator on sets 



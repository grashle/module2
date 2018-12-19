# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:46:36 2018

@author: 612383423
"""

a = [50, 1, 2,3,4,5,6,7,8,9]
b= (0,1,2,3,4,5,6,7,8,9)
my_favourite_fruits = ['apple', 'orange', 'banana']
x = ['aa', 'sb', 'lf', 'hw', 'ed', 'fy']
z = ['zs', 'yw', 'hd', 'cs', 'ab']
y=sorted(x)

#yu = lambda a: a + 10
#print (yu(5))
x2=[('a',3,z), ('c', 1, y), ('b', 5, x)]
# x2 is a list of tuples

#x2
#Out[12]: 
#[('a', 3, ['zs', 'yw', 'hd', 'cs', 'ab']),
# ('c', 1, ['ed', 'fy', 'hw', 'lf', 'sb', 'xa']),
# ('b', 5, ['xa', 'sb', 'lf', 'hw', 'ed', 'fy'])]
#
#sorted(x2)
#Out[13]: 
#[('a', 3, ['zs', 'yw', 'hd', 'cs', 'ab']),
# ('b', 5, ['xa', 'sb', 'lf', 'hw', 'ed', 'fy']),
# ('c', 1, ['ed', 'fy', 'hw', 'lf', 'sb', 'xa'])]

print (sorted(x2, key=lambda s:s[2]))
print (sorted(x2, key=lambda s:s[2][-1][-2]))
# note the difference between output (paste directly into console to read it easier)
# the letter s can be replaced by any placeholder
# forcing the computer to order things by an absolute position (when they
# are all the same, eg x=0) will just return default input order)
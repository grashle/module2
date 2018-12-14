# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 14:03:29 2018

@author: 612383423
"""

densities = {'iron':7.8, 'gold':19.3, 'zinc':7.13, 'lead':11.4}
#metals = list(densities.keys())
#(iron, gold, zinc lead)
#metals.sort(reverse=True, key=lambda m:densities[m])
#(gold, lead, iron, zinc)

#sorted(densities.items(), key=lambda kv:kv[1], reverse=True)
# sorts by densities descending

#print(sorted(densities.items(), key=lambda kv:kv[1], reverse=True))

#TASK

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



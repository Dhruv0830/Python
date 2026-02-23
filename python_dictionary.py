#Python Dictionary

a = {"key":"value"}

#Does not have indexing
#It is mutable
#Keys are immutable
#Values can be mutable
#Keys are unique

#Mutable - list,set,dict
#Immutable - string,tuples,float,int,complex,Boolean

#When value is edited then memory address changes in immutable data types and a new object is created

d2 = {(1,2,3):"Nitish"} #Correct as tuple is immutable
d3 = {[1,2,3]:"Nitish"} #Throws error as list is mutable

d4= {1:2,1:3} #This stores 1:3

#Accessing items 

d4[1] #Key value not the index
d4.get(1)#Not good for 2d

#Edit
d4[1] = 4
d4["this"]="that"

#Deleting 

del d2
del d4[1]
d2.clear()

#Operations in dictionary

#No concatenation and multiplication but loops work

for i in d4:
    print(i,d4[i])

# 1 in d4 . Checks in keys not values

#len,max,min,sum if keys integer,sorted

d4.keys() #list of keys
d4.values() #list of values

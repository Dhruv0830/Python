#Python Set

#Sets don't allow duplicates
#Set does not have indexing , therefore slicing not possible
#Sets do not allow mutable data types
#Set is itself mutable .Therefore 2d sets not possible due to above rule

s1 = set() #Empty set
s1 = {1,2,3,4}
s2 = {1,2,3,4,"hello"}

s3 = {[1,23],'hello'} #Throws error

s4 = {(1,2,3),"hello"} #output has hello before the tuple as they do not have indexing but rather use hashing to decide the position of the element

s5={{1},{2}} #Unhashable type set .Throws error


#We cannot edit nor access items from a set

#Even if we convert to a list then again to a set, we cannot do this inplace, the new set will be a different object

#Adding items

s1.add(6) #inplace adding. Therefore mutable

#Deleting items

del s1    #Deletes the whole set
s1.remove(55)  #Removes 
s1.pop()  #Removes the last item. Not last index but last hash address element


#Set Operations

s1={1,2,4,5}
s2={1,2,4,5,6}

#Cannot concatenate or multiply sets , but membership and loops work

#len, sum, sorted(converts to list), max, min are there

s1.union(s2)
s1.intersection(s2)
s1.difference(s2)
s1.symmetric_difference(s2)
s1.isdisjoint(s2)
s1.issubset(s2)
s1.issuperset(s2)




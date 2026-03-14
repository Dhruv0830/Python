#Python list

#Array is homogeneous while list is not. Also elements in list are not contiguous , therefore lists are slower as a result.

l1= [1,2,3,4]
l3= [1,2,3,True]
l2= [1,2,3,[1,2]]
list("hello")

l1[0] #These functions are similar to strings, but there are differences for multidimensional lists 
l2[3][1]

l2[2] =100 #lists are mutable
l2[0:2] = [1,2,]

#Adding into list

l1.append(100)
l1.append([1,2]) #Single item for append

l1.extend([33,44,22,33]) #Adding multiple items
l1.extend("hello")

l2.insert(0,"world") #inserting at desired location

#Deleting from list

del l2
del l2[1]
del l2[-3:]

l1.remove("hello") #When index not known but item is known

l1.pop() #removes last item

l1.clear() #Removes all the items

#Concatenation

l1+l2 #This is a new list
l1*3 #Multiplies list three times

4 in l3 #True or false

#Functions for list

len(l1)
min(l1)
max(l1)
sorted(l1,reverse=True) #This is not inplace
l1.sort(reverse=True) #This is inplace
l1.index(2) #returns first index of 2

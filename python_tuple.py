#Python tuples

#Creating a tuple
t1=()
t2=(1,2,3)
t3=('hello',2,3,4)
t4=((1,2),(2,4))

#If we try to create a single element tuple, and check the data type of that tuple , we will get the data type of the single element.

#To make a single value tuple we need to ensure that we are adding a comma after the element

t1=(1) #still an int
t1=(1,) #now a tuple

t6 =tuple('Goa')
t6 =tuple([1,2,3])


#Accessing an item from a tuple

t2[0]

#Difference between a list and tuple - Tuple is immutable unlike list

t2[0] = 100 #Throws an error

#Adding an item is also not possible as we cannot edit a tuple

del t2[-1] #Throws an error

t2+t1 #same as list
t2*3 #same as list

#max(), min(), sum(), len() same as list , but if we use sorted it returns a list instead of the tuple

#Tuples are read-only data type - therefore used where data integrity is important


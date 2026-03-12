#Any program is stored in ROM when not running. While executing it is in RAM.
#Registers - hexa-decimal address and variable value in binary.
#Python calls variable as 'name'. The variable points towards the memory address which contains the value of the variable - Call by Object Reference.

#Aliasing - if a=5 and b=a . Then the id of both a and b will be same. b starts pointing at the same address as a.
#Even if we del a, b still exists and points to 5.

#Now, if we make a=6 then b will still point to 5 as b will have the same object reference in it while a starts pointing to some other address which contains the value 6.

#Reference Counting-
import sys
a='corona'
b=a
c=b
#The number of variables pointing to a memory location can be ascertained using the following code.
sys.getrefcount(a)
#We get 3+1 .Number of variables pointing to corona string + the getrefcount also assigns a variable to find out the others which increases it by 1.

#Garbage Collection
#When we have a value which is not pointed by any variable then it is unnecessarily occupying that memory location. Python does not provide us with manual garbage collection like C does, but it has a garbage collector which runs periodically and frees up memory.In C there is no internal Garbage Collector , we need to manually do it.

#Weird Behaviour in Python
#1.
a=2
b=a
c=b
sys.getrefcount(a)
#Ideally, this should give us 4 as the answer but due to the fact that 2 is a very common number it is already being pointed by a lot of variables and thus we get a very high number like 373. If we use an uncommon number then it is possible that we might get 4 as the answer.

#The above behaviour occurs when the value is between -5 to 256 . But, if we go beyond this range then 2 different objects are created in two different memory addresses.

a= 256
b= 256
#This will have only one memory address with 256 and both pointing to it.

a = 257
b = a #This will result in 3 pointers pointing to 257 

b = 257 #This will result in new address for a and b as it is out of range.

#This is software optimization. When we open python it creates -5 to 256 cells with values to point.But if we go beyond then the third case occurs.

a= "this"
b= "this"
id(a)
id(b)#As the string is a valid identifier(no digit in starting and only _ as special character).Therefore the ids are same
a= "this is a string"
b= "this is a string"
id(a)
id(b)#As the string is not a valid identifier.Therefore the ids are not same(there are spaces.)
a= "this_is_a_string"
a= "this_is_a_string"
id(a)
id(b)#As the string is a valid identifier.Therefore the ids are same

#How are lists stored in python

l=[1,2,3]
#If we find the id of 1 and l[0] then it will be same. Therefore we have an address for the list and the list itself has ids which point to the elements in the list .
l=[1,2,[3,4]]
#In the above example the inner list will have its address stored inside the main list and the inner list will have addresses pointing towards 3 and 4.

#The above logic holds true for tuples as well.

#Mutability - Ability to change the data in its memory location.

#Side effects of Mutability

l1=[1,2,3]
l2=l1

l2=[1,2,3,4]

#Then l1 also changes.To avoid this do the following

l3=l1[:]

#In list concatenation changes the address but appending or any other built in function does not change the address.

a =[1,2]
b =[5,3]
c=(a,b)

c[0][0] =100 #This is legal and will go through but 
c[0] = c[0] + [4,5] #This will not go through as new list will be created due to concatenation.Now ,

a=a+[5,6]
#a will change but c will not change.
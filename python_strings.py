#Strings in Python - Strings are a sequence of UNICODE characters

#Ascii codes are 8bit. After incorporating multiple languages. It was not possible to represent the new languages in ascii. Therefore UNICODE was created. It is a 16 bit format for representing characters.

#Creating strings

a = 'String'
b = "It's raining outside"
c = '''This is a 
        multiline string'''

#Indexing and Slicing

print(a[0]) #Positive indexing - Left to Right
print(a[-1]) #Negative indexing - Right to left 

print(a[0:4])   #0 till 3
print(a[2:])    #2 till end 
print(a[:4])    #Start till 3
print(a[:])     #Full String
print(c[2:6:2]) #Slicing with step
print(c[::-1])  #Reversing

#Editing and Deleting Strings

#Strings are immutable in Python. We can reassign but cannot edit

del b #Deleting full string

del b[0] # String does not support item deletion


#String Operations in Python

#Arithmetic Operations - 

"Hello" + "World"
"Hello"*50

#Relational Operations

"Hello" == "World"
"Hello" != "World"
"Mumbai" > "Pune" #Mumbai comes first in dictionary. Therefore False

#Captial letters occur before lower case letters

#Logical Operations

"" #False
"kdflskf" #True - non-empty string

"" or "world" # True

#Loops

for i in c:
    print(i)

#Membership Operations

'H' in c
'word' not in c

#String functions

#Common functions 
len()
max()#Based on ascii value
min()
sorted()#in ascending and output is list

#Specific functions

c="dsfnsfdlsd"
d= c.capitalize() # Not in place
"it was raining today".title() #Every word is capitalized
c.upper()
c.lower()
c.swapcase()#upper to lower and vice versa
c.count("ing")#count of ing in string
c.find('i') #first index
c.index('i') #same as find but throws error when not present in string
c.endswith('sd')
c.startswith('sd')
"This is {} and i am {}".format("nitesh",30)
"This is {1} and i am {0}".format("nitesh",30)
"This is {age} and i am {name}".format(name="nitesh",age=30)

"falt20".isalnum()#true
"falt20@".isalpha()#false
"20".isdigit()
"hello world".isidentifier()#false

"who is the pm of india".split(" ")#makes list after splitting
"who is the pm of india".split("pm")#makes list after splitting
"".join([1,2,3,4])#makes string after joining

"Hi my name is Nitish".replace("Nitish","Rahul")
"    Rahul   ".strip()

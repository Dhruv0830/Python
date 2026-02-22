#Python print function
print("Hello world")
print("Hello World",'This is the use of separator',sep=',')
print("Hello World",'This is the use of separator',sep='----')
print("Hello World",'This is the use of separator',sep='-', end=',,,,')
print("We should get this string in the next line but we have used end as ,,, . Therefore we get it in same line separated by ,,,")

#Python data types

###Basic types

a =10 #integer (Range - 1e308 : 10 to the power 308)

b =10.43 #float (Range - 1.7e308 : 1.7*10 to the power 308)

flag = True #Boolean 

complex = 1+3j #complex data type

string = 'This is a string data type'

###Container types

list = [1,2,3,4,True,"This is a string"]

tuple = (1,2,3,4)

sets = {1,3,4}

dict = {1:"Python",
        2:"Lecture"}


###Comments in Python

# use hash for single line
# No implementation of multi-line comment in python

#Variables in python

#No variable declaration in python - just name of variable and value

#No need to tell variable type in python - Dynamic typing
#Java - static typing - need to write the data type


#Dynamic Binding - we can easily change the data type of a variable in Python .

a = True
a = "Now we store a string"
a = 10 #Now a integer value

#Opposite is Static Binding - Java

#Special Syntax for variable declaration
a=10;b=20;c=30
#OR
a, b, c = 10, 20, 30
#OR
a=b=c=10

#Python is a case sensitive language
#Keywords - reserved words with special meaning which cannot be used while naming variables
import keyword
print(keyword.kwlist)

#identifiers

#Name of our variable, class, module, function or other object
#Can only start with alphabet or _
#We can use anything other than special characters inside the variable
#Identifiers cannot have the name of any keyword

#Taking user input - The input is always in string format. Therefore we need to convert based on our need.
input("This is a prompt to tell user what to input")

type(6+7j)

#Type conversion 

#Implicit 
4+5.5

#Explicit
int(4.5)
float(2)
str(33)
bool(1)
complex(5)
list('Hello') - [ 'H','e','l','l','o',]

#Type conversion is not a permanent operation we need to save the result in another variable to get the converted value. The original stays the same.

#Literals in Python

#Numeric Literal 

a = 0b1010 #binary
b = 100 #decimal
c = 0o310 #octal
d = 0x12c #hexadecimal

float_1 = 10.5
float_1 = 1.5e2
float_1 = 1.5e-3

complex_1 = 3.14j
print(complex_1.imag, complex_1.real)

#String Literals

string = "This is a Python String"
char = 'c' #This is still treated as a string. Python does not have char data type.
multiline = '''This 
is a multiline
string'''
unicode = u'unicode_string' # Emojis can be stored like this
rawString = r"This is a raw string \n" #We can store html tags in this without converting them to html

#Boolean Literals

a =True+4 #Implicit conversion and a = 5 will be stored.

#Special Literals

a = None #Absence of anything. We want to declare the variable without any value.

#Operators in Python

#Arithmetic Operator:  - , + , / , % , * , // , ** .

#Comparison Operator: > , < , >= , <= , == , != .

#Logical Operator: and , or , not .

#Bitwise Operator: &(binary and) , |(binary or) , <<(right shift) , <<(left shift) , ~ (complement)

#Assignment Operator: a = 3 (= is assignment operator) , += , -= , *= , /= , &= 

#Identity Operator: a is b (Same memory location) , is not

#Membership Operator: D in x , D not in x . X can be string, list, tuple, set and dictionary

##Python does not use a++ and ++a 

#if else elif
#Indentation

#while loop
i = 1
while i<11:
    print(i)
    i+=1

#do while loop - There is no explicit syntax for do while loop in python but we can implement it using the core logic of do while.An example is shown below

#Guessing game
import random
jackpot = random.randint(1,100)

guess = int(input("Guess the jackpot number"))
counter = 1
while guess != jackpot :
    if(guess < jackpot):
        print("Guess Higher")
    else:
        print("Guess Lower")

    guess= int(input("Guess Again"))
    counter+=1

print("You just hit the jackpot")
print("You took ", counter, "attempts")

#For loops

#Range function
list[range(1,11)]
range(5)
range(20, 10, -2)

#Sequence : for iterates over range or sequence

for i in range(1,22,3):
    print(i)

for i in 'String':
    print(i)

for i in [1,2,3,4]:
    print(i)

for i in (1,2,3,4):
    print(i)

#Nested Loops

#Break, Continue, Pass statements

#Break - terminates the loop then and there
#Continue - Skip a paricular iteration
#Pass - Filler code . When we don't have the logic ready then we can fill pass instead of code to avoid error.

#Built in functions in Python

print("This is a built in function")
input("Enter in this built in function")
a = 20
type(a)
#Type conversion function - int(), float(), str()

abs(a)
pow(2,3)
min([1,2,3,4])
max([1,5,7])
min('kolkata') #based on ascii value
round(3.14555,2)
divmod(5,2) #returns the quotient and remainder
bin(44);oct(33);hex(44) #Return the binary, octal and hexadecimal value
id(a) #returns the memory address of the variable
ord(c) #returns the ascii value 
len([1,23,4])
sum([1,2,3,4]) # returns sum of iterable
help('sum') #returns the documentation of the function



#Built in Modules

#It is a python file which can be used in our code for reusability

help('modules')

#Math Random os and time

import math
import random
import os
import time

random.shuffle([1,2,3,44])

time.time() #1st Jan 1970 till now in milliseconds
time.ctime() #Current time 
time.sleep()

os.getcwd()
os.listdir()




















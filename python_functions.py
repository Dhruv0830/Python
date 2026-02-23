#Functions in Python

#def -define 
#function name should be an identifier
#Add a string before the function body to describe the function.
# print(function_name.__doc__) this returns the description of the function we defined in the line above.

#If we save our function file in the lib folder then we can import it just like the random file


#If RAM is city then global frame is your house .
#Function creates its own frame like a room in your house.If no return value then None is returned


#Parameters-when creating a function vs Arguments-when using the function.
#Values of the parameters are the arguments that the user of the function provides.

#Default Arguments
def power(a=1,b=1):
    return a**b

#Positional Arguments
power(2,3) #Then 2 will be a and 3 will be b

#Keyword Arguments
power(b=3,a=2) #Keyword Argument overrides the positional arguments

#Arbitrary Arguments
print(1,2,3,4)#Any number of arguments

def product(*number): # *args
    p=1
    for i in number:
        p*=i
    return p

# Keyword arguments = *kwargs .This store the arugments in a dictionary
def tea_order(customer_name, tea_type, **kwargs):
    for k,v in kwargs.items():
        print(k,":",v)

tea_order("Rahul", "Normal Tea", sugar="None", milk="Oat")

#To use *args and **kwargs simultaneously we need to write args first then kwargs in the function definition.
#function(this,that,*args,**kwargs).This means that we need to use positional arguments before keyword arguments in the function definition and when calling the function.

#When calling the function we can define a dict or a tuple depending on *args or **kwargs and then unpack it while calling it by using *extra_arguments or **extra_dict.

eve_extras = ("almond","sugar", "lemon")
tea_order("eve","green",eve_extras) 

#The number variable is a tuple 

#Local vs Global Scope

#Inside function then local scope of the variable 

#If the function does not have that variable in its scope then it can pick the variable from the global scope

def g(y):
    print(x)
    print(x+1)

x=5
g(x)
print(x)

#This will return 5,6,5 . g(y) uses x from globl scope.

#We can use the global variable but we cannot change it
def h(y):
    x+=1 #This throws error of x referenced before assignment
 
x=5
h(x)
print(x)

#It is possible to change but not advisable
def i(y):
    global x #Now we can change the global variable
    x+=1 
 
x=5
i(x)
print(x)

#If we have nested function then the main program has no idea of the inner function.Therefore , if we call the inner function directly then it will throw an error

#Everything in python is an object and so are functions
def a():
    return a

b=a

del a 
b()#Still works because the del removes the pointer from a to function but b still has that pointer.

#We can also store a function in a list because integers are also objects just like function.

#We can also give a function as an argument and we can also return a function.

def f():
    def x(a,b):
        return a+b
    return x

val = f()(3,4) #Here f() returns another function x which takes 3 and 4 as arguments and returns the final value.

print(val)

#Lamda Functions

#These are anonymous functions which are written in a single line.

x = lambda x : x**2
y = lambda x,y : x+y

#Differences : The return value is the function
#Lambda are single use functions
#Why? We use these with higher order functions : Higher order functions have functions as input or return a function

b= lambda x: "Even" if x%2==0 else "Odd"

#Higher order functions

l = [11,14,21,24,22,33,44,7,55]

def return_sum(func,L):
    result = 0
    for i in L:
        if func(i):
            result+=i
    return result

x = lambda x:x%2==0
y = lambda y:y%2!=0
z = lambda z:z%3==0

print(return_sum(x,l))
print(return_sum(y,l))
print(return_sum(z,l))

#Inbuilt Higher order function

#Map() : lambda function and iterable

this_list = list(map(lambda x:x*2,l))
print(this_list)

#Filter() : 

list(filter(lambda x:x>2,l))

#Reduce() :
import functools

#Reduces our list 
functools.reduce(lambda x,y:x+y,l) #Adds all the items in the list

functools.reduce(lambda x,y:x if x>y else y,l)#Highest Number in the list
functools.reduce(lambda x,y:x if x<y else y,l)#Lowest Number in the list

#List and Dictionary Comprehension

l2 = [x*2 for x in l]

l3 = [x*2 for x in range(10)]

l4 = [x*2 for x in range(1,10,2)]

d1 = {"Name":"Nitish",
      "Age":"30", "Gender":"Male"}

dict.items(d1)

d2 = {key:val for key,val in d1.items() if len(key)>3 }
d3 = {key:key*2 for key in l2 }







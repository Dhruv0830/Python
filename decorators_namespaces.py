#Namespaces are dictionary of identifiers(keys) and their Objects(values)

#1. Builtin Namespace
#2. Global Namespace
#3. Enclosing Namespace
#4. Local Namespace

#Scope is a textual region where a namespace is directly accessible
#LEGB Rule - #4#3#2#1

#The interpreter finds the name in local then enclosing then global then built in scope.

#Local is inside a function.
#Global is everywhere or the global scope.

def add():
    global a
    a = 1 #Creating in local for global scope is possible.
    print(a)

add()

#Parameter of function is a local variable.

#Built in scope
#print(),max(),min() etc these are above global scope and when we run python we get these built in our scope.

#We can change the name of built in scope 
def max():
    print("hello")

#We have overridden the max function which does not need any argument.

#Enclosing Scope
def outer():
    def inner():
        print('inner')
    inner()
    print('outer')

outer()
print('main')

#inner
#outer
#main

#Here inner is local , outer is enclosing or non-local and global is global

def outer():
    a=1
    def inner():
        nonlocal a
        a+=1 #Throws error if nonlocal not mentioned
        print('inner')
    inner()
    print('outer')

outer()
print('main')

#Decorators

#A decorator is a function that receive another function as input and adds some functionality(decoration) to it and it returns it.

#Python functions are first class citizens

def func():
    print('a')

a =func

#A function can be an argument in another function

def my_decorator(func):
    def wrapper():
        print('#######')
        func()
        print('#######')
    return wrapper

def hello():
    print('hello')

a = my_decorator(hello)
a()

#This is called Closure. The decorator function has been removed from the memory after returning the wrapper, but the wrapper still has the func which was passed in the decorator as argument .The control of the program switches again and again during execution.The reference of the parent is still in the heap but has been removed from the call stack

@my_decorator
def hello():
    print('hello') 

#But why 
#A function which prints the execution time of the input function

import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        print('time taken by the',func.__name__,time.time()-start,'secs')
    return wrapper

@timer
def hello2():
    print('hello world')
    time.sleep(4)

#This decorator works on no input functions

def timerNew(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        print('time taken by the',func.__name__,time.time()-start,'secs')
    return wrapper

@timerNew
def hello2():
    print('hello world')
    time.sleep(4)


#A bigger problem

#Checks if the data type for the input function are appropriate or not

#Therefore we need 2 inputs , the function and the input datatype 
def checkDataType(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(*args) == data_type:
                func(*args)
            else:
                raise TypeError("Incorrect Datatype")
            return inner_wrapper
        return outer_wrapper

@checkDataType(int)
def square(num):
    print(num**2)

square(4.5) #Does not work

@checkDataType(str)
def greet(name):
    print('hello',name)

greet(5)#Throws error

#10 fabulous python decorators
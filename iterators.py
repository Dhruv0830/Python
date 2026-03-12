#Itereators and Generators

#Iterator is an object that allows a programmer to traverse through a sequence of data without having to store entire data in memory. It provides a way to access elements of a collection one at a time, which can be useful when working with large datasets or when you want to process data on-the-fly.

x = range(1,10000) #range is an iterable, but not an iterator.

#Iterable is an object that can be iterated over, meaning it can return an iterator. An iterable is any object that implements the __iter__() method, which returns an iterator object. Examples of iterables include lists, tuples, strings, and dictionaries.

#It generates an Iterator when passed to the iter() function.

l = [1,2,3,4,5]

type(iter(l)) #List_iterator

#Every iterator is iterable but every iterable is not an iterator.
#Every iterable has iter function
#Iterators have both iter and next functions.

dir(l) #iter is present or loop can run on list

dir(iter(l)) #iter and next are present-->then iterator

#My own for loop using iterators

def my_for_loop(iterable):
    iterator = iter(iterable)

    while True:
        try:
            element = next(iterator)
            print(element)
        except StopIteration:
            break

num = [1,2,3,4,5]
iter_obj = iter(num)

print(id(iter_obj),"This is iterator object")

iter_obj2 = iter(iter_obj) #iter of iterator is same as iterator

print(id(iter_obj2),"This is iter of iterator object")

#Both ids are same, which means iter of iterator is same as iterator itself. This is a property of iterators in Python. When you call iter() on an iterator, it returns the same iterator object, allowing you to use it in a loop or with the next() function without creating a new object.

#My own range class

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return MyRangeIterator(self)

class MyRangeIterator:
    def __init__(self, iterable_object):
        self.iterable_object = iterable_object
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iterable_object.start < self.iterable_object.end:
            current = self.iterable_object.start
            self.iterable_object.start += 1
            return current
        else:
            raise StopIteration
        
#What's the use ? We can perform lazy evaluation, which means we can generate values on-the-fly without storing the entire sequence in memory. This can be particularly useful when working with large datasets or when you want to process data in a memory-efficient way.


#Generators in Python

#Generators are a special type of iterators that allow you to create iterators in a more concise and memory-efficient way. They are defined using a function that contains one or more yield statements. When the generator function is called, it returns a generator object that can be iterated over.

def gen_demo():
    yield 1
    yield 2
    yield 3

type(gen_demo()) #generator_object
gen = gen_demo()
next(gen) #1
next(gen) #2
next(gen) #3
next(gen) #StopIteration error because generator is exhausted after yielding 3 values.

#Difference between yield and return in a function:
#1. Return statement is used to exit a function and return a value, while yield statement is used to produce a value and pause the function's execution, allowing it to be resumed later.
#2. Return statement terminates the function, while yield statement allows the function to be resumed from where it left off.

def square(num):
    for i in range(1,num+1):
        yield i**2

gen = square(10)

print(next(gen)) #1
print(next(gen)) #2

#Range using generator

def my_range(start, end):
    for i in range(start, end):
        yield i

#Instead of a big class we are able to create range using a simple generator function. This is one of the main advantages of generators: they allow you to create iterators in a more concise and readable way, without the need for defining a separate class.

gen = (i**2 for i in range(1,11)) #Generator expression

for i in gen:
    print(i)

#Keras image data genrator is a powerful tool for loading and preprocessing image data in real-time during model training. It allows you to efficiently feed batches of images to your model without having to load the entire dataset into memory at once. This is particularly useful when working with large datasets that may not fit into memory.

#We can chain generators as well.
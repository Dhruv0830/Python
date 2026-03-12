#File Handling in Python

#Types of data that can be stored in a file:
#1. Text data: This includes plain text, such as letters, numbers, and symbols
#2. Binary data: This includes images, audio files, and other non-text data

#Open , Read , Write , Close

#Text File Handling
f = open("example.txt", "w") #Open a file in write mode
f.write("Hello, World!") #Write data to the file
f.close() #Close the file
# f.write("This will cause an error") #This will cause an error because the file is closed

#Writing multiple lines to a file
f = open('example.txt', 'w')
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
f.writelines(lines) #Write multiple lines to the file
f.write("This is an additional line.\n") #Write another line to the file
f.close()

#Writing to a file which is already present
f = open("example.txt", "w") #Open the file in write mode (this will overwrite the existing content)
f.write("This will overwrite the existing content.") #Write new content to the file
f = open("example.txt", "a") #Open the file in append mode

#Python open function makes a buffer in the RAM when we open a file. When we write to the file, it writes to the buffer first and then flushes it to the disk when we close the file or when the buffer is full. This is why we need to close the file after writing to ensure that all data is written to the disk.

#Reading from a file
f = open("example.txt", "r") #Open the file in read mode
s = f.read() #Read the entire content of the file
print(s) #Print the content of the file
f.close() #Close the file

f = open("example.txt", "r") #Open the file in read mode
s = f.read(10) #Read the first 10 characters of the file
print(s) #Print the content of the file
f.close() #Close the file

f = open("example.txt", "r") #Open the file in read mode
s = f.readline() #Read the first line of the file
print(s, end='') #Print the content of the file
f.close() #Close the file

#When working with big files, it is better to read the file line by line using a loop to avoid memory issues.

f = open("example.txt", "r") #Open the file in read mode
while f.readline() != '': #Read the file line by line until the end of the file
    print(f.readline(), end='') #Print each line of the file
f.close() #Close the file


#Using Context Manager to handle files

#Garbage collector in Python automatically closes the file when it is no longer needed, but it is not recommended to rely on it. It is better to use a context manager (with statement) to ensure that the file is properly closed even if an error occurs.

with open("example.txt", "w") as f: #Open the file using a context manager
    f.write("This is an example of using a context manager to handle files.") #Write data to the file #No need to explicitly close the file, it will be automatically closed when the block is exited


#Reading a file using a context manager
with open("example.txt", "r") as f: #Open the file using a context manager
    s = f.read() #Read the entire content of the file
    print(s) #Print the content of the file

#Moving within the file using seek() and tell()

with open("example.txt", "r") as f: #Open the file using a context manager
    print(f.read(10)) #Read the first 10 characters of the file
    print(f.read(10)) #Read the next 10 characters of the file

with open("example.txt",'r') as fin:
    chunk_size = 100
    while 1:
        s = fin.read(chunk_size)
        if not s:
            break
        print(s)

#Seek and tell methods

with open("example.txt", "r") as f: #Open the file using a context manager
    print(f.tell()) #Print the current position of the file pointer (0 at the beginning)
    print(f.read(10)) #Read the first 10 characters of the file
    print(f.tell()) #Print the current position of the file pointer (10 after reading 10 characters)
    f.seek(0) #Move the file pointer back to the beginning of the file
    print(f.tell()) #Print the current position of the file pointer (0 after seeking to the beginning)

with open("example.txt", "w") as f: #Open the file in write mode using a context manager
    f.write("Hello")
    f.seek(0)
    f.write('X')#This will overwrite the first character of the file with 'X'


#Working with binary files

with open("screenshot.png",'rb') as f: #Open the file in binary read mode
    with open("copy_screenshot.png",'wb') as f2: #Open a new file in binary write mode
        f2.write(f.read()) #Read the content of the original file and write it to the new file

#Working with other data types
with open('sample.txt','w') as f:
    f.write('5') #Write a number as a string to the file

#Whether it is a dict , list or any other data type we need to convert it to string before writing it to a file

#When we retrieve it from the file it will be a string and we need to convert it back to the original data type

#Serialization and deserialization of data using the json module

#Serialization - python data types to JSON format
#Deserialization - JSON format to python data types

import json

l = [1, 2, 3, 4, 5] #A list of numbers
with open('list.json', 'w') as f: #Open a file in write mode using a context manager
    json.dump(l, f) #Serialize the list and write it to the file

dict = {'name': 'Alice', 'age': 30, 'city': 'New York'} #A dictionary
with open('dict.json', 'w') as f: #Open a file in write mode
    json.dump(dict, f, indent=4) #Serialize the dictionary and write it to the file

with open('list.json', 'r') as f: #Open the file in read mode
    l = json.load(f) #Deserialize the content of the file and store it in a variable
    print(l) #Print the deserialized list of type list 

#Tuple serialization and deserialization

#When we dump a tuple it will still give us a list. Therefore we need to manually convert it from a list to a tuple.

#Serializing Custom Objects

class Person:
    def __init__(self,fname,lname,age,gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

    # format to print : fname lname age -> age gender -> gender

#We cannot directly store these objects, we need to define a function describing how to print the object in the file

person = Person("Robin","John",33,"male")

def show_object(person):
    if isinstance(person,Person):
        return "{} {} age -> {} gender -> {}".format(person.fname,person.lname,person.age,person.gender)
    

def show_object_as_dict(person):
    if isinstance(person,Person):
        return {'name':person.fname+' '+person.lname,'age':person.age,'gender':person.gender}

with open('demo.json','w') as f:
    json.dump(person,f,default=show_object)

with open('demo.json','w') as f:
    json.dump(person,f,default=show_object_as_dict,indent=4)

with open('demo.json','r') as f:
    d = json.load(f)
    print(d)
    print(type(d))#Dict

#How to pick our object and use it as it is using pickling

#Pickling

#Converting our Python object hierarchy into a byte stream and unpickling is the inverse whereby a byte stream is converted back to object hierarchy.

#The file where we transfer our object does not have any idea about our class but the object still performs all of its internal operations

import pickle

with open('person.pkl','wb') as f:
    pickle.dump(person,f)


with open('person.pkl','rb') as f:
    p = pickle.load(f)

# p.any_method() This will work 

#Pickle lets user store the data in binary format. JSON lets user store data in human readable text format.

#Therefore if we want to retain the functionality of our object then we use pickle. If we just want text representation then JSON.

#Now if we upload this file to another google colab file we can still use it.This will be cleared in the modules section.

#ML models can be dumped using pickle , therefore it is very important. 



        
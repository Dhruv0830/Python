#Everything is an object in python

# What are objects ? 

#Class is a blueprint - Object is instance of class
#Write the name of the class in Pascal case - ThisIsClass
#Write the names of variables and methods using snake-case - this_is_snake_case

#public method or variable with + : +update
#private method or variable with - : -important_var

#For inbuilt classes we can use object literal - list - instead of using list() , we use [];

#Methods are functions in a class . If class.function() then method otherwise if function(value) then normal function and available to all the variables .

#What is self?
#print(id(self)-address where self is stored === id(object). Therefore object is self itself. The object we work with is self at that instance.)

#Why do we need self with every method?
#This is because one method cannot communicate with another method , even in the same class. Only the object of the class can access all the methods. Therefore we pass the object (using self)in every method so that they can access it.

#ATM class example

class Atm:
    #__init__() is the constructor- Same init name for every class(syntax) - This runs automatically when an object of the class is instantiated(Object is created). 
    # This is a magic method - any method with __ before and after is a magic method(double unders - dunders). They are predefined

    #What is the use of constructor?
    # It cannot be controlled by the user and therefore any configuration related settings like connecting to the database or connecting to the internet is added in the constructor  

    def __init__(self):
        self.pin=''
        self.balance=0

        self.menu()
    
    def menu(self):
        user_input = input('''
                           How would you like to proceed?
                           1. Enter 1 to create PIN
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit
                           ''')
        
        if(user_input =='1'):
            self.pin = input("Please enter new PIN ")
            print("Pin has been set successfully")
            self.menu()

        elif(user_input =='2'): 
            valid_user = self.check_pin()
            if(valid_user):
                deposit = int(input("Please enter the amount to be deposited "))
                self.deposit(deposit)
            else:
                print("Wrong PIN")
                self.menu()
        
        elif(user_input =='3'):
            valid_user = self.check_pin()
            if(valid_user):
                amount = int(input("Please enter the amount to be withdrawn "))
                self.withdraw(amount)
            else:
                print("Wrong PIN")
                self.menu()
        
        elif(user_input =='4'):
            valid_user = self.check_pin()
            if(valid_user):
                print(self.balance)
            else:
                print("Wrong PIN")
                self.menu()
        
        elif(user_input =='5'):
            print("You have successfully logged out")
        else:
            input("Please select a valid menu option")
            self.menu()

    def check_pin(self):
        pin = input("Please enter your PIN.")
        return pin == self.pin
    
    def deposit(self,amount):
        self.balance+= amount
        print("Your updated balance is", self.balance)

    def withdraw(self,amount):
        if(self.balance>=amount):
            self.balance-= amount
            print("Please collect the cash.")
        else:
            print("Insufficient Balance")
            self.menu()

#Creating our own data-type - Fraction

class Fraction:
    def __init__(self,n,m):
        self.num = n
        self.deno = m
    
    #Now if we try to print fraction , python returns us info that fraction is an object but cannot show it as the class definer has not mentioned how to show this data type when printed.For this we need to override the default print function .
    
    #When we call the print function python internally searches for __str__ method (dunder) which tells it how to print it in the console.

    def __str__(self):
        return "{}/{}".format(self.num,self.m)
    
    #Whenever we write + between any 2 object instances of same class ,python looks for the below method to perform the task
    
    def __add__(self,other):
        temp_num = self.num*other.deno + self.deno*other.num
        temp_deno = self.deno*other.deno

        return "{}/{}".format(temp_num, temp_deno)
    
    def __sub__(self,other):
        temp_num = self.num*other.deno - self.deno*other.num
        temp_deno = self.deno*other.deno

        return "{}/{}".format(temp_num, temp_deno)
    
    def __mul__(self,other):
        temp_num = self.num*other.num
        temp_deno = self.deno*other.deno

        return "{}/{}".format(temp_num, temp_deno)
    
    def __truediv__(self,other):
        temp_num = self.num*other.deno
        temp_deno = self.deno*other.num

        return "{}/{}".format(temp_num, temp_deno)
    
#Search magic methods for different classes

#Encapsulation

#What is an instance variable
#The variables in constructor. The value for these is different for all the objects.Ex- PIN, PASSWORD, BALANCE

#Now the object can access all the methods and instance variables in the class. Therefore we use access modifiers like private in java.

#To define we use __before variable name self.__name . Now name is private. Same goes for methods __method_name

#What goes on behind the scenes
#Python saves the private variable using the following format:
# _class_name__variable_name

#Nothing is truly private in python. So, if anyone uses the above syntax and if they know the class and variable name then they can access that "private" variable

#Why? Python is an adult language so the engineers will know what to access and what not to access. And if in the future they need that variable then they can use it using the _class__var format.

#Getter and Setter Methods : we can add logic to ensure a wrong value is not set using these methods

#This is Encapsulation - Hiding our variables but giving access using functions which we can enhance to ensure no incorrect value goes through them.

#For every data member we use getter and setter methods.
#Encapsulate - one data member + 2 methods


#Reference Variable
#Reference of the object is stored in the variable or the variable which we name our object with points to the actual object in the memory.

class Customer():
    def __init__(self,name):
        self.name = name

def greet(customer):
    print(id(customer))

cust = Customer("Rahul")
print(id(cust))

greet(cust)

#Pass By Reference
#We can pass an object using the reference variable as an argument for a function. The working is same as that for integers or floats.This works similar to aliasing.The id in the above case will be same as they are pointing to the same memory location.

#Objects are mutable like lists, dict . When we edit an object using a function we find out that the id does not change , which means it is mutable.

#When we pass by reference in Python, if it is a mutable data type then it will affect the original object and if immutable like a tuple then no changes are seen in the original object.

#Sets can only have immutable elements

#Static Keyword
#Every Object should have a serial number

#A variable where the value is not based on the instance or belongs to the class. Same for all the Objects. Ex- The population of a country remains same for all the people in the population.

#Defined ouside the constructor
class Example:
    __counter =1

    def __init__(self):
        self.id = Example.__counter
        Example.__counter+=1
    
    @staticmethod
    def get_counter():
        return Example.__counter
    
    @staticmethod
    def set_counter(value):
        Example.__counter = value


#We can access the static variable using the class name and also the object name. Ex- Example.__counter and not example1.__counter because it is not an instance variable but a class variable. This is the coding convention but we can access it using the object name as well. Ex- example1.__counter but it is not recommended. We can make it private by using __ before the variable name.

#Static method is a method which is not related to the instance but to the class. It does not take self as an argument. We can call it using the class name and also the object name. Ex- Example.get_counter() or example1.get_counter() but it is recommended to use class name. We can make it private by using __ before the method name.

#Aggregation(has-a) and Inheritance(is-a)

#If one class is using the object of another class then it is called aggregation. Ex- Car has an engine. Engine is a class and Car is a class. Car is using the object of Engine class.

#Diagram for aggregation - Car <>----> Engine

class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
    
    def edit_profile(self,new_name,new_pincode,new_city,new_state):
        self.name = new_name
        self.address.change_adress(new_pincode,new_city,new_state)  


class Address:
    def __init__(self,pincode,city,state):
        self.pincode = pincode
        self.city = city
        self.state = state

    def change_adress(self,pincode,city,state):
        self.pincode = pincode
        self.city = city
        self.state = state

add = Address(110092,"Delhi","Delhi")
cust = Customer("Rahul","Male",add)

cust.edit_profile("Rahul Kumar",110093,"Delhi","Delhi")

#Inheritance - When one class inherits the properties of another class. Ex- Car is a vehicle. Vehicle is a class and Car is a class. Car is inheriting the properties of Vehicle class.

#Inheritance increases code reusability and reduces code redundancy. It also helps in method overriding and polymorphism.

#Superclass cannot inherit from subclass but subclass can inherit from superclass. Ex- Vehicle cannot inherit from Car but Car can inherit from Vehicle.

#Subclass inherits data members and member functions of the superclass along with the constructor of the superclass. We can also add new data members and member functions in the subclass.But private members of the superclass cannot be inherited by the subclass.

class User:
    def login(self):
        print("Logged in successfully")

    def register(self):
        print("Registered successfully")
    
class Student(User):
    def enroll_course(self):
        print("Enrolled in course successfully")
    
    def review_course(self):
        print("Reviewed course successfully")

#Ineritance class diagrm - Student ----> User

#If we don't have a constrcutor in subclass then the parent constructor is called, given that the attribute is not private.

#Polymorphism - Same function name but different implementation. Ex- print() function is used to print different data types like int, str, list etc. It is a built in polymorphic function. We can also create our own polymorphic functions.

#Method Overriding - Same method name but different implementation in the subclass. Ex- If we have a method in the superclass and we want to change its implementation in the subclass then we can override that method in the subclass. When we call that method using the object of the subclass then the overridden method in the subclass will be called.

#Subclass can access the private members sing getter and setter methods.

#If child has own constructor then parent will not be called and the variables inside the parent will not be defined.

#Super Keyword - It is used to call the constructor of the parent class in the child class. It is also used to call the methods of the parent class in the child class. We can use super() to call the constructor of the parent class and then we can add new data members in the child class. We can never accss attributes using super() because it is used to call the constructor of the parent class and not to access the attributes of the parent class. We can only access the attributes of the parent class using self because self is the reference variable which points to the object of the child class and the child class can access all the attributes of the parent class using self. We can also use super() to call the methods of the parent class in the child class.

#Super keyword can only be used inside child class but not outside.

class Phone:
    def __init__(self,price,brand,model):
        self.brand = brand
        self.price = price
        self.model = model

#Calling the parent constructor should be the first line before doing anything else.

class Smartphone(Phone):
    def __init__(self,price,brand,model,ram,os):
        super().__init__(price,brand,model)
        self.ram = ram
        self.os = os

#Types of Inheritance in Python 

#Single Inheritance - When a child class inherits from a single parent class. Ex- Smartphone inherits from Phone.

#Mutlilevel Inheritance - When a child class inherits from a parent class and then another child class inherits from that child class. Ex- If we have another class called Android and it inherits from Smartphone and Smartphone inherits from Phone.

#If a mehtod is in parent and grandparent class and we call that method using the object of the child class then the method of the parent class will be called because it is closer to the child class. If the method is not in the parent class then the method of the grandparent class will be called.

#Hierarchical Inheritance - When multiple child classes inherit from a single parent class. Ex- If we have another class called Laptop and it inherits from Phone and Smartphone inherits from Phone.

#Multiple Inheritance - When a child class inherits from multiple parent classes. Ex- If we have another class called Camera and Smartphone inherits from both Phone and Camera. Not allowed in Java.

#MRO - Method Resolution Order - When there is ambiguity in multiple inheritance then the method of the first parent class will be called. We can also use super() to call the method of the second parent class. The order in which the methods are called is determined by the MRO.

#Hybrid Inheritance - When a child class inherits from multiple parent classes and those parent classes also have their own parent classes. Ex- If we have another class called Tablet and Smartphone inherits from both Phone and Camera and Phone inherits from another class called Device. Not allowed in Java.


#Method Overloading and Operator Overloading

class Geometry:
    def area(self,radius=None):
        return 3.14*radius*radius
    
    def area(self,length=None,breadth=None):
        return length*breadth

obj = Geometry()
obj.area(5) #This will give an error because the second method is overriding the first method and it is expecting 2 arguments but we are passing only 1 argument. This is called method overloading. Python does not support method overloading but we can achieve it using default arguments.

#How to achieve method overloading in Python using default arguments
class Geometry:
    def area(self, a, b=0):
        if b == 0:
            return 3.14*a*a
        else:
            return a*b 
        
#Operator Overloading - When we use the same operator for different data types. Ex- + operator is used for addition of integers and concatenation of strings. We can also create our own operator overloading using magic methods.

#Abstraction - Hiding the implementation details and showing only the functionality to the user. Ex- When we use a mobile phone we only know how to use it but we don't know how it works. We can achieve abstraction using abstract classes in Python.

#Abstract Methods - A method which is declared in the abstract class but does not have any implementation. The subclass which inherits the abstract class must provide the implementation for the abstract method. We can use the abc module to create abstract classes and abstract methods in Python.

from abc import ABC, abstractmethod

class BankApp(ABC): #inherit from ABC to make it an abstract class

    def database(self):
        print("Connected to the database")

    @abstractmethod #decorator to make it an abstract method and no code is written in the abstract method
    def security(self):
        pass

#If we do not provide the implementation for the abstract method in the subclass then we will get an error because the subclass is also considered as an abstract class and we cannot create an object of an abstract class.

class MobileApp(BankApp):
    
    def mobile_login():
        print("Logged in using mobile app")

    def security(self):
        print("Using fingerprint to login")

#Why called abstract method? Because it is not implemented in the abstract class and it is only a declaration of the method. The implementation is provided in the subclass.

#There should be atleast one abstract method in the abstract class. If there is no abstract method then it is not an abstract class and we can create an object of that class. We cannot create an object of an abstract class because it is incomplete and it is only a blueprint for the subclass.

#Every class in python inherits the object class by default. Therefore we can say that object class is the parent class of every class in python. Object class has some built-in methods like __str__, __add__, __sub__, __mul__, __truediv__ etc. which we can override in our class to provide our own implementation for those methods.
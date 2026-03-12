#Exception Handling in Python

#During compilation - sytax error
#Execution - Exceptions

#Error when incorrect grammar. Error raised by interpreter and compiler

#SyntaxError
#IndexError = when index out of bounds
#ModuleNotFoundError = no module of that name
#KeyError = no key with that name
#TypeError = applying function or operator which does not belong to that object 
#ValueError = int('a') when function argument is of incorrect type
#NameError = when object not found
#AttributeError = when the attribute does not belong to that object


#Exceptions - Runtime
#When something unforeseen has happened - logical error during runtime

#Memory Overflow
#Divide by Zero - logical error
#Database error

#Why to handle them?
#We get a message which is called StackTrace(This is the name given to the exception or error message)

#Type of error , message , line number , file name. We need to hide these messages from the user so as to save the user from seeing these messages at the frontend and also safeguard our code from attackers.

#Try-Except block
try:
    with open('example.txt','r') as f:
        print(f.read())
except:
    print('Sorry file not found')

#Catching specific exceptions

try:
    f =open('example.txt','r')
    print(f.read())
    # print(m)
    print(5/2)
    l=[1,2,3]
    l[100]
except FileNotFoundError:
    print("File not found")
except NameError:
    print("Varaible not defined")
except ZeroDivisionError:
    print('Cannot divide by zero')
except Exception as e:
    print(e.with_traceback)#The generic block should be at the end because it can takeover if an exception is thrown and we don't see the actual error

#Else block
try:
    f= open('sample.txt','r')
except FileNotFoundError:
    print("file not found")
except :
    print('Error')
else:
    print(f.read()) #This is triggered when try goes smoothly.And the code here should not crash.This is just good for readability.

#Finally:
  
try:
    f= open('sample.txt','r')
except FileNotFoundError:
    print("file not found")
except :
    print('Error')
else:
    print(f.read())
finally:
    print('Print this after reading the file or excepting the error')#No matter what happens we execute this block. It can be closing a db connection or a socket connection.

#Raise exception or throw error

#We can manually raise exceptions using the raise keyword

# raise NameError #Without message
# raise NameError("just raise this error") 

#Exception is a class and when we catch it using e we are refering to the object e of class exception.

#Why do we need to use this ?
class Bank:
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,amount):
        if amount < 0:
            raise Exception('Amount cannot be negative') #Our own raised exception
        if self.balance<amount:
            raise Exception('Insufficient Balance')
        self.balance-=amount
    
obj = Bank(10000)
try:
    obj.withdraw(50000)
except Exception as e:
    print(e)
else:
    print(obj.balance)

#How to Create Custom Exception
#Why to create our custom class ?
#Beacuse we want full control and application based error can be made using this.

class MyException(Exception):#Always inherit from Exception class
    def __init__(self,message):
        print(message)
            
class Bank:
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,amount):
        if amount < 0:
            raise MyException('Amount cannot be negative') #Our own raised MyException
        if self.balance<amount:
            raise MyException('Insufficient Balance')
        self.balance-=amount
    
obj = Bank(10000)
try:
    obj.withdraw(50000)
except MyException as e:
    print(e)
else:
    print(obj.balance)

class SecurityError(Exception):
    def __init__(self, message):
        print(message)

    def logout(self):
        print('logout of all devices')

class Google:
    def __init__(self,name,email,password,device):
        self.name = name
        self.password = password
        self.email = email
        self.device = device 

    def login(self,email,password,device):
        if device != self.device:
            raise SecurityError('Login device not same as Signup device')
        if email == self.email and password == self.password:
            print('Welcome')
        else:
            print('Login error')

obj2 = Google('Robin','robin@gmail.com','123334','android')

try:
    obj2.login('robin@gmail.com','123334','windows')
except SecurityError as e:
    e.logout()
else:
    print(obj2.name)
finally:
    print('database connection closed')
    

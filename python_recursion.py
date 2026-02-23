#Python recursion
#It uses stacks to store the function calls

#Head recursion and Tail recursion

#Finding if a string is Palindrome or not.
a= 'madam'
b= 'abc'

def palindrome(string):
    if(len(string) == 1 or len(string) == 0):
        return True
    else:
        return string[0]==string[-1] and palindrome(string[1:-1])

print(palindrome(a))
print(palindrome(b))


#Pen and Rabbit example 
#one male and one female
#once every month
#reproduce one month being born
# never die

#This is same as fibonacci

#We use memoization in this case. 
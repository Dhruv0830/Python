# Now I have initialized the git repository and made the first commit.
print("Hello, World!")

#Store frequency in dictionary nums = [1,2,2,3,4,4,4]

frequency = {} # dict()

for num in [1,2,2,3,4,4,4]:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print(frequency)

# This is an intro to hashing and thus we are using dictionary to store frequency of elements in a list.

hashmap = {} # dict()
for num in [1,2,2,3,4,4,4]:
    hashmap[num] = hashmap.get(num, 0) + 1
print(hashmap) 

# get method of dictionary helps to fetch value for a key, if key is not present it returns default value provided as second argument.

# Character frequency in a string s = "azyxyyzaaaa" , q = ["d", "a", "y", "x"]

#ASCII values between 97 to 122 . We make list of size 26 initialized to zero.
char_freq = [0] * 26 # list of size 26 initialized to zero
s = "azyxyyzaaaa"
for char in s:
    index = ord(char) - ord('a') # getting index between 0 to 25
    char_freq[index] += 1
for q_char in ["d", "a", "y", "x"]:
    q_index = ord(q_char) - ord('a')
    print(f"Frequency of {q_char} is {char_freq[q_index]}")

# ord() function gives ASCII value of character
# If we get other special we can use list of size 128 to cover all ASCII characters.

#Factorial of a number n! using recursion

def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)

# 22 Nov 2025
#Reversing string using recursion

def reverse(reversed, string):
    if len(string) == 0:
        return ""
    reverse(string[-1]+ reversed, string[:-1])

#Selection sort algorithm
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Bubble sort algorithm optimized
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break
    return arr

#Insertion Sort 
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr
            
#Merge Sort : Divide and Conquer

#How to sort two sorted arrays

left, right = [1,2,3,4] , [1,1,3,4,5,6,7]
def join_sorted(left,right):
    result =[]
    i = j = 0
    while i < len(left) and j < len(right):
        if(left[i]<right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    if i < len(left):
        result.append(left[i])

    if j < len(right):
        result.append(right[j])


def merge_sort(arr):
    n = len(arr)
    if(n<=1): #If empty array as input
        return arr
    mid = n//2 
    left_arr = arr[:mid] 
    right_arr = arr[mid:]

    left = merge_sort(left_arr) 
    right = merge_sort(right_arr)

    return join_sorted(left,right)

#Time complexity is O(log2(n))(dividing) + O(n+m)(joining) . Therefore total is nlogn.Space complexity is O(n) in stack.

#Pick any item as Pivot and place it at its correct position.
#Inplace sorting
def partition(arr,low,high):
    pivot = arr[low]
    i = low+1
    j = high
    while(i<j):
        while arr[i]<=pivot and i<= high-1:
            i+=1 
        while arr[j]>pivot and j>= low+1:
            j-=1 
        if(i<=j):
            arr[i],arr[j] = arr[j],arr[i]
    arr[low] , arr[j] = arr[j] , pivot
    return j
        
def quick_sort(arr,low,high):
    if low<high:
        p_index = partition(arr,low,high)
        quick_sort(arr,low,p_index-1)
        quick_sort(arr,p_index+1,high)

#Time Complexity(Best and Average): nLogn #Space Complexity:O(1) if we exclude the stack space
#Worst Case T.C.-> O(n^2) When all are same numbers.
new_arr = [12,3,5,4,3,4]
print("This was new array",new_arr)
quick_sort(new_arr,0,5)
print("This is new array now",new_arr)
    



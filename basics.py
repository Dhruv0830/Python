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

# This is an intro to hashing and thus we arre using dictionary to store frequency of elements in a list.

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

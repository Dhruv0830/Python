#Find largest Element in array
nums = [55,32,-97,99,3,67]
# largest = nums[0]
largest = float("-inf")+1
print(largest)
for i in nums:
    if i>largest:
        largest = i
print(largest)

#Find the second largest in array
largest= second_largest = float('-inf')
for i in nums:
    if i > largest:
        second_largest = largest
        largest = i
    if i > second_largest and i != largest:
        second_largest = i

print(second_largest)

#Check if array is sorted
for i in range(1,len(nums)-1):
    if nums[i-1] > nums[i]:
        print(False)
print(True)

#Removing Duplicates from sorted array for length greater than 1.
arr_2 = [1,1,1,2,3,4,4,7,9,9,9,10]
i ,j = 0 , 1 
while j<len(arr_2):
    if(arr_2[i]!=arr_2[j]):
        arr_2[i+1],arr_2[j] = arr_2[j],arr_2[i+1]
        i+=1
    j+=1
print(arr_2)

#Right Rotate the array by k place
k = 5  
#Brute force
for _ in range(0,k%len(nums)):
    e= nums.pop()
    nums.insert(0,e)
    
#T.C. is O(k*n)
rotations = k%len(nums)
nums = nums[len(nums)-rotations:] + nums[:len(nums)-rotations] #This will be a new variable
nums[:] = nums[len(nums)-rotations:] + nums[:len(nums)-rotations] #This will be the same variable
#T.C. is O(n)

#Optimal without slicing

#Reverse the last k elements then then reverse n-k elements then reverse the whole array

def reverse(arr,low,high):
    while(low<high):
        arr[low],arr[high]=arr[high],arr[low]
        low+=1
        high-=1
n = len(nums)
reverse(nums,n-rotations,n-1) # Reverse last k elements
reverse(nums,0,n-rotations-1) # Reverse n-k elements
reverse(nums,0,n-1)   # Reverse the whole array

# T.C. - O(k/2 + n-k/2 + n/2) = O(n)

#Move zeroes to the end . Order remains same for the rest of the elements
new_nums = [1,0,2,4,3,0,0,3,5,1]
i,j=0,1
while(j<len(new_nums)):
    if(new_nums[i]==0 and new_nums[j]!=0):
        new_nums[i],new_nums[j]=new_nums[j],new_nums[i]
        i+=1
    elif(new_nums[i]!=0):
        i+=1
    j+=1
print(new_nums)
    
    
#Merge 2 Sorted arrays duplicates not allowed

nums_1 = [1,1,1,2,4,6,7]
nums_2 = [1,2,3,6,7,8,9,10]

result = []

i = j = 0

while i < len(nums_1) and j <len(nums_2):
    if(nums_1[i]<=nums_2[j]):
        if (len(result)==0 or result[-1] != nums_1[i]):
            result.append(nums_1[i])
        i+=1
    else:
        if (len(result)==0 or result[-1] != nums_2[j]):
            result.append(nums_1[i])
        j+=1

while i<len(nums_1):
    if(len(result)==0 or result[-1]!=nums_1[i]):
        result.append(nums_1[i])
    i+=1   
            
while j<len(nums_2):
    if(len(result)==0 or result[-1]!=nums_2[j]):
        result.append(nums_2[j])
    j+=1
    
#Find the missing number in the array

def missing(arr):
    l = len(arr)
    return l*(l+1)/2 - sum(arr)

#Find max consecutive ones

nums = [1,1,0,1,0,1,1,1,1,0,1,1]
def ones(arr):
    i = 0 
    counter = 0
    max_count = 0
    for i in range(0,len(nums)):
        if nums[i] == 1:
            counter+=1
        else:
            max_count = max(count,max_count)
            count = 0
    return max(count,max_count) #If longest sequence is at the last

#Two Sum Problem

def two_sum(arr,target):
    arr.sort()
    i , j = 0 , len(arr)
    while(i<j):
        if(arr[i]+arr[j]==target):
            return [i,j]

        if(arr[i]+arr[j]>target):
            j-=1
            
        if(arr[i]+arr[j]<target):
            i+=1
    
    return [-1,-1]

#The above solution has TC O(nlogn)

#Now we use dictionary to solve in O(n)

def two_sum_optimal(arr,target):
    hash_map = {}
    for i in range(0,len(arr)):
        remaining = target - arr[i]
        
        if remaining in hash_map:
            return [hash_map[remaining],i]
        
        hash_map[arr[i]] = i  
        
        
#Find the maximum subarray sum 
nums = [-2,1,-3,4,-1,2,1-5,4]

def max_subarray(arr):
    #Kadane Algorithm
    max = float('-inf')
    sum = 0
    for i in range(0,len(arr)):
        sum+= arr[i]
        max = max(sum,max)
        if sum<0:
            sum = 0
    return max

#Best Time to buy sell stock 1
stock = [7,2,1,5,6,4,8]
def buy_sell(arr):
    max_profit = 0
    min_price = float('inf')
    for i in range(len(arr)):
        min_price = min(min_price,arr[i])
        max_profit = max(max_profit,arr[i]-min_price)
    return max_profit
    # best_profit = 0
    # i , j = 0 , 1
    # while j<len(arr):
    #     profit = arr[j]-arr[i]
    #     best_profit = max(best_profit,profit)
        
    #     if profit < 0:
    #         i=j
            
    #     j+=1
    # return best_profit
    
#Rearrange elements by sign
arr= [5,10,-3,-1,-10,6]
# ans= [5,-3,10,-1,6,-10]
def rearrange(nums):
    i,j=0,1
    result = []
    while i<len(nums) and j<len(nums):
        if nums[i]>0 and nums[j]<0:
            result.extend([nums[i],nums[j]])
            i+=1
            j+=1
            
        if nums[i] < 0 :
            i+=1
        
        if nums[j] > 0 :
            j+=1
    return result

#Find the longest consecutive sequence
seq_arr = [1,99,101,98,2,5,3,100,1,1]
def seq(arr):
    my_set = set()
    for i in range(len(arr)):
        my_set.add(nums[i])
    longest = 0
    for num in my_set:
        if num-1 not in my_set:
            x = num
            count = 1
            while x+1 in my_set:
                count+=1
                x+=1
            longest = max(longest,count)
    return longest
#O(3N)

#2D Lists

#Set zeros in the rows and columns containing a zero
  
matrix_1 = [[7,9,2,3],[20,8,0,10],[29,0,-10,5],[4,14,6,7]]

def set_zero(arr):
    r = len(arr)
    c = len(arr[0])
    
    row_track = [0 for _ in range(r)]
    col_track = [0 for _ in range(c)]
    
    for i in range(0,r):
        for j in range(0,c):
            if arr[i][j]==0:
                row_track[i] = -1
                col_track[j] = -1
    
    for i in range(0,r):
        for j in range(0,c):
            if row_track[i] == -1 or col_track[j] == -1:
                arr[i][j] = 0
# TC is O(2*N*M) , SC is O(N+M) 

#Rotate matrix by 90 degree 

matrix_2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def rotate_clockwise_90(arr):
    r = len(arr)
    for i in range(r):
        for j in range(i+1,r):
            arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
    
    for i in range(r):
        arr[i] = arr[i][::-1]
    
rotate_clockwise_90(matrix_2)
print('This is after rotation',matrix_2)

#Print matrix in spiral order

matrix_3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def spiral(arr):
    if not arr or not arr[0]:
        return []
    
    result = []
    top, bottom, left, right= 0, len(arr)-1, 0, len(arr[0])-1 
    
    while top<=bottom and right>=left:
        for i in range(left,right+1):
            result.append(arr[top][i])
        top+=1
        for i in range(top,bottom+1):
            result.append(arr[i][right])
        right-=1
        if top<=bottom:#If the matrix is 1*N
            for i in range(right,left-1,-1):
                result.append(arr[bottom][i])
            bottom-=1 
        if left<=right:#If the matrix is N*1
            for i in range(bottom,top-1,-1):
                result.append(arr[i][left])
            left+=1  
    
    return result

# TC is O(N*M) and SC is O(1) if result matrix not considered

#3Sum Problem

def three_sum(arr,sum):
    arr.sort()
    n = len(arr)
    result = []
    
    for i in range(n):
        if i!=0 and nums[i] == nums[i-1]:
            continue
        
        j=i+1
        k=n-1
        
        while j<k:
            
            while j<k and arr[j] == arr[j+1]:
                    j+=1
                    
            while j<k and arr[k] == arr[k-1]:
                    k-=1
            
            if arr[i]+arr[j]+arr[k] == sum:
                result.append([arr[i],arr[j],arr[k]])
                
            elif arr[i]+arr[j]+arr[k] < sum:
                j+=1
                
            else:
                k-=1
        
    return result
    
# TC is O(nlogn) + O(n**2) and SC is O(No. of Triplets)

#4Sum Problem 

def four_sum(arr, sum):
    arr.sort()
    n = len(arr) 
    result = []
    
    for i in range(n):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and arr[j] == arr[j-1]:
                continue
            k = j + 1
            l = n - 1
            while k < l:
                while k < l and arr[k] == arr[k+1]:
                        k += 1
                        
                while k<l and arr[l] == arr[l-1]:
                        l -= 1
                
                if arr[i] + arr[j] + arr[k] + arr[l] == sum:
                    result.append([arr[i], arr[j], arr[k], arr[l]])
                    
                elif arr[i] + arr[j] + arr[k] + arr[k] < sum:
                    k += 1
                    
                else:
                    l -= 1  
        
        return result
    
# TC is O(n**3) and SC is O(No. of Quadruplets)

#Binary Search

#We can implement it using iteration and recursion 
#TC is O(logn) and SC is O(1)

#Lower Bound : Smallest Index such that nums[i] >= target

nums = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
target = 1

def lower_bound(arr,target):
    low, high = 0, len(arr)-1
    lb = len(arr)
    
    while low<=high:
        mid = low+(high-low)//2
        if arr[mid] >= target:
            lb = mid
            high = mid-1
                      
        else:
            low = mid+1  
            
    return lb        

#Smallest index such that arr[ub] > target

def upper_bound(arr,target):
    low, high = 0, len(arr)-1
    ub = len(arr)
    
    while low<=high:
        mid = low+(high-low)//2
        if arr[mid] >  target:
            ub = mid
            high = mid-1
                      
        else:
            low = mid+1  
            
    return ub        
            
#Using the upper and lower bound we can find the starting and ending point of our target

#Search Insert position

#Array is sorted an all elements are unique

nums_4 = [1,3,4,5,8,9,14,15,19,20,21]
#Return where the index where the target can be inserted
 
def insert_pos(arr,target):
    #This is basically lower bound
    return lower_bound(arr,target)  

  
         
            
                    
         

            
    
        

 
    

    
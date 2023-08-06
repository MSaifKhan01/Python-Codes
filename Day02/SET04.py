import math


#1) 1. **Anagram Check**: Write a Python function that checks whether two given words are anagrams.
   # - *Input*: "cinema", "iceman"
   # - *Output*: "True"
# Anagram Check
# Input: "cinema", "iceman"
str1="cinema"
str2="iceman"
str1=''.join(sorted(list(str1)))
str2=''.join(sorted(list(str2)))
if str1==str2:
    print("Its an anagram")
else:
    print("Not an anagram")



#2) 2. **Bubble Sort**: Implement the bubble sort algorithm in Python.
   # - *Input*: [64, 34, 25, 12, 22, 11, 90]
  #  - *Output*: "[11, 12, 22, 25, 34, 64, 90]"

# Bubble sort
# Input: [64, 34, 25, 12, 22, 11, 90]
list= [64, 34, 25, 12, 22, 11, 90]
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
print(list)

#6) **Missing Number**: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
  #  - *Input*: [3, 0, 1]
  #  - *Output*: "2"
# Missing Number
arr=[3,0,1]
arr=sorted(arr)
for i in range(1,len(arr)):
    if arr[i]-arr[i-1]>1:
        print(arr[i]-1)

#7) 7. **Climbing Stairs**: You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    #- *Input*: 3
    #- *Output*: "3"

# Number of ways
def Number(n):
    if n<0:
        return 0
    if(n==0):
        return 1
    else:
        return Number(n-1)+Number(n-2)
print(Number(3))

#9  **Power of Two**: Given an integer, write a function to determine if it is a power of two.
   # - *Input*: 16
    #- *Output*: "True"

# Power or not
def Power(n):
    product=2
    while(product<n):
        product*=2
    if(product==n):
        return True
    else:
        return False
print(Power(6))

#10) **Contains Duplicate**: Given an array of integers, find if the array contains any duplicates.
    #- *Input*: [1, 2, 3, 1]
    #- *Output*: "True"
# Duplicate in array
def Duplicate(arr):
    obj={}
    for num in arr:
        if num not in obj:
            obj[num]=1
        else:
            return False
    return True
#11) **Binary Search**: Write a function that implements binary search on a sorted array.
   # - *Input*: [1, 2, 3, 4, 5, 6], target = 4
    #- *Output*: "3"
# Binary Search
arr=[1, 2, 3, 4, 5, 6]
k=4
left=0
right=len(arr)-1
while left<=right:
    mid=math.floor((left+right)/2)
    if(arr[mid]==k):
        print(mid)
        break
    elif arr[mid]<k:
        left=mid+1
    else:
        right=mid-1

#15) **Single Number**: Given a non-empty array of integers, every element appears twice except for one. Find that single one.
    #- *Input*: [4,1,2,1,2]
    #- *Output*: "4"        
# Single 
arr=[4,1,2,1,2]
obj={}
for num in arr:
    if num not in obj:
        obj[num]=1
    else:
        obj[num]+=1

for key in obj:
    if obj[key]==1:
        print(key)
        break

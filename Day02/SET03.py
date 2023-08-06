#1)1. **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
    #- *Input*: [("John", 25), ("Jane", 30)]
    #- *Output*: "John is 25 years old. Jane is 30 years old."
people = [("John", 25), ("Jane", 30)]

for person in people:
    name = person[0]
    age = person[1]
    print(f"{name} is {age} years old.")


#2)1. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
    #- *Input*: Add "John": 25, Update "John": 26, Delete "John"
   # - *Output*: "{}, {'John': 26}, {}"

# dictionary manipulation
#  Add "John": 25, Update "John": 26, Delete "John"
def Obj():
    obj={}
    obj["name"]=25
    print(obj)
    obj["name"]=26
    print(obj)
    del obj["name"]
    print(obj)
Obj()


#3)1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
  #  - *Input*: [2, 7, 11, 15], target = 9
  #  - *Output*: "[0, 1]"

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

# Input array and target
nums = [2, 7, 11, 15]
target = 9


result = two_sum(nums, target)

print(result)


#4)1. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
  #  - *Input*: "madam"
   # - *Output*: "The word madam is a palindrome."

def is_palindrome(word):
    word = word.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    length = len(word)
    
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            return False
    return True

# Input word or phrase
input_word = "madam"

# Check if the input is a palindrome
if is_palindrome(input_word):
    print(f"The word {input_word} is a palindrome.")
else:
    print(f"The word {input_word} is not a palindrome.")


 #5)1. **Selection Sort**: Implement the selection sort algorithm in Python.
    #- *Input*: [64, 25, 12, 22, 11]
   # - *Output*: "[11, 12, 22, 25, 64]"
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Input array
arr = [64, 25, 12, 22, 11]

# Apply selection sort
selection_sort(arr)

# Print sorted array
print(arr)



#9) **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
 #   - *Input*: 5, 0
  #  - *Output*: "Cannot divide by zero."

def func(a,b):
    try:
        res=a/b
        return res
    except ZeroDivisionError:
        return "Cannot divide by zero."
print(func(5,0))
   

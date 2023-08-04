1)
people = [("John", 25), ("Jane", 30)]

for person in people:
    name = person[0]
    age = person[1]
    print(f"{name} is {age} years old.")





3)

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


4)

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


 5)
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
   

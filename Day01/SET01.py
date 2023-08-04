##SET-01


1)
 print("Hello, World!")

 2)
# int
int_var = 10

# Float
float_var = 3.14

# String
string_var = "Hello, World!"

# Boolean
bool_var = True

# List
list_var = [1, 2, 3, 4, 5]

# Tuple
tuple_var = (5, 10, 15)

# Dictionary
dict_var = {"name": "Alice", "age": 30, "city": "New York"}

# Set
set_var = {1, 2, 3, 4, 5}

# Printing types and values
print("Type of int_var:", type(int_var), ", value:", int_var)
print("Type of float_var:", type(float_var), ", value:", float_var)
print("Type of string_var:", type(string_var), ", value:", string_var)
print("Type of bool_var:", type(bool_var), ", value:", bool_var)
print("Type of list_var:", type(list_var), ", value:", list_var)
print("Type of tuple_var:", type(tuple_var), ", value:", tuple_var)
print("Type of dict_var:", type(dict_var), ", value:", dict_var)
print("Type of set_var:", type(set_var), ", value:", set_var)


3)

list=[1,2,3,4,5,6,7,8,9,10]

list.append(20)

list.remove(3)

list.sort()

print(list)


4)
list=[10, 20, 30, 40]

sum=sum(list)

average=sum/len(list)

print("Sum: ", sum, "Average: ", average)

5)

def reverse_string(input_string):
    reversed_str = ""
    for i in input_string:
        reversed_str = i + reversed_str
  
    return reversed_str

# Test the function
input_string = "Python"
reversed_string = reverse_string(input_string)
print(reversed_string)

6)

str="Hello"
c=0
for i in str:
    if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        c+=1
        
print( "Number of vowels:", c)

7)
   
def is_prime(number):
    if (number<=1):
        return False
    for i in range(2,number):
        if(number%i==0):
            return False
            
        
    return True


input_number = 13
if is_prime(input_number):
    print(f"{input_number} is a prime number.")
else:
    print(f"{input_number} is not a prime number.")



 8)

 def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        result=1
        
        for i in range(2,n+1):
            result*=i
            
        return result
        

Input=5

output=factorial(Input)
print(output)   

9)

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_num = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_num)
    return fib_sequence

# Test the function
input_n = 5
fib_numbers = fibonacci(input_n)
print(fib_numbers)

10)

squares = [x ** 2 for x in range(1, 11)]
print(squares)





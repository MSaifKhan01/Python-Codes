#- *Input*: [("John", 25), ("Jane", 30)]
#- *Output*: "John is 25 years old. Jane is 30 years old."

Input= [("John", 25), ("Jane", 30)]

for i in Input:
    name=i[0]
    age=i[1]
    print(f"{name} is {age} years old")




from types import Nonetype 
# to print that is enclosed in parentheses
print("Hello World")

#comments (# => hash used to define comments in Python)
#this is a comment

# Datatypes
str2: str = "This is a String"
num: int = 23 #it is a number
floatnum: float = 2.0 # it is a float number
list1: list = [1, 2, 3, 4] # it is an array/List
dict1: dict = {1: "This is dictionary data store in key value pair"}
set1: set = {1, 2, 3, 4} # it is a set
tuple1: tuple = (2, 4, 4, 3) # it is a tuple    
boolt: bool = True or False # truthy or falsy value / 1 or 0
Nonet: None = Nonetype #it is None type
byte_data: bytes = b"Hello" #it is a byte data
byte_array_data: bytearray = bytearray([65, 66, 67])# it is a bytearray or list
complex_num: complex = 3 + 4j #it is a complex number
frozen_set1: frozenset = frozenset([1, 2, 3]) #immutable set
mem_view: memoryview = memoryview(b'Python') #Used for accessing the internal data of an object

#typecasting in python
casted_num: int = int("2") # typecasting in int if str only contains digit
casted_str: list[object] = [str("2"), str([1,2]), str((1,2)), str({1:"dict"}), str({1,2}), str("None")] # and more
casted_float: float = float(3)
casted_dict: dict = dict([(1,2),(2,1)])
casted_tuple: list[object] = [tuple([1,2,3]), tuple("Nishidh"), tuple({1:2, 2:1})] # dict return the key in the form of tuple
casted_list: list[object] = [tuple([1,2,3]), tuple("Nishidh"), tuple({1:2, 2:1})] # dict return the key in the form of tuple

# list and tuple are almost same instead of their types and converts the datatype in the casted datatype

#Operators in Python
#arthemetic Operators
a, b = 10, 3
print(a + b)  # Addition -> 13
print(a - b)  # Subtraction -> 7
print(a * b)  # Multiplication -> 30
print(a / b)  # Division -> 3.333...
print(a // b) # Floor Division -> 3
print(a % b)  # Modulus -> 1 (Remainder)
print(a ** b) # Exponentiation -> 1000

#Comparison/Relational Operators
x, y = 5, 10
print(x == y)  # False (Equal to)
print(x != y)  # True (Not equal to)
print(x > y)   # False (Greater than)
print(x < y)   # True (Less than)
print(x >= 5)  # True (Greater than or equal to)
print(y <= 10) # True (Less than or equal to)

#logical Operators
a, b = True, False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False

#Bitwise Operators
a, b = 5, 3  # Binary: a = 0101, b = 0011
print(a & b)  # AND -> 1
print(a | b)  # OR  -> 7
print(a ^ b)  # XOR -> 6
print(~a)     # NOT -> -6
print(a << 1) # Left Shift -> 10
print(b >> 1) # Right Shift -> 1

#assignment Operators
x = 5
x += 3   # Same as x = x + 3
print(x) # 8
y = 10
y *= 2   # Same as y = y * 2
print(y) # 20

#Identity operators
a = [1, 2, 3]
b = a
print(a is b)   # True (Same object)
print(a is not b) # False (Same object)
x = [1, 2, 3]
print(a is x)   # False (Different objects)

#membership operators
numbers = [1, 2, 3, 4]
print(3 in numbers)    # True
print(5 not in numbers) # True

#ternary Operator => used to right short hand conditional statements
a, b = 10, 20
max_value = a if a > b else b
print("Max value is:", max_value)


#conditional statements in Python
# if elif and else statements , if can be used separately
BOOL_VAL = True
if (BOOL_VAL):
    print("Condition is True")
elif (BOOL_VAL):
    print("Conditon is false")
else:
    print("Conditon is not bool")

#switch case / match case
case_val: str = "Martin"
match(case_val):
    case "Nishidh":
        print("No")
    case "Martin":
        print("Yes")

#loops in Python
# for loop 
for i in range(0,2,1): # 0->start 2-> end 1-> step , end value is exculsive
    print(i)

#while loop
while(True):
    print("the condition is true I work only in true condition")

#for else loop
numbers = [1, 3, 5, 7]
for num in numbers:
    if num % 2 == 0:
        print("Even number found:", num)
        break
else:#it works when all the loop run without any interruption
    print("No even number found")
    
# Use break when you want to stop the loop entirely.
# Use continue when you want to skip certain values but keep looping.


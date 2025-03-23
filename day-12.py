# Day 12 - Polymorphism and String Formatting

# --- POLYMORPHISM ---

# 1. Duck Typing Example
def add(x, y):
    return x + y  # Works for numbers, strings, lists, etc.

print(add(5, 10))      # 15 (int)
print(add("Hello, ", "World!"))  # Hello, World! (str)
print(add([1, 2], [3, 4]))  # [1, 2, 3, 4] (list)

# 2. Function Overloading using *args
def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

print(multiply(2, 3))      # 6
print(multiply(2, 3, 4))   # 24
print(multiply(5))         # 5

# --- STRING FORMATTING ---

name = "Nishidh"
age = 18
pi = 3.14159

# 1. Old-style % Formatting
print("My name is %s and I am %d years old." % (name, age))
print("Pi is approximately %.2f" % pi)

# 2. Using .format()
print("My name is {} and I am {} years old.".format(name, age))
print("Pi is approximately {:.2f}".format(pi))

# 3. Using f-strings (Recommended)
print(f"My name is {name} and I am {age} years old.")
print(f"Pi is approximately {pi:.2f}")

# 4. Alignment in f-strings
print(f"|{'Left':<10}|{'Center':^10}|{'Right':>10}|")

# 5. Using .join() and alignment methods
words = ["Hello", "World"]
print(" ".join(words))  # Hello World
print("Hello".ljust(10, "-"))   # Hello-----
print("Hello".rjust(10, "-"))   # -----Hello
print("Hello".center(10, "-"))  # --Hello---

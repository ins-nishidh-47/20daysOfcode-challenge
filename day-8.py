# Day 8 - Classes, Objects, Inheritance, and Threading in Python

# Classes and Objects Example
class Calculator:
    """A simple calculator class"""
    def __init__(self, a, b):  # Constructor
        self.a = a
        self.b = b

    def __str__(self):  # String representation
        return f"Calculator with values a={self.a} and b={self.b}"

    def __del__(self):  # Destructor
        print(f"Calculator object with values a={self.a} and b={self.b} is deleted")

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Division by zero is not allowed"

    def floor_divide(self):
        if self.b != 0:
            return self.a // self.b
        else:
            return "Floor division by zero is not allowed"

# Inheritance Example
class AdvancedCalculator(Calculator):
    def power(self):
        return self.a ** self.b

    def modulo(self):
        return self.a % self.b

    def is_even(self):
        return "Even" if self.a % 2 == 0 else "Odd"

    def is_prime(self):
        if self.a < 2:
            return False
        for i in range(2, int(self.a ** 0.5) + 1):
            if self.a % i == 0:
                return False
        return True

# Threading Example
import threading
import time

def print_numbers():
    for i in range(1, 11):
        print(f"Number: {i}")
        time.sleep(0.5)

def print_letters():
    for letter in 'ABCDEFGHIJ':
        print(f"Letter: {letter}")
        time.sleep(0.5)

def print_square():
    for i in range(1, 6):
        print(f"Square of {i}: {i**2}")
        time.sleep(0.5)

def print_cube():
    for i in range(1, 6):
        print(f"Cube of {i}: {i**3}")
        time.sleep(0.5)

# Creating Threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
t3 = threading.Thread(target=print_square)
t4 = threading.Thread(target=print_cube)

# Starting Threads
t1.start()
t2.start()
t3.start()
t4.start()

# Ensuring all threads complete before continuing
t1.join()
t2.join()
t3.join()
t4.join()

print("All threads have finished execution.")

# Demonstrating Class and Inheritance Usage
calc = AdvancedCalculator(10, 5)
print("Addition:", calc.add())
print("Subtraction:", calc.subtract())
print("Multiplication:", calc.multiply())
print("Division:", calc.divide())
print("Floor Division:", calc.floor_divide())
print("Power:", calc.power())
print("Modulo:", calc.modulo())
print("Is Even:", calc.is_even())
print("Is Prime:", calc.is_prime())

# Demonstrating Special Methods
print(calc)  # Calls __str__
del calc      # Calls __del__

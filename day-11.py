#timer decorator
import time  # Import time module to measure execution time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record the end time
        print(f"Execution time: {end_time - start_time:.4f} seconds")  # Print elapsed time
        return result
    return wrapper

@timer
def test():
    time.sleep(2)  # Simulate a function that takes time
    print("Function executed!")

test()


# Preserving Function Metadata Using functools.wraps 

import functools

def decorator(func):
    @functools.wraps(func)  # Preserves original function metadata
    def wrapper(*args, **kwargs):
        print("Function is being called...")
        return func(*args, **kwargs)
    return wrapper

@decorator
def example_function():
    """This is an example function."""
    return "Hello, world!"

print(example_function.__name__)  # Output: example_function
print(example_function.__doc__)   # Output: This is an example function.

# Using Decorators for Authentication

# Simulating user authentication
def authenticate(user):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if user == "admin":
                return func(*args, **kwargs)  # Only admins can access
            else:
                return "Access Denied"
        return wrapper
    return decorator

@authenticate("admin")
def secret_data():
    return "This is confidential information."

print(secret_data())  # Output: This is confidential information.

# Class-Based Decorators 

# Creating a decorator using a class
class MyDecorator:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("Function is being called...")
        return self.func(*args, **kwargs)

@MyDecorator
def say_hello():
    return "Hello, World!"

print(say_hello())

#output
# Function is being called...
# Hello, World!


# Decorator
# A simple decorator function
def decorator(func):
    def wrapper():
        print("Before the function runs")  # Code before the function execution
        func()  # Calling the original function
        print("After the function runs")   # Code after the function execution
    return wrapper  # Returning the wrapper function

# Applying the decorator using @ syntax
@decorator
def say_hello():
    print("Hello, World!")

say_hello()  # Calling the function

# 🔹 Decorator with Arguments
# A decorator that wraps a function and adds extra behavior
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is being called...")  # Before function execution
        result = func(*args, **kwargs)  # Calling the original function
        print("Function execution finished!")  # After function execution
        return result  # Returning the function's result
    return wrapper

@decorator
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

print(add(5, 3))  # Output: Function logs + sum result


# 🔹 Stacking Multiple Decorators
# First decorator - Makes text bold
def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"  # Wraps output in <b> tags
    return wrapper

# Second decorator - Makes text italic
def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"  # Wraps output in <i> tags
    return wrapper

# Applying both decorators
@bold
@italic
def text():
    return "Hello, Decorators!"  # Function returns simple text

print(text())  # Output: <b><i>Hello, Decorators!</i></b>

#  Logging Decorator
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} {kwargs}")  # Logs function details
        return func(*args, **kwargs)  # Calls the original function
    return wrapper

@logger
def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

print(multiply(3, 4))  # Output: Function logs + product result

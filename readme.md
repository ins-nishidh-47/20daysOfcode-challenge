## Day 1
> Basic fundamentals and syntax in python to make the person comfortable while coding in python.
### Datatypes in Python <br>
>> str<br>
>> int<br>
>> float<br>
>> list<br>
>> dict<br>
>> set<br>
>> tuple<br>
>> bool<br>
>> None<br>
>> bytes<br>
>> bytearray<br>
>> complex<br>
>> frozenset<br>
>> memoryview<br>
### Typecasting in Python <br>
### Operators in Python <br>
>> arthemetic Operators <br>
>> Comparison/Relational Operators <br>
>> logical Operators <br>
>> Bitwise Operators <br>
>> assignment Operators <br>
>> Identity operators <br>
>> membership operators <br>
>> ternary Operator <br>
### conditional statements <br>
>> If, elseif, else <br>
>> match case <br>
### loops in Python <br>
>> for loop, while loop
>> for else loop
## Day 2
> Will learn how to create functions and the some built-in methods
### what is function ? how to create a function
>> def keyword <br>
>> pass keyword <br>
>> operations with arguments <br>
>> Types of parameters <br>
>> *args, **kwargs <br>
>> assert keyword <br>
### Built-in Methods / Functions
>> default Methods <br>
>> Methods for (string, list, dictionary, sets, tuples)<br>
>> lambda function, filter, reduce <br>
>> Math functions <br>
## Day 3
### Text file handling
>> Methods of Opening file <br>
>> Modes : (a, w, r, a+, r+, w+) <br>
>> Python file Methods <br>
## Day 4
### Binary file handling
>> What is Pickling and unpickling <br>
>> Methods of Opening file <br>
>> Modes : (ab, wb, rb, ab+, rb+, wb+) <br>
>> Pickling file Methods <br>
## Day 5
> Learning how to handle CSV files effectively using Python's `csv` module.
### Writing pip install matplotlibCSV Files
>> **`csv.writer()`** to write list-based data.<br>
>> **`csv.DictWriter()`** to write dictionary-based data.<br>
### Reading CSV Files
>> **`csv.reader()`** to read list-based data.<br>
>> **`csv.DictReader()`** to read dictionary-based data.<br>
### Appending Data to CSV Files
>> Writing additional data without overwriting existing content
### Important Concepts
>> **`newline=''`** for correct file formatting.<br>
>> **Modes:** `w` (write), `a` (append), `r` (read).<br>
### Example Methods Covered
>> Writing CSV files.<br>
>> Reading CSV files.<br>
>> Appending data to CSV files.<br>
>> Writing and reading CSV files using dictionaries.<br>
## Day 6
> Exploring Intermediate Python Concepts <br>
### Exception Handling in Python <br>
>> try, except and finally block <br>
>> ZeroDivisionError, FileNotFoundError <br>
>> Raising Exceptions <br>
### Debugging Basics <br>
>> Using print() for debugging <br>
>> Introduction to Python's pdb module <br>
>> Stepping through code interactively <br>
### Pandas Library (Day1) <br>
>> Data Manipulation with pandas <br>
>> Reading CSV files with pandas.read_csv() <br>
>> Filtering data based on conditions <br>
>> Saving filtered data to new CSV files <br>
### Practical Exercises <br>
>> Handling file operations errors <br>
>> Validating user input with exceptions <br>
>> Debugging code with intentional errors <br>
## Day 7
> Advanced Data Analysis with Pandas (Day 2)
### Data Creation <br>
>> Creating DataFrames using `pd.DataFrame()` <br>
### Data Inspection <br>
>> `.info()` for data overview <br>
>> `.describe()` for statistics <br>
>> `.head()` and `.tail()` for quick data sampling <br>
### Data Cleaning <br>
>> Handling missing values with `.fillna()` <br>
>> Removing duplicates with `.drop_duplicates()` <br>
### Sorting & Indexing <br>
>> Sorting with `.sort_values()` <br>
>> Accessing data with `.loc[]` and `.iloc[]` <br>
### Data Transformation <br>
>> Applying calculations with `.apply()` <br>
### Grouping and Aggregation <br>
>> `.groupby()` for calculating grouped statistics <br>
### Data Merging <br>
>> Using `.merge()` to combine data <br>
### Data Visualization <br>
>> Visualizing data using `.plot()` with Matplotlib integration <br>
### Pivot Tables <br>
>> Creating pivot tables for summarizing data <br>
### Date and Time Handling <br>
>> Using `pd.to_datetime()` for date conversion <br>
### MultiIndexing <br>
>> Setting multi-level indexes with `.set_index()` <br>
### Adding a Calculated Column <br>
>> Creating new calculated columns (e.g., Annual Salary) <br>
### File Handling <br>
>> Saving processed data using `.to_csv()` <br>
## Day 8
> Understanding Object-Oriented Programming concepts like classes, objects, inheritance, and threading in Python.
### Classes and Objects <br>
>> Creating Classes using `class` keyword <br>
>> Defining Constructor (`__init__`) <br>
>> Defining string representation (`__str__`) <br>
>> Defining destructor (`__del__`) <br>
>> Creating Methods for Operations <br>
>> Arithmetic Operations: `add()`, `subtract()`, `multiply()`, `divide()` <br>
>> Additional Methods: `floor_divide()` for integer division <br>
### Inheritance <br>
>> Extending Class Functionality <br>
>> Overriding Methods in Derived Classes <br>
>> Advanced Operations: `power()`, `modulo()` <br>
>> Checking Conditions: `is_even()`, `is_prime()` <br>
### Threading in Python <br>
>> Creating Threads using `threading.Thread` <br>
>> Running Multiple Tasks Concurrently <br>
>> Synchronizing Threads with `.join()` <br>
>> Practical Examples: <br>
>>> Printing Numbers <br>
>>> Printing Letters <br>
>>> Displaying Squares <br>
>>> Displaying Cubes <br>
### Key Concepts Demonstrated <br>
>> Arithmetic Operations with Error Handling <br>
>> Prime Number Checking <br>
>> Multi-threading for Simultaneous Execution <br>
>> Ensuring Efficient Code Execution with Threads <br>
## Day 9
## Concepts
>> Class and Object creation <br>
>> Instance variables and Methods, and Class level attributes <br>
>> Model systems with class inheritance i.e., inherit From Other Classes <br>
>> Parent Classes and Child Classes <br>
>> Extend the functionality of Parent Classes using Child class <br>
>> Object checking <br>
## Day 10
> Understanding Python Decorators and their applications.
### Introduction to Decorators <br>
>> A function that modifies another function without changing its original code. <br>
>> Used for logging, authentication, caching, etc. <br>

### Basic Decorator Syntax <br>
```python
# Defining a simple decorator

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

say_hello()
```
### Output:
```
Before the function runs
Hello, World!
After the function runs
```

### Why Use Decorators? <br>
>> Code reusability <br>
>> Keeps code **clean** and **modular** <br>
>> Useful for logging, authentication, caching, etc. <br>

### Decorator with Arguments <br>
```python
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
    return a + b

print(add(5, 3))  # Output: Function logs + sum result
```
### Output:
```
Function is being called...
Function execution finished!
8
```

### Stacking Multiple Decorators <br>
```python
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
```

### Logging Decorator <br>
> A **logging decorator** can be used to track function calls and parameters. <br>
```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} {kwargs}")  # Logs function details
        return func(*args, **kwargs)  # Calls the original function
    return wrapper

@logger
def multiply(a, b):
    return a * b

print(multiply(3, 4))  # Output: Function logs + product result
```
### Output:
```
Calling multiply with arguments (3, 4) {}
12
```

### Conclusion <br>
> Decorators are a powerful feature in Python that allow you to **modify functions dynamically**. <br>
> They help in keeping code clean, reusable, and structured. <br>
## Day 11
> Advanced Python Decorators and Real-World Applications.


### Import time module to measure execution time
```python
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
```

### Decorators with Return Values <br>
```python
# A decorator that modifies the return value
def double_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2  # Modifies the function output
    return wrapper

@double_result
def get_number():
    return 10

print(get_number())  # Output: 20
```
### Output:
```
20
```

### Preserving Function Metadata Using `functools.wraps` <br>
```python
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
```

### Using Decorators for Authentication <br>
```python
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
```

### Class-Based Decorators <br>
```python
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
```
### Output:
```
Function is being called...
Hello, World!
```

### Conclusion <br>
> Decorators can be used for **logging, modifying return values, authentication, and preserving metadata.** <br>
> They make Python code more modular and maintainable. <br>

## Day 12
> Understanding Polymorphism and String Formatting in Python.

### Polymorphism <br>
>> Duck Typing (Implicit Polymorphism) <br>
>> Function Overloading using `*args` <br>

### String Formatting <br>
>> Old-style (`%` formatting) <br>
>> `.format()` method <br>
>> F-strings (Recommended) <br>
>> Alignment and padding methods (`<`, `>`, `^`) <br>
>> Joining strings using `.join()` <br>
>> Padding methods: `.ljust()`, `.rjust()`, `.center()` <br>

### Execution <br>
>> Run the script using: `python day12_polymorphism.py` <br>




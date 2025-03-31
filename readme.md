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

## Day 13
> Exploring Python's `datetime`, `json`, and `re` modules along with their mathematical methods.

### Datetime Module <br>
>> Getting the current date and time using `datetime.now()` <br>
>> Formatting date and time with `strftime()` <br>
>> Parsing dates using `strptime()` <br>
>> Working with time differences using `timedelta` <br>
>> Getting individual components like year, month, day, hour, minute, second <br>
>> Mathematical methods:<br>
>>> `timestamp()` - Convert datetime to a timestamp <br>
>>> `fromtimestamp()` - Convert timestamp to datetime <br>

### JSON Module <br>
>> Converting Python objects to JSON using `json.dumps()` <br>
>> Parsing JSON to Python objects using `json.loads()` <br>
>> Reading JSON files using `json.load()` <br>
>> Writing JSON to files using `json.dump()` <br>
>> Formatting JSON output with `indent` and `sort_keys` <br>
>> Mathematical methods:<br>
>>> `float()` - Convert numeric values in JSON <br>
>>> `int()` - Convert integers from JSON <br>

### Regular Expressions (re Module) <br>
>> Matching patterns using `re.match()` <br>
>> Searching for patterns using `re.search()` <br>
>> Finding all occurrences using `re.findall()` <br>
>> Replacing text using `re.sub()` <br>
>> Splitting strings using `re.split()` <br>
>> Using special sequences like `\d`, `\w`, `\s` <br>
>> Mathematical methods:<br>
>>> `findall()` - Count occurrences of numeric patterns <br>
>>> `sub()` - Replace numeric values dynamically <br>

# Day 14 - Introduction to Django

## What is Django?
- A high-level Python web framework.
- Encourages rapid development and clean, pragmatic design.
- Follows the **MVT (Model-View-Template)** architecture.

## Installing Django
```bash
pip install django
```
- Verify installation using:
```bash
django-admin --version
```

## Creating a Django Project
```bash
django-admin startproject myproject
```
### Project Structure:
```
myproject/
│── manage.py
│── myproject/
    │── __init__.py
    │── settings.py
    │── urls.py
    │── wsgi.py
```

## Running the Development Server
```bash
cd myproject
python manage.py runserver
```
- Default server runs at `http://127.0.0.1:8000/`

## Creating a Django App
```bash
python manage.py startapp myapp
```
### App Structure:
```
myapp/
│── __init__.py
│── admin.py
│── apps.py
│── models.py
│── tests.py
│── views.py
│── migrations/
```

## Registering the App
- Add `'myapp'` to `INSTALLED_APPS` in `settings.py`.

## Creating a Simple View
```python
# myapp/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
```

## Configuring URLs
```python
# myapp/urls.py
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
```
- Link the app's URLs to the project’s `urls.py`:
```python
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
```

## Running the Application
```bash
python manage.py runserver
```
- Visit `http://127.0.0.1:8000/` to see the output.

## Django Admin Panel
- Create a superuser:
```bash
python manage.py createsuperuser
```
- Login at `http://127.0.0.1:8000/admin/`.

## created home.html in templates for fronted
- render it in views.py 
```
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

```

## Day 15
> Diving deeper into Django by exploring applications, models, migrations, and the admin panel.

### Creating a Django App <br>
>> `python manage.py startapp myapp` <br>
>> Register the app in `INSTALLED_APPS` in `settings.py` <br>

### Understanding Models in Django <br>
>> What are models? <br>
>> Creating models using `models.Model` <br>
>> Defining fields: `CharField`, `IntegerField`, `DateTimeField`, `BooleanField`, etc. <br>
>> Adding `__str__` method for readable representation <br>

### Migrations in Django <br>
>> What are migrations? <br>
>> Creating migrations using `python manage.py makemigrations` <br>
>> Applying migrations using `python manage.py migrate` <br>
>> Checking migration history <br>

### Django Admin Panel <br>
>> Creating a superuser using `python manage.py createsuperuser` <br>
>> Registering models in `admin.py` <br>
>> Exploring the Django admin interface <br>
>> Customizing the admin panel <br>

### Querying the Database Using ORM <br>
>> `Model.objects.all()` - Fetching all records <br>
>> `Model.objects.filter()` - Filtering records <br>
>> `Model.objects.get()` - Getting a single record <br>
>> `Model.objects.create()` - Creating new records <br>
>> `Model.objects.update()` - Updating existing records <br>
>> `Model.objects.delete()` - Deleting records <br>

### Practical Exercises <br>
>> Creating a simple model for a blog post <br>
>> Performing CRUD operations using Django ORM <br>
>> Exploring Django shell (`python manage.py shell`) <br>

# Day 16 - SQLite Migrations: Insert, Update, and Delete

## Overview
On Day 3 of learning Django, we focused on **adding, updating, and deleting records** in SQLite using Django migrations. Below are step-by-step instructions on performing these operations efficiently.

---

## 1️⃣ Adding a Record

### **Model Definition**
Define a model in `models.py`:

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
```

### **Run Migrations**
```sh
python manage.py makemigrations
python manage.py migrate
```

### **Insert Data using Django Shell**
```sh
python manage.py shell
```
Then, execute:
```python
from myapp.models import Student
student = Student(name="John Doe", age=20, email="johndoe@example.com")
student.save()
```

---

## 2️⃣ Updating a Record

### **Update a Record using Django Shell**
```python
student = Student.objects.get(id=1)  # Fetch student by ID
student.age = 21  # Modify age
student.save()  # Save changes
```

### **Update a Record using Views**
```python
from django.shortcuts import

#Day-17 - Django Student Management System

This is a simple Django project to manage student records. It allows users to add, update, delete, and list student records using an SQLite database.

## Features
- Add new students
- Update student records
- Delete students
- List all students

## Installation

### Prerequisites
Make sure you have Python installed (recommended version: 3.x) and Django set up.

### Clone the Repository
```bash
git clone <repository-url>
cd <project-directory>
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Migrations
```bash
python manage.py migrate
```

### Start the Server
```bash
python manage.py runserver
```

## Usage
- Open `http://127.0.0.1:8000/` in your browser.
- Use the interface to manage student records.

## Project Structure
```
project-directory/
│── manage.py
│── db.sqlite3
│── requirements.txt
│── students/
│   ├── migrations/
│   ├── templates/
│   │   ├── add_student.html
│   │   ├── update_student.html
│   │   ├── delete_student.html
│   │   ├── student_list.html
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   ├── forms.py
│── templates/
│── static/
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.

# Django Template Concepts (Day 18)

This repository provides an in-depth demonstration of various Django template concepts, helping you understand how templates work in Django applications.

✅ Django Variables  
✅ Django Tags  
✅ Django If-Else  
✅ Django For Loop  
✅ Django Comment  
✅ Django Include  

## 📌 Project Setup

### 1️⃣ Create a Django Project and App
```bash
django-admin startproject myproject
cd myproject
python manage.py startapp myapp

```
# Day 19: Handling 404 Page in Django

## 📌 Overview
how to create a custom **404 Page Not Found** error page in Django. Instead of displaying Django’s default error page, we designed a user-friendly 404 page with custom styling.

---

## 📂 Project Structure
```
myproject/
│── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│── myapp/
│   ├── __init__.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── home.html
│   │   ├── 404.html
│── manage.py
```

---

## 🛠️ Steps to Implement Custom 404 Page

### 1️⃣ **Create a Custom 404 Template**
Inside your Django app, create a `templates` folder and add a `404.html` file:

#### `myapp/templates/404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to bottom, #f8f9fa, #e9ecef);
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            margin: 0;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            max-width: 500px;
            width: 100%;
        }
        h1 { font-size: 60px; color: #333; }
        h2 { font-size: 24px; color: #555; margin-bottom: 10px; }
        p { font-size: 16px; color: #777; margin-bottom: 20px; }
        .buttons { display: flex; justify-content: center; gap: 10px; }
        .btn {
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 8px;
            font-size: 16px;
            transition: 0.3s;
        }
        .btn-back { background: #ddd; color: #333; border: 1px solid #ccc; }
        .btn-home { background: #007bff; color: white; border: none; }
        .btn:hover { opacity: 0.8; }
    </style>
</head>
<body>
    <div class="container">
        <h1>404</h1>
        <h2>Page Not Found</h2>
        <p>Oops! The page you are looking for has moved or doesn't exist.</p>
        <div class="buttons">
            <a href="javascript:history.back()" class="btn btn-back">Go Back</a>
            <a href="/" class="btn btn-home">Back to Home</a>
        </div>
    </div>
</body>
</html>
```

### 2️⃣ **Create a Custom 404 View**
In `myapp/views.py`, add a function to handle 404 errors:
```python
from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
```

### 3️⃣ **Register the 404 Handler**
In `myproject/urls.py`, add this line at the bottom:
```python
from myapp.views import custom_404_view
from django.conf.urls import handler404

handler404 = custom_404_view
```

### 4️⃣ **Update `settings.py`**
Ensure `DEBUG = False` and allow all hosts (only for testing, change it in production):
```python
DEBUG = False  # Set to False in production
ALLOWED_HOSTS = ['*']  # Replace '*' with your domain in production
```

---

## 🚀 Running the Project
```sh
python manage.py runserver
```
- Visit **http://127.0.0.1:8000/** → Home Page ✅
- Visit **http://127.0.0.1:8000/non-existent/** → Custom 404 Page ✅

---

## 🎯 Summary
✅ Created a **custom 404 template**
✅ Added a **view function** to handle 404 errors
✅ Configured **Django to use the custom 404 page**

Now, when users enter a wrong URL, they will see your **beautiful 404 page instead of Django's default error page!** 🎉

# Day 20: Django Weather App 🌦️

## Final Day of My 20-Day Python Coding Sprint! 🎉

Wrapping up this epic streak with a sleek **Django Weather App** powered by the **OpenWeather API**! 🚀

### Features:
✅ Fetches real-time weather data ☀️🌧️❄️
✅ Uses **Django + SQLite3** for backend storage 📊
✅ Implements **CRUD operations** (Create, Read, Update, Delete) efficiently 💡
✅ Seamless UI for searching and displaying weather information 🎨

### Tech Stack:
- **Python** 🐍
- **Django** 🌍
- **SQLite3** 🗄️
- **OpenWeather API** 🌍
- **HTML/CSS** 🎨

### What I Learned:
🔹 Mastered **Django models, views, templates, and forms**
🔹 Strengthened **CRUD operations (GET, POST, DELETE, UPDATE)**
🔹 Worked with **external APIs** for fetching live data
🔹 Improved **frontend-backend integration**


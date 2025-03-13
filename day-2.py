
#Function
def this_is_a_function()-> str:
    return "this is a function"

#To define function we use def keyword 
def function_name()-> str:
    return "By this we can define a function"

#pass keyword -> (used to define a function without any issue )Placeholder for an empty function
def _for_future()-> None:
    pass

#operations with arguments with function
def add(a: int,b: int)-> int:
    return a+b
print(add(20,20))

def greet(name: str, age: int)-> None:
    print(f"Hello {name}, your age is {age}")

#passing arguments inside a funciton

#formal parameters
def greet(name, age):  # 'name' and 'age' are **formal parameters**
    print(f"{name} is {age} years old.")

#actual parameters => arguments passed during function call
greet("Nishidh", 18)  # "Nishidh" and 18 are **actual parameters**

#positional arguments -> (the arguments should be passed with the same order)
def body_t(name: str, bodycount: int)-> str:
    return f"Hello {name}, your bodycount is {bodycount}"

print(body_t(2, "Hardick")) #correct order  
print(body_t("Hardick", 2)) # wrong order

#default arguments
def chk_default(name: str = "Martin")-> str:
    return name

print(chk_default("Virushka")) #It will assign this value to name
print(chk_default()) # it will return the default arg

#keyword arguments -> (order not matter here, if there are only keyword arg)
def chk_key_arg(book: str, price: int)-> str:
    return f"For {book}, price is {price}"

#Both are correct
print(chk_key_arg(book="Deathnote", price=299))
print(chk_key_arg(price=230, book="Deathnote"))
# only use it like this when there is no such arg and you are only passing the keyword arg

# Variable-Length Arguments (*args)
def args(*args)-> None: # -> pass as many arguments, param in the form of tuple
    print(sum(args))
    
args(1,2,3,4,5) #15

# Keyword-Only Arguments (**kwargs)
def kwargs(**kwargs)-> None:# -> pass as many keyword arguments, param in the form of dictionary
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
kwargs(name="Rihit", age=18, language="python")

#Position only arguments => positional arg cannot appear after keyword arguments
def meet(name, /, age):
    print(f"{name} is {age} years old.")
# Arguments before / must be passed positionally.
meet("Nishidh", 18)       # Correct
meet(name="Nishidh", 18)  # Error

# * keyword only
def meet_2(*, name, age):
    print(f"{name} is {age} years old.")
# Arguments after * must be passed as keywords.
meet_2(name="Nishidh", age=18)  # Correct
meet_2("Nishidh", 18)           # Error

#assert keyword -> checks the condition fullfills or not
def calculate_area(radius):
    assert radius > 0, "Radius must be positive"
    return 3.14 * radius ** 2


# Built-in Methods

#default Methods
def default_functions():
    return {
        "len": len("Hello"),  # Returns the length of the string
        "type": type(123),  # Returns the type of the object
        "id": id("sample"),  # Returns the identity of the object
        "repr": repr("Hello"),  # Returns a string representation of the object
        "callable": callable(print),  # Checks if an object is callable
        "sorted": sorted([5, 2, 9, 1]),  # Sorts a list
        "min": min([1, 5, 2, 9]),  # Returns the smallest item in an iterable
        "max": max([1, 5, 2, 9]),  # Returns the largest item in an iterable
        "sum": sum([1, 2, 3]),  # Returns the sum of all items in an iterable
        "all": all([True, False, True]),  # Checks if all elements are true
        "any": any([True, False, False]),  # Checks if any element is true
        "abs": abs(-7),  # Absolute value of a number
        "enumerate": list(enumerate(["apple", "banana", "cherry"])),  # Adds index to iterable
        "zip": list(zip([1, 2, 3], ["a", "b", "c"])),  # Zips two iterables together
        "filter": list(filter(lambda x: x > 2, [1, 2, 3, 4])),  # Filters elements based on condition
        "map": list(map(lambda x: x * 2, [1, 2, 3])),  # Applies a function to all items
        "range": list(range(1, 6)),  # Generates a sequence of numbers
        "chr": chr(97),  # Converts an ASCII code to a character
        "ord": ord('a'),  # Converts a character to its ASCII code
        "reversed": list(reversed([1, 2, 3])),  # Reverses an iterable
        "isinstance": isinstance(123, int),  # Checks if an object is an instance of a class
        "round": round(3.14159, 2),  # Rounds a number to a given precision
        "divmod": divmod(10, 3),  # Returns a tuple of (quotient, remainder)
        "eval": eval("2 + 3"),  # Evaluates a string as Python code
        "exec": exec('a = 5; print(a)'),  # Executes dynamically created Python code
        "format": "Hello, {}!".format("World"),  # String formatting using .format()
        "hex": hex(255),  # Returns the hexadecimal representation of a number
        "oct": oct(8),  # Returns the octal representation of a number
    }

#Methods for string
def string_methods(s):
    return {
        "lower": s.lower(), # make the characters in lowercase
        "upper": s.upper(), # make the characters in lowercase
        "title": s.title(), # capitalize all the words first character
        "capitalize": s.capitalize(),# capitalize the first character only
        "replace": s.replace("hello", "hi"), # replace the hello with hi in the string
        "split": s.split(), # make the fragments of the string
        "strip": s.strip(), # remove all the whitespaces from left and right
        "find": s.find("e"),# gives the index of first occurence of e
        "count": s.count("l"), # gives the number of occurence of l
        "startswith": s.startswith("H"), # returns true if the str starts with H
        "endswith": s.endswith("o"), # returns true if the str ends with H
        "isalpha": s.isalpha(), # returns true if there are only characters
        "isdigit": s.isdigit(), # returns true if there are only digits
        "isnumeric": s.isnumeric(), # returns true if there are only digits/num
        "isspace": s.isspace(), # returns true if the str only contains space
    }
    
 # Methods for lists
def list_methods(lst):
    return {
        "append": lst.append(4),  # Adds 4 to the list
        "extend": lst.extend([5, 6]),  # Adds multiple elements
        "insert": lst.insert(1, 10),  # Inserts 10 at index 1
        "remove": lst.remove(10),  # Removes the first occurrence of 10
        "pop": lst.pop(),  # Removes the last item
        "clear": lst.clear(),  # Clears the entire list
        "index": lst.index(2),  # Returns the index of first occurrence of 2
        "count": lst.count(1),  # Counts how many times 1 occurs
        "sort": lst.sort(),  # Sorts the list in ascending order
        "reverse": lst.reverse(),  # Reverses the list
        "copy": lst.copy(),  # Creates a shallow copy of the list
        "join": ', '.join(map(str, lst)),  # Joins list elements into a string
    }
    
#Methods for dictionary
def dictionary_methods(d):
    return {
        "get": d.get("key1", "Not Found"),  # Returns value for 'key1'
        "keys": list(d.keys()),  # Returns all keys
        "values": list(d.values()),  # Returns all values
        "items": list(d.items()),  # Returns a list of key-value pairs
        "update": d.update({"key3": "value3"}),  # Adds a new key-value pair
        "pop": d.pop("key1", "Key not found"),  # Removes key 'key1'
        "popitem": d.popitem(),  # Removes the last key-value pair
        "clear": d.clear(),  # Clears the entire dictionary
        "setdefault": d.setdefault("key4", "default_value"),  # Sets default value
    }

#Methods for sets
def set_methods(s):
    return {
        "add": s.add(4),  # Adds 4 to the set
        "remove": s.remove(4),  # Removes 4 from the set
        "discard": s.discard(5),  # Discards 5 from the set without error
        "pop": s.pop(),  # Removes a random element
        "clear": s.clear(),  # Clears the set
        "union": s.union({1, 2, 3}),  # Returns a set with elements from both sets
        "intersection": s.intersection({2, 3, 4}),  # Returns common elements
        "difference": s.difference({1, 2}),  # Returns elements in s but not in {1, 2}
        "issubset": s.issubset({1, 2, 3, 4}),  # Checks if s is a subset
        "issuperset": s.issuperset({2, 3}),  # Checks if s is a superset
        "copy": s.copy(),  # Creates a shallow copy of the set
    }
    
# Methods for tuples
def tuple_methods(t):
    return {
        "count": t.count(2),  # Counts occurrences of 2
        "index": t.index(3),  # Returns the index of first occurrence of 3
    }

# lambda function , filter function and reduce function    
def function_methods():
    lst = [1, 2, 3, 4, 5]

    # Using map to apply a function to each item
    doubled = list(map(lambda x: x * 2, lst))

    # Using filter to filter out odd numbers
    even = list(filter(lambda x: x % 2 == 0, lst))

    # Using reduce to accumulate results (requires functools)
    from functools import reduce
    sum_all = reduce(lambda x, y: x + y, lst)

    return {
        "map": doubled,
        "filter": even,
        "reduce": sum_all,
    }
    
# Math Functions
import math
def math_methods():
    return {
        "abs": abs(-7),  # Absolute value
        "pow": pow(2, 3),  # 2 raised to the power of 3
        "sqrt": math.sqrt(16),  # Square root of 16
        "max": max([1, 5, 2, 9]),  # Maximum value
        "min": min([1, 5, 2, 9]),  # Minimum value
        "round": round(3.14159, 2),  # Rounds to 2 decimal places
        "factorial": math.factorial(5),  # 5!
    }

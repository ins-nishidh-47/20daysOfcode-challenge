
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

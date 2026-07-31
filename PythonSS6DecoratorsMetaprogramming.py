# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Start small. Ship something.")
#decorators 
# a function that takes another function adds extra behaviour to it and return its new function
def func():
    return "hello"
    
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before func call")
        res = func(*args, **kwargs)
        print("After func call")
        return res
    return wrapper
    
@my_decorator    
def say_hello():
    print("Hello")
    
# decorated_function = my_decorator(say_hello)

# decorated_function()

say_hello()

@my_decorator
def add(a, b):
    return a + b
    
# can't direct ly use this func using my decorator as it is taking parameters as arguments    
print(add(10, 20))

#Logging 
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Before func call :  {func.__name__}")
        res = func(*args, **kwargs)
        print(f"After func call :  {func.__name__}")
        return res
    return wrapper
    
@log_function
def add2(a, b):
    return a + b
    
print(add2(20, 30))

print("Timer Decorator")
#Timing decorator

import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds")
        return res
    return wrapper
    
    
@timer
def slow_function():
    # time.sleep(2)
    print("done")
    
slow_function()

#functools.wraps
from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
    
@my_decorator    
def greet():
    """It greets the user"""
    print("Hello")
    
# it remembers the docstrings as well
print(greet.__name__)
print(greet.__doc__)

#Class Decorator # less common
# a function that takes a class, modifies it and returns it

def add_greeting(cls):
    cls.greet = lambda self: "hello from decorated class"
    return cls
    
@add_greeting    
class Student:
    def __init__(self, name):
        self.name = name

        
student = Student("Soham")
print(student.name)
print(student.greet())


# Introspection > means inspecting objects at runtime
# Python allows us to check what attributes and methods an object has
class Student:
    school = "algoschool"
    def __init__(self, name):
        self.name = name
        
    def introduce(self):
        print(f"My name is {self.name}")
        
student = Student("soham")
print(dir(student))
print(getattr(student, "name" ))
print(getattr(student, "age", "Age not found"));
setattr(student, "age", 25)
print(student.age)
print(dir(student))

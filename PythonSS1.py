# global keyword is used when we want to modify a global variable inside a function

from ast import Lambda


count = 0

def increment():
    global count
    count += 1

increment()
print(count)


#nonlocal keyword is used in nested functions to modify a variable in the nearest enclosing scope that is not global.

def outer():
    count = 2

    def inner():
        nonlocal count
        count += 1
        print("Inner count:", count)

    # calling inner function from outer function
    inner()

outer()
print("Outer count:", count)  # This will print the global count, which is still 1

#Lambda Expressions -> small anonymous function used for short one line functions
# syntax : lambda arguments : expression

square = lambda x: x**2
print(square(5))  # Output: 25

add = lambda a, b : a + b
print(add(3, 4))  # Output: 7

is_Even = lambda x : x % 2 == 0
print(is_Even(4))  # Output: True

to_Upper = lambda s : s.upper()
print(to_Upper("hello"))  # Output: HELLO   


# DocStrings -> used to document a function, class or module. usually written intriple quotes and is the first statement in a function, class or module.

def greet(name):
    """This function greets the person with the given name."""
    return f"Hello, {name}!"


# Type Annotations -> used to indicate the expected data types of function parameters and return values. It helps in code readability and can be used by static type checkers.
#  describe the expected input and output types of a function. It does not enforce type checking at runtime, but it serves as documentation for developers and can be used by static type checkers.

def add_numbers(a: int, b: int) -> int:
    """This function adds two numbers and returns the result."""
    return a + b
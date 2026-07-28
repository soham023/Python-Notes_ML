# Type Hints

# Type hints are a feature in Python that allows you to specify the expected data types of function parameters and return values. 
# They provide additional information to developers and can be used by static type checkers to catch potential type-related errors before runtime. 
# Type hints do not enforce type checking at runtime, but they serve as documentation for developers and can improve code readability.

# Python is still dynamically typed, meaning that you can still pass values of different types to functions, and Python will not raise an error. 
# However, using type hints can help developers understand the intended usage of functions and improve code quality.


def greet(name: str) -> str:
    # name: str indicates that the parameter name is expected to be of type str.
    # -> str indicates that the function is expected to return a value of type str.
    return f"Hello, {name}!"

message = greet("Alice")

print(message)  # Output: Hello, Alice!

name : str = "Bob"
age : int = 30
height : float = 5.9

marks : int = "nine"  # This will not raise an error at runtime, but it is a type mismatch according to the type hint.

print(marks)  # Output: nine


# the typing module
# provides many useful types for writing type hints, such as List, Dict, Tuple, Optional, Union, and more.

from typing import List, Dict, Tuple, Optional, Union, TypedDict, Any, NamedTuple


# Generics : list[T] 

# Generics allows us to mention what type of data a collection contains

numbers: list[int] = [1, 2, 3, 4, 5]
names: list[str] = ["Alice", "Bob", "Charlie"]

def total(numbers : list[int]) -> int:
    return sum(numbers)

# Generics: dict[K, V]
student : dict[str, int] = {
    "math": 85,
    "science": 90
}

print(student)  # Output: {'math': 85, 'science': 90}
def print_student_scores(scores: dict[str, int]) -> None:
    for subject, score in scores.items():
        print(f"{subject}: {score}")

coordinates: tuple[int, int] = (10, 20)
unique_numbers: set[int] = {1, 2, 3, 4, 5, 2}


# optional is used to indicate that a value can be of a specific type or None.
# It is often used for function parameters that may or may not be provided.

from typing import Optional

def find_user(user_id : int) -> Optional[str]:
    if user_id == 1:
        return "Alice"
    return None

# modern way
def find_user(user_id: int) -> str | None:
    if user_id == 1:
        return "Alice"
    return None

# Union is used to indicate that a value can be of multiple types.
from typing import Union

def format_id(user_id: Union[int, str]) -> str:
    return f"User ID: {user_id}"
# modern way
def format_id(user_id: int | str) -> str:
    return f"User ID: {user_id}"



# Any is used to indicate that a value can be of any type.
# It is often used when the type of a value is not known or can vary.

from typing import Any

def print_value(value: Any) -> None:
    print(f"Value: {value}")

data: Any = {"name": "Alice", "age": 30}
data2: Any = [1, 2, 3, 4, 5]
data3: Any = "Hello, World!"
data4: Any = True


# TypedDict is used to define the expected structure of a dictionary

from typing import TypedDict

class Student (TypedDict) :
    name : str
    age : int
    course : str

student: Student = {
    "name" : "Riya",
    "age" : 25,
    "course" : "python"
}


def print_student( student : Student ) -> None:
    print(student["name"])
    print(student["course"])

print_student(student)

# protocol 
# used to define expected behaviour instead of exact class inheritance

from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None:
        ...

class Circle:
    def draw(self) -> None:
        print("Drawing circle")

class Square:
    def draw(self) -> None:
        print("Drawing Square")

def render(shape: Drawable) -> None:
    shape.draw()


render(Circle())

render(Square())

# HEre Circle and Square , they do not inherit really from Drawable still match the protocol who have a raw method
# Flexible


#Static Type Checking
# means type errors before running the program

# myPy and pylan -> internal tools for static type checking as python itself is not strictly type checking language

def add(a : int, b: int ) -> int:
    return a + b


print(add("10", "20"))


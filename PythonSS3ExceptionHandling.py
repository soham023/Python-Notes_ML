# Exception
# Exception is an event that occurs during the execution of a program that disrupts the normal flow of the program's instructions.
# if they are not handled properly, they can cause the program to crash or produce unexpected results.

num = int('abc') # throws ValueError: invalid literal for int() with base 10: 'abc'

# ValueError: invalid literal for int() with base 10: 'abc'
# FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file.txt'
# IndexError: list index out of range
# KeyError: 'non_existent_key'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# ZeroDivisionError: division by zero

# TraceBack: A traceback is a report that provides information about the sequence of function calls that led to an exception being raised. It shows the file name, line number, and function name where the exception occurred, as well as the call stack leading up to that point.
#  it shows where the error happened and what type of error occurred.

def divide(a, b):
    return a / b

divide(10, 0)  # This will raise a ZeroDivisionError

try:
    divide(10, 0)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input.")
else:
    print("Division successful.")
finally:
    print("Always executed.")


#  Broad Exception Handling: Catching all exceptions using a generic except block. It is generally not recommended to catch all exceptions, as it can hide bugs and make debugging difficult. Instead, it's better to catch specific exceptions that you expect might occur.
try:
    divide(10, 0)          
except Exception as e:  # Catching all exceptions
    print(f"An error occurred: {e}")


#  raise statement: The raise statement is used to manually raise an exception in Python. It allows you to create custom exceptions or re-raise existing exceptions. You can raise built-in exceptions or define your own exception classes.
def check_positive(num):    
    if num < 0:
        raise ValueError("Number must be positive.")
    return num

# Custom Exception Classes: You can create your own exception classes by inheriting from the built-in Exception class. This allows you to define specific types of exceptions for your application.
class CustomError(Exception):   
    pass

#  Exception Chaining: Exception chaining allows you to raise a new exception while preserving the original exception's context. This is useful when you want to provide additional information about an error without losing the original traceback.
def divide_with_chaining(a, b): 
    try:
        return a / b
    except ZeroDivisionError as e:
        raise CustomError("Custom error: Division by zero.") from e
    
divide_with_chaining(10, 0)  # This will raise CustomError with the original ZeroDivisionError as context

# finally block: The finally block is used to define a section of code that will always be executed, regardless of whether an exception was raised or not. It is typically used for cleanup operations, such as closing files or releasing resources.
# cleanup code that needs to be executed regardless of whether an exception occurred or not. It is often used for releasing resources, closing files, or performing any necessary cleanup tasks.

file = None
try:
    file = open("sample.txt", "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("Error: File not found.")
finally:
    if file:
        file.close()
        print("File closed.")
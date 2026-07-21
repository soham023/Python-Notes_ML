#  Modules
#  A module is simply a python file that contains reusuable code like variables, functions, classes etc. we can import a module into another module or script to use its functionality.

import math
import random
import datetime
import os
import sys

# random module
# randint returns a random number between 1 and 10
print (random.randint(1, 10))   

print(datetime.date.today())  # returns current date

print(os.getcwd())  # returns current working directory

print(sys.argv)  # returns command line arguments

# #  Packages
# A package is a collection of python modules. It is a way of organizing related modules together. A package is simply a directory that contains a special file called __init__.py and one or more python files (modules). The __init__.py file can be empty or it can contain initialization code for the package.


# from .calculator import add, subtract 
# from ..calculator import multiply, divide
# . -> current package
# .. -> parent package
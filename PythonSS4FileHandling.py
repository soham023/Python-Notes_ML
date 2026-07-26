# File I/O

# open 
# mode -> read - r , write - w
# f = open(<filename/filepath>, <mode>)
file = open("sample.txt", "r") # returns a file object

# 1. read
data = file.read()
print(data)
print(type(data))

file.readline() # reads the file by 1 single line

file.close()
# everytime if you r opening your file , u always need to close the file.

# 2. write
# write fully overwrites the file
file1 = open("sample.txt", "w") 
file1.write("Text to overwrite")
file1.close() # need to close the file after writing
# need to change the mode to w


# 3. append
# close
# delete

# different modes
# r -> reading
# w -> writing , truncates the file first/ overrides the whole file
# x -> creates new & open for writing
# a -> writing, appends at end
# b -> binary mode
# rb -> reading in binary mode
# wb -> writing in binary mode
# t -> text mode
# + -> opens disk file for update ( r & w )

# diff b/w r+ , w+, a+
# r+ -> pointer starts from the starting idx
# a+ -> pointer starts from the ending idx
# w+ -> file will become empty and it will just start writing

# context manager
# with keyword 
# with statement automatically closes the file after the nested block of code
with open ("sample.txt", "r" , encoding='utf-8') as f: # f is just a variable
    print(f.read())

# deleting a file
# os.path -> helps to check if the file exists or not
import os
# os.remove("sam.txt")
# os.path.exists("sam.txt") # returns True or False
# os.path.abspath("sam.txt") # returns the absolute path of the file
# file_path = os.path.join("data", "sample.txt") # joins the path of the file

# Exception Handling
# try, except, else, finally

try :
    x =  int(input("Enter x"))
    ans = 10/x
except ZeroDivisionError:
    # zero division error
    print("Cant enter 0")
except ValueError:
    print("Invalid input")
else:
    print(f"ans : {ans}")

finally:
    print("End of program")


squares = []

for i in range (6):
    squares.append(i*i)

print (squares)

# list comprehension
sq = [i*i for i in range(6)]
print(sq)

# with cond 
oddsq = [i*i for i in range(6) if i%2 != 0]
print (oddsq)

nums = [9,1,4,-2,1,-4,-7]
nums = [0 if i < 0 else i for i in nums]
print(nums)

#pathlib module
# modern way to handle file system paths
# it treats paths as objects rather than strings, so code is more readable and easier to work with

from pathlib import Path

path = Path("sample.txt")

print(path.exists()) # returns True or False
print(path.stat().st_size)
print(path.absolute()) # returns the absolute path of the file

content = path.read_text(encoding='utf-8') # reads the content of the file
print(content)

# Standard Streams > python has 3 standard streams that handle input, output and error operations
# sys.stdin, sys.stdout, sys.stderr


# stdin > standard input stream, used to read input from the user or from a file
name = input("Enter your name : ")
print(f"Hello {name}")

# import sys
# data = sys.stdin.readlines() # reads the input from the user or from a file
# print(data)

# stdout > standard output stream, used to write output to the console or to a file 
import sys
sys.stdout.write("Hello World\n") # writes the output to the console


# stderr > standard error stream, used to write error messages to the console or to a file
sys.stderr.write("Error: Invalid input\n") # writes the error message to the console


#Serialization
# process of converting an object into a format that can be stored or transmitted and reconstructed later

student = {
    "name": "Soham",
    "age" : 24
}

# json > readable text format 
# csv > tabular data format
# pickle > python specific binary format

import json

student = {
    "name": "Soham",
    "age" : 24
}

with open("student.json", "w", encoding='utf-8') as f:
    json.dump(student, f) # serializes the object and writes it to the file

with open("student.json", "r", encoding='utf-8') as f:
    data = json.load(f) # deserializes the object and reads it from the file

print(data)


# csv > comma separated values

# name , age
# Soham, 24
# Shivam, 25

import csv
students = [
    ["name", "age"],
    ["Soham", 24],
    ["Shivam", 25]
]

#  newline='' means -> it prevents the extra blank line after each row in the csv file
with open("students.csv", "w", newline="", encoding='utf-8') as f:
    writer = csv.writer(f) # csv.writer -> creates a writer object that can write to the file
    writer.writerows(students) # writes the rows to the file

with open("students.csv", "r", encoding='utf-8') as f:
    reader = csv.reader(f) # csv.reader -> creates a reader object that can read from the file
    for row in reader:
        print(row) # prints each row as a list


#DictWriter -> writes a dictionary to a csv file
# students = [    
#     {"name": "Soham", "age": 24},
#     {"name": "Shivam", "age": 25}
# ]


# Pickle > python specific binary format
import pickle

student = {
    "name": "Soham",
    "age": 24
}

with open("student.pkl", "wb") as f:
    pickle.dump(student, f) # serializes the object and writes it to the file in binary format

with open("student.pkl", "rb") as f:
    data = pickle.load(f) # deserializes the object and reads it from the file in binary format

print(data)
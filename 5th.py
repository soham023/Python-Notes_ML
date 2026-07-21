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
# need to change the mode to w


# 3. append

# close
# delete


# different modes
# r -> reading
# w -> writing , truncates the file first
# x -> creates new & open for writing
# a -> writing, appends at end
# b -> binary mode
# t -> text mode
# + -> opens disk file for update ( r & w )

# diff b/w r+ , w+, a+
# r+ -> pointer starts from the starting idx
# a+ -> pointer starts from the ending idx
# w+ -> file will become empty and it will just start writing


# with keyword 
with open ("sample.txt", "r") as f: # f is just a variable
    print(f.read())

# deleting a file
import os
# os.remove("sam.txt")

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
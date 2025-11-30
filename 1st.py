age = int(input("Enter age :"))
if age == 13 :
    print("Chup chutiye")
elif age == 15 :
    print("hatnaa Gandu!")
elif age == 18 :
    print("Tu bhi noob hi haii")
else :
    print("Tere baap ko mat sikha!")

word = "Hellio"

print(word[2: 3])


# Formatting --> Dynamic strings
    # format()
    #f-strings

a = 5
b = 10

sum = a + b
# normal formatting
print("sum is {}" .format(sum))
print("sum of {} & {} is {}" .format(a, b, sum))

#index based formatting
print ("sum of {1} & {0} is {2}" .format(a, b, sum))

#value based formatting
print ("{a} values of vars {a} & {b} ".format(a = 4, b = 12))

# F-Strings --> Literal String InterPolation 
print ( f"fstring-sum of {a} & {b} is {a + b}")


# Lists
marks = [98, 92,93, 91,94]
print(marks)
print(len(marks))
print(marks[:5])

# method in lists
nums = [1, 2, 3]
# 1. list.append(val)
nums.append(4)
print(nums)
# 2. list.insert(idx, val)
nums.insert(1, 5)
print(nums)
# 3. list.sort()
nums.sort()
print(nums)
#  4. list.reverse()
nums.reverse()
print(nums)

# Loops in Lists
for i in nums:
    print(i)

# find an  element in list (linear search)
idx = 0
for val in nums:
    if(val == 3):
        print("idx is ",idx)
        break
    idx += 1

# Tuples 
# immutable sequnce of values
# have parenthesis/1st brackets

tup = (1, 2, 3, 4, 5)
# access tuple by idx --> tup[idx]
print(tup[2]) # here idx = 2
# tup.index(val) --> returns the 1st occurence
print(tup.index(2))
# tup.count(val) --> returns the counts of the val
print(tup.count(3))

# Dictionary
# key-value pairs
# have curly braces / 2nd brackets
#  Dictionary is mutable
info = {
    "name" : "Soham",
    "hobby" : "gaming",
    "IGN" : ["Texas","Denied"],
    3.14 : "PI"
}

print(type(info))
print(info["name"])
print(info[3.14])

info["hobby"] = "shooting heads"
print(info)

info["IGN"][1] = "Denial"
print(info)

# dictionary methods
print(info.keys())

# converting into lists
print(list(info.keys()))

# dict values
dict_vals = list(info.values())
print(dict_vals)

# dict_items --> returns key value pairs
dict_items = list(info.items())

# get meethod --> returns value according to the key
# info.get(val)
dict_name_val = info.get("name")
print(dict_name_val)

# we already have [key] to access why get(key)?
# bcz [key] -> if the key is wrong, it gives error. bt inside get(key) if key is wrong it returns none

# print(info["c"]) #gives error c is invalid


# for updating a new key value pair
info.update({
    "city" : "Kolkata"
})

print(info)


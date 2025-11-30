# Sets
# Collection of unique elements
# unordered
newset = {1, 2, 3, 4, 2, 2}
print(newset)

empty_set = {} # it is not an empty set, it creates a dictionary, as curly braces represents for dictionary in pyhton

print(type(empty_set))

# creating empty set
emset = set()
print(type(emset))

# Methods in set --> 
# add(val), remove(val), 
newset.add(5)
newset.add(98)
print(newset)
newset.remove(2)
print(newset)
# pop() --> removes a random val
newset.pop()
print(newset)

# union(set2) --> returns new union
set2 = { 2,3,5, 7, 7}
print(newset.union(set2))

# intersection(set2) --> returns new intersection
print(newset.intersection(set2))

# clear() --> empties the set
newset.clear()
print(newset)
# iterables > an iterable in any object that can be looped over using a for loop

numbers = [1, 2, 3, 4]
name = "Python"
student = { "name" : "Riya", "age" : 25 }


# All above things are iterables because we can do this looping on every one of them

# iterables ->  eg. list, tuple, string, dictionary
for item in numbers:
    print(item)


# iterables vs iterators

# iterable is something that we can loop over
# iterator is the actual object that gives values one by one.

numbers = [10, 20, 30]

iterator = iter(numbers)


print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# iterator protocol >
# An Object should have __iter__() > return iterator object  and __next__() > return the next value

print(iterator.__next__())
print(iterator.__next__())

# Stop iteration

# Generators > simple way to create iterators

# yield() instead of __iter__() , __next__()

def count_up_to(limit):
    current = 1

    while current <= limit:
        yield current
        current += 1

for num in count_up_to(3):
    print(num)


# Generator Expressions

squares = [ x * x for x in range(5)]

print(squares)

squares = (x * x for x in range(5))
print(squares)
print(next(squares))
print(next(squares))
print(next(squares))

#Generators works like 1 by 1 like a stream


#map() > applies a function to every item in an iterable and modifies the same list

numbers = [1, 2, 3, 4]

squares = map(lambda x : x * x, numbers)
print(list(squares))


def square(x) :
    return x * x

squares2 = map(square, numbers)
print(list(squares2))


#filter > keeps only the items that match a condition

numbers = [1, 2, 3, 5]

even_numbers = map (lambda x : x % 2 == 0, numbers)

print(list(even_numbers))

# reduce combines all the values into a value according to a given condition
# available in functools module

from functools import reduce

numbers = [ 1, 3, 4, 6]
reduced_val = reduce(lambda x , product : product * x  , numbers)
print(reduced_val)

#functional Programming
#functions can be stored in variables
#passed as arguments
#returns from other functions
#used inside data transformations

def sq(x):
    return x*x
operation = sq
print(operation(6))

#HOF
def apply_operation(func, value):
    return func(value)

def sq(x):
    return x * x

print(apply_operation(sq, 5))


# Closures > a closure is when an inner function remembers variables from the outer function
# even after the outer function is finished

def multiplier (factor) :
    def multiply(number):
        return number * factor
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(10))
print(triple(10))


# functools > provides tools for working with functions

#reduce, partial, lru_cache, wraps

#functools.partial > partial() let us create a new function by fixing some argumnents of an existing function

from functools import partial

def power(base, exponent):
    return base**exponent

square = partial(power , exponent = 2)
cube = partial(power, exponent = 3)

print(square(5))

print(cube(3))

#itertools
# provides efficient tools for working iterators

#chain > combines multiple iterables into 1 sentence

from itertools import chain
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = chain(list1, list2)
print(list(combined))

#combinations() > gives possible selections using repeating order

from itertools import combinations

items = ["A", "B", "C", "D"]

result = combinations(items, 3)
print(list(result))
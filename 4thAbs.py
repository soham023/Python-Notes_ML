# Abstraction
# Hiding internal detail & showing only essential features

# we use Abstract classes(part of ABC module)


from abc import ABC, abstractclassmethod

class Animal(ABC):
    @abstractclassmethod
    def make_sound():
        pass
class Lion (Animal):
    def make_sound(self):
        print("Roar!")

lion = Lion()
lion.make_sound()


# Polymorphisim
# Many Forms
# Multiple Functions with same name bt diff implementations
# Like + operartor -> we can add 2 numbers and concat 2 strings as well

# 1. func overriding
class Emp :
    def get_designation(self):
        print("Employee")

class Tech(Emp):
    def get_designation(self):
        print("teacher")

# 2. Duck_Typing
    #  2 classes with no relation , 1 function needed in both classes for same type of work

class Teacher:
    def get_designation(self):
        print("Teacher")

class Acct:
    def get_designation(self):
        print("Accountant")

acc1 = Acct()
acc1.get_designation()
te1 = Teacher()
te1.get_designation()
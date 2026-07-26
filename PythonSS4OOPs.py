class Student:
    subject = "Python"
    college = "ABC"

stu1 = Student()
stu2 = Student()
students = []
for i in range (0,4):
    stud = Student()
    students.append(stud)

for i in students:
    print(i.college, i.subject)

# Contructor
# _init_Method
#  def__init__(self):
# self means it's storing the current instance of the class/storing reference of current object.
class Studs:
    college = "ABC Collrge" #class attribute > belongs to the class and shared by all instances of the class
    def __init__(self, name, cgpa):
        self.name = name #instance attribute (name in self.name) > belongs to individual object
        self.cgpa = cgpa

    # class methods --> it can access only class attributes
    # class methods has decorators --> e.g - @classmethod
    # class methods --> 1st param - cls
    @classmethod #changes the behaviour and makes it as a class method
    def get_info(cls): 
        print(cls.college)

    # instance methods --> 1st param - self
    def get_cgpa(self): 
        return self.cgpa
    # instance attribute --> higher priority


    # static methods 
    # no compulsory parameter
    # neither access class attribute nor instance attribute
    # decorator -> @staticMethod
    # static method - tied up with class
    @staticmethod
    def calc_disc(price, mormrate):
        finalp = price * mormrate
        print(finalp)


# class method vs static method
# class method can access class attributes and instance attributes but static method can't access any attributes

stuu1 = Studs("Soham", 9.3)  
print(stuu1.name)
print(stuu1.get_cgpa())
Studs.get_info()
stuu1.calc_disc(30000, 0.2)


class Products:

    count = 0

    def __init__(self, name , price):
        self.name = name
        self.price = price
        Products.count += 1 #self.count can't be written as it will create the count variable for the new object

    @classmethod
    def getCount(cls):
        return cls.count
    
    @staticmethod
    def calc_dic(price , perc):
        disc_p = price - price *perc /100
        print(disc_p)
    
p1 = Products("Phone", 40000)
p2 = Products("Laptop", 100000)

print(Products.getCount())

p1.calc_dic(p1.price, 10)
          
# OOPs
# Encapsulation
# wrapping data & functions in a single unit

# data-hiding
# make variables /methods private/protected which you want to hide

# private - can't access outside class
# protected - only accessable inside class and its subclass

class BankAcc :
    def __init__(self, name, num, bal):
        self.name = name
        self._num = num #protected attribute by using single underscore(_)
        self.__bal = bal #private attribute by using double underscore(__)

    def get_balance(self):
        return self.__bal

acc1 = BankAcc("Soham", 2341, 3000)
    
# access private variables by using getters/setters
print(acc1.get_balance())

# access private variables directly
# acc1._<classname>__<private-variable>
print(acc1._BankAcc__bal)



# Inheritance
class Employee :
    st_time = "10AM"
    e_time = "6PM"

class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject
class Admin(Employee):
    def __init__(self, role):
        self.role = role
# multilevel
class Accountant(Admin):
    def __init__(self, role, salary):
    #    calling constructor of parent class
        super().__init__(role)
        self.salary = salary

t1 = Teacher("Math")
print(t1.subject, t1.st_time, t1.e_time)

acc1 = Accountant("Engineer", 24000)

print(acc1.role, acc1.salary, acc1.st_time, acc1.e_time)
# Types of inheritance
# 1. single Level 
# 2. MultiLevel

# 3. Multiple
class Prof:
    def __init__(self, salary):
        self.salary = salary

class ClgStudent:
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Prof, ClgStudent):
    def __init__(self, salary, gpa):
        # 1st parent constructor using super
        super().__init__( salary)
        # 2nd parent constructor using the ClassName
        ClgStudent.__init__(self, gpa)
        self.name = name



# magic methods
# special methods
 #__init__ --> constructor
 #__str__ --> string representation of the object
 #__add__ --> add 2 objects
 #__len__ --> length of the object
 #__eq__ --> compare 2 objects
 #__gt__ --> greater than


class Student:
    school = "ABC"

    def __init__(self, marks):
        self._marks = marks

    @property # getter method
    def marks(self):
        return self._marks   

    @marks.setter # setter method
    def marks(self, marks):
        self._marks = marks


student1 = Student(90)
print(student1.marks)

student1.marks = 95
print(student1.marks)


# Data Classes > helps to create classes that are mainly used to store data

# they reduce boilerplate code by automatically generating special methods like __init__, __repr__, and __eq__ based on the class attributes.

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    gpa: float

student1 = Student("Soham", 24, 9.3)
print(student1)

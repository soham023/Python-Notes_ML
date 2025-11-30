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
    college = "ABC Collrge" #class attribute
    def __init__(self, name, cgpa):
        self.name = name #instance attribute
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

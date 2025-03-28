# classes & objects 
# class is a blueprint for creating objects

class Student: # this is class and name hamesha capital letter thi saru thay
    name = "jay"

s1 = Student() # this is object(instance)
print(s1.name) 



# __init__ function (constructor)
class Student:
    # default constructor 
    def __init__(self): 
        pass

    # parameterized constructor 
    def __init__(self, name, marks): 
        self.name = name
        self.marks = marks
        print("adding new student")

s1 = Student("Jay", 97)
print(s1.name, s1.marks) # attributes -> data, variables



# class & instance Attributes
class Student:
    college_name = "ABC College"
    name = "anonymous" # class attribute

    def __init__(self, name, marks): 
        self.name = name # object attribute > class attribute
        self.marks = marks
        print("adding new student")

s1 = Student("Jay", 97)
print(s1.name, s1.marks, s1.college_name)
print(Student.college_name)



# methods 
class Student:
    college_name = "ABC College"

    def __init__(self, name, marks): 
        self.name = name 
        self.marks = marks
        
    def welcome(self): # method
        print("welcome student")

s1 = Student("Jay", 97)
s1.welcome() # call method



# static methods 
# jema self parameter ni jarur na hoy tyare tene class level par lavi tena mate decorator use kari sakay
class Student:
    @staticmethod # decorator
    def college():
        print("ABC College")



# oops pillars
# 1) Abstraction (Hiding the implementation details of a class and only showing the essential features to the user)
# 2) Encapsulation (wrapping data and functions into a single unit(object))
# 3) Inheritance (When one class(child/derived) derives the properties & methods or another class(parent/base))
# 4) Polymorphism


# 1) Abstraction
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True    
        self.acc = True
        print("car started..")

car1 = Car()
car1.start()


# 2) Encapsulation




# del keyword 
# used to delete object properties or object itself
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("JAY")
del s1 # delete
print(s1)



# private(like) attributes & methods
class Person:
    __name = "anonymous" # private (make 2 __ before attribute)

    def __hello(): # private (make 2 __ before method)
        print("hello person")

p1 = Person()
print(p1.__name) # no access (class ni bar access na thay)
print(p1.__hello()) 



# 3) Inheritance 
class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car): # inheritance Car class
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Hilux")

print(car1.name)
print(car1.start())

# inheritance types
# 1) single
# 2) multi-level
# 3) multiple



# supre method 
# super() method is used to access methods of the parent class
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name, type): 
        super().__init__(type) # parent class ni koipan method ne call karva mate super thruw access kari sakay
        self.name = name

car1 = ToyotaCar("Fortuner", "electric")
print(car1.type)


# class method
# @classmethod

# @property
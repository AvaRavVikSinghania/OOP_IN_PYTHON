# DRY  Do not repeat yourself
# Code resuability
# All the data member , method and constructor
# Private member are not inherited (__things)
# Child class object can access all the method from parent class reverse is not possible
# in UML we represent --|>
# polymorphism 
# Method Overriding (same function name if we make the object and called the override 
# function then it wil search own class if not then it go to parent class
# if child class has constructor then it will called if not then parent constructor will be called
#Super Keyword (with the help this keyword we can called parent constructor and method not attribute of parent)
#Method Overloading
# Operator Overloading

class User:

    def login(self):
        pass

    def register(self):
        pass


class Student(User):
    
    def enroll(self):
        pass

    def review(self):
        pass



student1 = Student()
student1.register()
student1.enroll()



#Types of Inheritance 
# 4 types
# single level
# Multi level Inheritance
# Hierachical Inheritance
# Multiple Inheritance (Java do not allow this)

#MRO (Method Resolution Order !! Jis Order me Inherit hoga usi order me priority de jayegi)
# Method overloading
# There is no method overloading in python but we can achieve this

class Geometry:
    def area(self,radius):
        return 3.14*radius*radius
    
    def area(self,l,b): # this will be override with previous one area
        return l*b
    


#Operator Overloading
# + -    This is achieved by magic method
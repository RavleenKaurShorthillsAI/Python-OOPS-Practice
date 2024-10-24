# we cannot have method overloading in python
# that means two methods canot have same names

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None):
        s = a+b
        return s

s1 = Student(34,45)
print(s1.sum(4,10))
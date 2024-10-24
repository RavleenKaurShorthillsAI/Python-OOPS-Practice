# instance methods
# class methods
# static methods

class Student:

    school = "BCM"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        # instance method --> Accessors --> T fetch the value
        # Mutators --> to modify The values 
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    # def get_m1(self):
    #     return self.m1
    # def set_m1(self, value):
    #     self.m1 = value
    @classmethod
    # we have to write the classmethod in order to access the class variable without passing any argument, also use the classname only to access it.
    def info(cls):
        return cls.school
    
    @staticmethod
    def get_info():
        print("This is STudent Class")

s1 = Student(33,44,55)
s2 = Student(56,98,45)

print(s1.avg())
print(s2.avg())
print(Student.info())

Student.get_info()
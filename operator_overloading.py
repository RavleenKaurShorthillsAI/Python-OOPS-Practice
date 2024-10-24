a=5
b=6
print(a+b)
print(int.__add__(a,b))


class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 =m2
    
    def __add__(self,other):
        m1 = self.m1 + self.m2
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)

        return s3
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)

s1 = Student(66,78)
s2 = Student(99,34)

s3 = s1+s2
print(s3.m1)

a = 9
print(a)
print(a.__str__())
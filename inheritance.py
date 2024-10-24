class A:
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2")
class B():
    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4")

class C(A,B):
    def feature3(self):
        print("Feature 6 working")

a1 = A()

a1.feature1()
a1.feature2()

b1 = B()
c1 = C()
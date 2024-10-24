class A:
    def __init__(self):
        print("In A's Init")

    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2")
class B(A):
    def __init__(self):
        print("In B's Init")
        super().__init__()
        

    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4")


class C(A,B):
    def __init__(self):
        # Method Resolution Order (Left to Right)
        super().__init__()
        print("In C init")

a = C()
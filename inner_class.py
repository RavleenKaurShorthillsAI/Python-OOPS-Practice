class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 16
        def show(self):
            print(self.brand, self.cpu,self.ram)
            

s1 = Student("Ravleen",127)
s2 = Student("Jenny",89)

lap1 = s1.lap.brand 
print(lap1)
s1.show()
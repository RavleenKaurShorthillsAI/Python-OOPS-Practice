# 2 variables ---> Class Variable(static), Instance Variable
class Car:
    def __init__(self):
      self.mil = 10
      self.com = "Mercedes"

c1 = Car()
c2 = Car()
Car.wheels = 3
wheels = 4  
# (if we create a variable inside a class , then for every object it gets changed)
print(c1.mil,c2.com,c2.wheels)

print(c1.mil,c2.com,c2.wheels)

# If the variables are declared inside __init__ methods,
# then they are instance variables,
# If the variables are declared inside a class(outside init), then they are class variables which cannot be changed
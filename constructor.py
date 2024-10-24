class Computer:
    def __init__(self):
        self.age = 22
        self.name = 'Ravleen'
    
    def update(self):
        self.name = 'Ravleen Kaur'
    def compare(self,c2):
        if self.age == c2.age:
            return True
        else:
            return False

c1 = Computer()
c2 = Computer()
c1.update()
c1.age = 22
if c1.compare(c2):
    print("They are same")
else:
    print("They are different")
print(c1.name)
print(c2.name)
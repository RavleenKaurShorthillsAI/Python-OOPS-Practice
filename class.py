class Computer:
    def config(self):
        print("i5 ,16GB, 1 TB")


com1 = Computer()
print(type(com1))
Computer.config(com1) #if we want to call a method, we have to mention the classname
com1.config()

# A class always have attributes --> variables and behaviour --> methods
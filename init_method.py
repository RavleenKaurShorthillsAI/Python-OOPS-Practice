class Computer:
    def __init__(self,ram,cpu):
       self.ram = ram
       self.cpu = cpu
       print("In init") 

    def config(self):
        
        
        print("in config", self.cpu,self.ram)

com1 = Computer("Ryzen 5","abcd")
com1.config()
# com1.config()
class Pycharm:
    def execute(self):
        print("Compiling")


class MyEditor:
    def execute(self):
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()

ide = Pycharm()

lap1 = Laptop()
lap1.code(ide)
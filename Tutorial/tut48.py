'''Polymorphism -- Duck typing'''
#if it walks, swims and quacks like a duck, it is a duck

class Laptop:
    def code(self,ide):
        try:
            ide.execute()
        except:
            print("This IDE does not support Execution.")
        
class PyCharm:
    def execute(self):
        print("Interpreting")
        print("Executing")
        
class Spyder:
    def execute(self):
        print("Type Check")
        print("Def Check")
        print("Interpreting")
        print("Executing")
        
class Gedit:
    def dark(self):
        print("Theme changed to dark")
        
ide1 = PyCharm()
ide2 = Spyder()
lap = Laptop()
ide3 = Gedit()

lap.code(ide1)
print("")
lap.code(ide2)
print("")
lap.code(ide3)  
print("")      
#As long as a class contains a certain method, it will be fetched when called
#This is irrespective of whether that same method is present in other class or not
#This is what duck typing means, we perform methods as long as they exist in class

        
        
        
        
        
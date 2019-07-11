'''Constructor, Self and Comparing Objects'''

class Computer():
    def __init__(self):
        self.brand = 'Lenovo'
        self.os = 'Windows'
    
    def update(self):
        self.os = 'Arch Linux'
        
    def compare_os(self,other):
        if self.os == other.os:
            return True
        else:
            return False

#These are constructors, they create objects in memory
c1 = Computer()
c2 = Computer()
print(id(c1),id(c2))

#changing attribute values
c2.os = 'Ubuntu'
c2.brand = 'Dell'

print(c1.os,c1.brand,c2.os,c2.brand)

#Lets run update method now

c1.update()             #self is assigning the method to current instance
print(c1.os,c1.brand,c2.os,c2.brand)
print("")
if c1.compare_os(c2):
    print("They use the same OS")
else:
    print("They use different OS")
print("")
   
c2.update()

if c1.compare_os(c2):
    print("They use the same OS")
else:
    print("They use different OS")
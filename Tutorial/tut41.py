'''Class and Object'''
#Class is a design whereas object is an instance, an example of a class
#A class contains attributes and behaviours
#Attributes are varibales and behaviours are functions

##Lets create a class and an object to go with it

class Computer:
    def config(self):                   ##Note this self keyword, will see l8r
        print('intel i5, 16gb, 1Tb')
        
comp1 = Computer()                 ##This an instance/ object of the class 
print(comp1, type(comp1))
comp1.config()
Computer.config(comp1)

##Lets make a new class -- init method : constructor for attributes
print("")
class city:
    def __init__(self,location,football_club):
        print("This is init speaking")
        self.location = location
        self.football_club = football_club
        
        
    def language(self):
        print("Spanish, Romance")
        print(self.location, self.football_club)
        
Barcalona = city(location='North-East',football_club='FCB')     #Object creation with attributes
Madrid = city('Central','Real Madrid')
Barcalona.language()                                            #Method call -- will print init by default
Madrid.language()



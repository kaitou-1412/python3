'''Variables inside a class -- instance and class (static)'''

class Car:
	
	doors,wheels = 4,4				##These are class variables
		
	def __init__(self):				##These are instance variables
		self.economy = 10
		self.brand = 'BMW'
		
c1,c2 = Car(),Car()
c1.economy = 8
c1.brand = 'Audi'

print(c1.economy,c1.brand,c1.doors,c1.wheels)
print(c2.economy,c2.brand,c2.doors,c2.wheels)

#Rolling an update to all class objects --
Car.doors = 2
print(c1.economy,c1.brand,c1.doors,c1.wheels)
print(c2.economy,c2.brand,c2.doors,c2.wheels)
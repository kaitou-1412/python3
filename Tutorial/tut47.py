'''Inheritance in Python - - init and MRO'''

#Child classes gain qualities of parent class
#child classes are more feature rich
#Priority of inheritance from parent classes

class A:
	def _init_(self):
		print("This is A init")
		
	def f1(self):
		print("This is feature 1")
		
	def f2(self):
		print("This is feature 2")
		
	def fc(self):
		print("This is feature from A")	

class A1:
	def _init_(self):
		print("This is A1 init")
		
	def f11(self):
		print("This is feature 11")
		
	def f21(self):
		print("This is feature 21")
		
	def fc(self):
		print("This is feature from A1")	
	

##B->A but B has no init of its own

class B(A):
	def f3(self):
		print("This is feature 3")
		
	def f4(self):
		print("This is feature 4")

##C->A and C has its own init		
		
class C(A):
	def _init_(self):
		print("This is C init")
	
	def f5(self):
		print("This is feature 5")
		
	def f6(self):
		print("This is feature 6")

##Accessing init of parent class
##D->A and D has an init but we want A init
class D(A):
	def _init_(self):
		super()._init_()
		print("This is D init")
		
	def f7(self):
		print("This is feature 7")
		
	def f8(self):
		print("This is feature 8")
		
#If a class has multiple parents 
#init preference to leftmost class
#This is MRO Method res order
		
class E(A,A1):
	def _init_(self):
		super()._init_()
		print("This is E init")
		
	def f7(self):
		print("This is feature 7")
		
	def f8(self):
		print("This is feature 8")
	
##C contains f 5,6,1,2
##D contains f 1-8

b1 = B()
c1 = C()
d1 = D()
e1 = E()

##Same goes for methods with same name
e1.fc()
'''Inheritance in Python'''

#Child classes gain qualities of parent class
#child classes are more feature rich


class A:
	def f1(self):
		print("This is feature 1")
		
	def f2(self):
		print("This is feature 2")


class B:
	def f3(self):
		print("This is feature 3")
		
	def f4(self):
		print("This is feature 4")
		
		
class C(A):
	def f5(self):
		print("This is feature 5")
		
	def f6(self):
		print("This is feature 6")

class D(C,B):
	def f7(self):
		print("This is feature 7")
		
	def f8(self):
		print("This is feature 8")
	
##C contains f 5,6,1,2
##D contains f 1-8
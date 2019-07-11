'''Method overloading, Method Overriding'''

##Equivalent of method overloading

class Adder:
	def sum(self,a=None,*b):
		s = 0
		if a==None:
			return s
		if a!=None:
			s+=a
			for i in b:
				s+=i
		return s
		
a1 = Adder()
print(a1.sum(12,9,78,56,52,47))
print(a1.sum(4))
print(a1.sum(12,22))
print(a1.sum(12,13,5))
print(a1.sum())

##Method overriding -- My fathers phone is my phone when I don't have a phone
##But when I get a phone my phone is my phone first, father's phone ignored

class A:
    def show(self):
        print("Class A sends regards!")
        
class B(A):
    def show(self):
        print("Class B sends regards!")
        
class C(A):
    def see(self):
        print("Potatoes are green in Ireland")
        
        
b1 = B()
c1 = C()

b1.show()
c1.show()

##Note how b1 says Class B since it has its own show and C takes it from parent A
##B overrides show method taken from A









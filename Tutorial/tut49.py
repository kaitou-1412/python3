'''Operator overloading'''
##Use help(int/class) inside idle to get methods

#What happens behing the scenes -- how operations are carried out

a,b = 5,6
print(a+b)
print(int.__add__(a,b))

#We redefine operators for our new classes

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        
        return s3
    
    def __gt__(self,other):
        S1 = self.m1 + self.m2
        S2 = other.m1 + other.m2
        if S1>S2:
            return True
            
    def __ge__(self,other):
        S1 = self.m1 + self.m2
        S2 = other.m1 + other.m2
        if S1>=S2:
            return True
    
    def __eq__(self,other):
        S1 = self.m1 + self.m2
        S2 = other.m1 + other.m2
        if S1==S2:
            return True
    
    def __str__(self):
        return "m1: {} m2: {}".format(self.m1,self.m2)
       
    
s1 = Student(42,55)
s2 = Student(48,52)
s3 = s1 + s2                            ##We have a overloaded method for this

if s1 > s2:                             ##We have method defined for this
    print("s1 has more marks overall")
elif s1==s2:
    print("they are equal scoring")
else:
    print("s2 has more marks overall")
    
#Printing instance values using overriding function
#Otherwise it return class type and address by default

print(s1)
print(s2)
    
    
    
    
    

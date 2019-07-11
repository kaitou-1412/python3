'''Methods inside a class -- instance, class and static'''

class Student:
    school = 'Epsilon'
    
    def __init__(self,m1,m2,m3):
       self.m1 = m1
       self.m2 = m2
       self.m3 = m3
       
    def avg(self):                                  ##Instance method
        return (self.m1 + self.m2 +  self.m3)/3
        
    def get_m1(self):                               ##Access method
        return self.m1
    
    def set_m1(self,value):                         ##Mutating method
        self.m1 = value
        
    @classmethod                                    ##decorator
    def get_school(cls):                            ##class method
        return cls.school
    
    @staticmethod                                   ##decorator
    def info():                                     ##Static method
        print("This is Student class.")
    
    
s1 = Student(34,42,88)
s2 = Student(55,89,78)

print(round(s1.avg(),2))
print(round(s2.avg(),2))

print(Student.get_school()) ##Doesn't matter if class is passed or instance is
print(s1.get_school())



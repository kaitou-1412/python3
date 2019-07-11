'''Arguments and their types'''

def add(a,b):       ##Formal arguments
    c = a+b
    print(c)
    
add(5,6)            ##Actual arguments

#Actual arguments have four types : Position, Keyword, Default and Var length

def person(name,age):
    print(name,"",end='')
    print(age)
    
person('john',20)           ##This is positional arg since its entry is pos dependent

person(name='john',age=20)  ##This is keyworded arg


def person_with_defaults(name='john appleseed',age=18):
    print(name,"",end='')
    print(age)
    
person_with_defaults('Michael') ##This is default arg and it gets age as default
person_with_defaults('Benjamin',25) ##This overwrites the default

#Variable length argument -- here b will be parsed as a tuple
def fsum(a,*b):
    c = a
    for num in b:
        c += num
    print(c)
        
fsum(12,13,22,6)
fsum(13,12)        

















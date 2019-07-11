'''Functions in Python3'''

#they are the suits that give modularity to the code
#they give repitition to the program
##defining a function
def greet():
    print("This function says hello")
   
##calling a function   
greet()

#creating a simple add function

def add(x,y):
    c = x+y
    print(c)
    
add(12,13)

#returning a value back without printing

def square(x):
    c = x**2
    return c
num = int(input('enter a number:\t'))
z = square(num)
print("The square of",num,"is",z)    









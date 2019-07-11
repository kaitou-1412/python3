'''Operators in Python3'''

#Arithmetic operators
x,y = 2,9
print(x+y,x-y,x/y,x*y)

#Assignment operator 
x = 7
print(x)
x = x+2
print(x)
x+=2
print(x)
x*=3
print(x)

#Unary operator
n = 7
n = -n
print(n)

#Relational Operators
print(x<y)
print(x==33)
print(y<=x)
print(x!=33)

#Mathematical logical operators -- conjuction, disjunction and negation
##Truth table methods
print("Or operator",x<8 or y>3)
print("And operator",x<8 and y!=3)
print("Not operator",not(x<8 and y!=3))
'''Swapping two variables in python3'''
a = 5
b = 6

#Temp variable method
t = a
a = b
b = t
print("a",a,"b",b)

#Mathematical method
a = a+b
b = a-b
a = a-b
print("a",a,"b",b)

#Logical method -- works only on int
a = a^b
b = a^b
a = a^b
print("a",a,"b",b)

#Python way -- stack technique
a,b = b,a
print("a",a,"b",b)


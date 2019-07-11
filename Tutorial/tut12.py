'''The Math module/library in Python3'''

##this is an import statement --
import math
##alternatively we can do a selective import 
from math import sqrt
import math as m

#Lets make use of this sqrt function
y = sqrt(25)
print(y)
print(int(math.sqrt(256)))
z = m.sqrt(54)
print(round(z,3))

#Floor and ceil functions 
print(m.floor(z))
print(m.ceil(z))

#Exponents and Powers
print(2**4)
print(m.pow(4,3))

#Constats from math library
print(m.pi)
print(m.e)

#For more info
##print(help('math'))
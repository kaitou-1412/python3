'''For loops in python3'''

#A few ways of using the for loop

lst = ['zarcon','imran','navjot']

for i in range(len(lst)):
    print(lst[i])
    
for name in lst:
    print(name,len(name))

#A simple range iteration

for i in range(2,11,2):
    print(i,"",end='')
    
#The biggest power of loops is seen when they are used in tandum with if-else

for i in range(1999,2019):
    if(i%4==0):
        print(i)
        
print("")
#Printing square numbers between 1 and 500
from math import sqrt

for i in range(1,500):
    if (int(sqrt(i))==sqrt(i)):
        print(i)
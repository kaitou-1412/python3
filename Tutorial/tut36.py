'''Factorial of a number using recursion'''

def fact(n)->int:
    if n == 0:
        return 1
    else:
        return n*fact(n-1) 
        
print(fact(5))

#Without recursion

def facto(n):
    prod = 1
    for i in range(1,n+1):
        prod = prod*i
    return prod  
    
print(facto(3))

#Recursion stats -- and modifiers

import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)
print(sys.getrecursionlimit())
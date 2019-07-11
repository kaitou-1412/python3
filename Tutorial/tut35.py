'''Fibonacci series problem'''

#Python way of doing it

def fibo(a,b):
    c = a+b
    return c
    
fibo_list = [0,1,1]
n = int(input('Enter the range for which fibo is to be generated: '))
for i in range(0,n-3):
    x = fibo(fibo_list[-1],fibo_list[-2])
    fibo_list.append(x)

print(fibo_list)

#Regular way of doing it

def fib(num):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in (2,num):
        c = a+b
        a = b
        b = c
        print(c)
fib(8)





        
        
        
        
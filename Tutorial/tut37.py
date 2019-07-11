'''Lambdas -- Anonymous functions'''

#Normie way of doing a squaring op

def square(a):
    return a*a

result = square(5)
print(result)

#Chad way -- lambda way

f = lambda a : a*a
res = f(12)
print(res)

#Chad way of composing a power function
power = lambda a,b : a**b
print(power(2,3))
'''Filter, Map and Reduce'''

#filter is method that takes a function,returns a filtered list from given list

#Normie way of using filter
def is_even(n):
    return n%2==0

nums = [2,6,7,5,12,9,77,28,45,99,78,10,15,21]
even = list(filter(is_even,nums))
print(even)

#Chad way
odd = list(filter(lambda n : n%2!=0,nums))
print(odd)

#map function takes original values and assigns a corresponding function to items

sqrt = list(map(lambda n : round(n**0.5,2),nums))
print(sqrt) 

#reduce takes multiple parameters and returns a single value out 
from functools import reduce
sum = reduce(lambda a,b : a+b, nums)
print(sum)
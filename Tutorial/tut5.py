'''Tuples and Sets in python3'''
'''Tuples in python3 are immutable'''
'''Tuples support multiple data-types'''

tup = tuple
tup = (32,22,22.5,'vamos')
print(tup)

#Lets make a tuple of tuples
new_tup = (22,5662,'muchacho')
big_tup = (new_tup,tup)
print(big_tup)

#Tuples are stripped down lists and have 2 methods -- count and index
#count works on top level only and index return index of the value passed
print(big_tup.count(22))
print(new_tup.count(22))

print(new_tup.index('muchacho'))

'''A set is a collection of unique values'''

my_set = {22,45,12,'gerrad',78,22}
#Note how 22 disappears and becomes unique 
#Set also does not retain the original sequence
#Set follows a hash-table method
print(my_set)


#Note : Try out different methods associated with set

'''Arrays in python3'''
#Arrays are like lists but support only homogeneous data types
#They are faster at processing as compared to lists

import array as arr

values = arr.array('i',[5,9,-8,2,7])

print(list(values),"\t",values)

#To retrieve address and size

print(values.buffer_info())

#To add values use append and to remove - remove argument is used

#To reverse the entire array --
values.reverse()
print(values)

#Printing values of the array sequentially 

for term in values:
    print(term,"",end='')
print("")    
for i in range(0,len(values)):
    print(values[i],"",end='')
print("")       


#Create a new array with same values

newArr = arr.array(values.typecode,(term for term in values))
print("New Array:\t",newArr)

#Create a new array to hold sqaures of given array

sqArr = arr.array(values.typecode,(term*term for term in values))
print("Square Array:\t",sqArr)
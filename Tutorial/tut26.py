'''More operations on Numpy arrays'''

import numpy as np

#Incrementing each element in one shot
arr = np.array([5,4,7,8,6])
arr += 5
print(arr)

#Adding two arrays -- vectorized operations
arr1 = np.array([7,6,8,9,4])
arr2 = arr + arr1
print(arr,arr1)
print(arr2)

#Transendetal functions on arrays

print(np.log(arr))
print(np.sin(arr))
print(np.cos(arr))

#Simple functions

print(np.sum(arr))
print(np.sqrt(arr))

##try out sort and other functions that come with numpy library

#concatenate two arrays

print(np.concatenate([arr,arr1]))

#Pseudo copy of an array -- They point to the same location on memory -- alias

arr = np.array([5,6,2,7,8,9])
arr1 = arr
arr1[1] = 8
print("Arr",arr,id(arr))
print("Arr1",arr1,id(arr1))

#Shallow copy -- arrays still rely on each other

arr = np.array([5,6,2,7,8,9])
arr1 = arr.view()
arr1[1] = 8
print("Arr",arr,id(arr))
print("Arr1",arr1,id(arr1))

#Deep copy -- arrays are now completey independent

arr = np.array([5,6,2,7,8,9])
arr1 = arr.copy()
arr1[1] = 8
print("Arr",arr,id(arr))
print("Arr1",arr1,id(arr1))





















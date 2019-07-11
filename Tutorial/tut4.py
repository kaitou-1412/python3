'''Lists in python'''
#Explicit declaration -- not necessary
nums = list

#supplying values
nums = [14,12,78,45]
print(nums)

#Fetching a value out a list
print(nums[2])

#List behaves quite a bit like a string -- examples
print(nums[1:3])
print(nums[-2])

#Lists also support multiple data types
names = ['ryzen',9.42,56,True]
print(names)

#We can also have a list of lists

misc = [nums,names]
print(misc)

#Appending to a list -- insert at last position
misc.append('jonathan')
print(misc)

#Insert -- (pos,value)
names.insert(2,'jabralis')
print(names)

#Remove -- (value)
names.remove(9.42)
print(names)

#Pop -- remove by index
nums.pop(2)
print(nums)

#deleting multiple values
del names[2:]
print(names)

#Extending a list -- adding multiple values
names.extend(['kabul','tango'])
print(names)

#Getting sum of all values of list given they are numerals
numbers = [25,52.2,69.322,55.25,6]
print(sum(numbers))

#It also applies sort for you -- inbuilt
sortnumbers = numbers.sort()
print(sortnumbers)
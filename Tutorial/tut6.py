'''More on Variables'''

#Fetching variable addresses
this_integer = 25
this_name = 'Paul'

print(id(this_integer),id(this_name))

#A tricky outlook -- same data : same address -- memory efficiency
a = 10
b = a
print("a",a,id(a))
print("b",b,id(b))
print(10,id(10))

#Changing value of a
a = 15
print(b,"b",id(b))
print("a",a,id(a))

#By convention we name constant vars in capitalize
#This is to show outr immutability intention
STORAGE_SPACE = 256
print("My PC has",STORAGE_SPACE,"GB drive in it.")

#We can create our own variable type like Structures in other langs
#Lets extend our discussion to data types in next file

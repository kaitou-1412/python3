'''Variables in Python3'''
#Unlike java, C++, C, etc. Python3 does not require explicit declaration of variables
#This might make prototyping very quick, but can have certain hidden ramifications
#Python3 auto-detects the variable type
#Use type() method to get class of variables as shown in the footer

#Here is an integer variable
price = 10
print('price :',price)

#Python3 interpretor executes line by line --
a_variable = 25
a_variable = 45
print('a_variable :',a_variable)

#Here is a decimal called a float in python
float_var = 22.5
print("The oil costed us",float_var,"rupees")

#To use output of the previous operation - Shell only
print(price)
#print(_+12)

#Here is a string variable
name = 'Jabralis'
print("My name is",name)
print("My name also happens to be "+name)

#String behaves like an array -- a collection of characters
#Hence we can seek and fetch certain characters like so, starting from 0
# -1 indicated first character from last and 3 indicates 4th character from the beginning 
print(name[-1]+name[-2]+name[3]+name[7])

#We can also print an interval of characters(string slicing) from a string here : 'ra' from Jabralis
print(name[3:5])

#String slicing can also be done backwards
print(name[-4:-8:-1])



#Try slicing with [:3] and [4:] and [:] as is
'''Note : Strings in python are immutable'''




print(type(price),type(float_var),type(name))


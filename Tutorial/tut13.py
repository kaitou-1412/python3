'''User input in python'''

#By default the user input is parsed as a string -- hence concatination
x = input('Enter first number\t')
y = input('Enter second number\t')
print(x+y)
print(type(x),type(y))

#Lets do better and define the input type

x = int(input('Enter first number\t'))
y = int(input('Enter second number\t'))
print(x+y)

#Taking single character input
chs = input('Enter a character--only first will be recorded\t')
ch = chs[0]
print(ch)

ch1 = input('Enter a character--only first will be recorded\t')[0]
print(ch1)

#Evaluating an expression 
result = eval(input('Enter a mathematical function\t'))
print(result)
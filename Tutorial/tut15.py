'''Nested if statement -- leap year program'''
#We can have an if else block inside an if else block
#This is called nested if statements
##User input year

year = int(input("Enter a year:\t"))

if (year%100==0):
    if(year%400==0):
        print(year,"is a leap year")
    else:
        print(year,"is not leap")
else:
    if(year%4==0):
        print(year,"is a leap year")
    else:
        print(year,"is not leap")
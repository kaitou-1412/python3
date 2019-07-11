'''Exception handling'''

a = int(input("enter the numerator: "))
b = int(input("enter the denominator: "))

c = None

try:
    print("Resource open.")
    c = a/b
except ZeroDivisionError as e:
	print("Sorry, can't perform division - ",e)
except ValueError as e:
	print("Sorry, can't perform division - ",e)
except Exception as e:
	print("Sorry, can't perform division - ",e)
finally:
    print("Resource closed.")
	
print("The value of c is {}".format(c))
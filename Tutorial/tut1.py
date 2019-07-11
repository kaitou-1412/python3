'''Hello world and strings in Python3'''

#This is a simple hello world statement
print("Hello world")

#This is the way to print integers and floats
print(42)

#This is an integer in a string
print("42")

#Integers can be adding during output
print(42+69)

#Integers in strings can only be concatenated
print("42"+"69")

#And this will simply print the statement as though it were a string
print("42+69")

#Print statements can also be written in single quotes
print('I am a single quotes print statement')

#This how you compensate for an apostrophe (ignore special meaning with \ character)
print('I will be at Ronald\'s office today.')

#Or in this case a particular schema is used
print("She said that she had a 'meeting' with the devil.")

#Here is an elaborate example
print("She said,\"I will not fall prey to that 'devil' and his antics\"")

#Finally, \n is a special string that indicates jump to a new line
print("I had Kazuka ion the phone.\nHe was quite upset.")

#Comma separation -- will be helpful later on
print("Come here.","Don't be afraid")

#Special char separation
print(192,168,178,42,sep=".")

#Normally output to a file or the console is buffered, with text output at least until you print a newline. 
#The flush makes sure that any output that is buffered goes to the destination.
print('foo', flush=True) 



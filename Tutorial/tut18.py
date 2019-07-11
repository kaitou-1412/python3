'''Break continue pass in python'''

# Break : The break statement in Python terminates 
#the current loop and resumes execution at the next statement, 
#just like the traditional break found in C.

##To stop printing after h as occured -
mystr = 'Python'

for letter in mystr:
    if letter == 'h':
        break
    print(letter,end='')
print("")

# Continue : The continue statement in Python 
#returns the control to the beginning of the while loop. 
#The continue statement rejects all the remaining statements 
#in the current iteration of the loop and moves the control back to the top.

##To skip printing letter h  -
mystr = 'Python'

for letter in mystr:
    if letter == 'h':
        continue
    print(letter,end='')
print("")

#Pass : The pass statement is a null operation; nothing happens when it executes. 
#The pass is also useful in places where your code will eventually go, 
#but has not been written yet

##To replace letter h we'll use pass as well as continue -
mystr = 'Python'

for letter in mystr:
    if letter == 'h':
        pass
        print("k",end='')
        continue
    print(letter,end='')
print("")


##Note the implementation of these keywords will be clear  as we proceed further
##in our python3 conquest

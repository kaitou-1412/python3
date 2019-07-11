'''While loops in Python3'''
#Use to bring about iterations and repetitions


i = 1                               ##initialisation

while i<=5:                         ##condition
    print("This is not java.",i)
    i+=1                            ##Incrementation
    
    
print("")


#Nested while loops

i,j = 0,0

while i<3:
    print("Old McDonald had a farm ~ ",end='')
    while j<2:
        print("E-I-",end='')
        j+=1
    print("O",end='\n')
    i+=1
    j=0

##Interesting to note is the end of line end='' parameter we used in print
##It prevents print from jumping to the next line and it is end='\n'  by default



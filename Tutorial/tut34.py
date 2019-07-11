'''Pass list to a function'''

def even_odd_classifier(morgan_freeman):
    even,odd = 0,0
    for i in lst:
        if(i%2==0):
            even+=1
        else:
            odd+=1
    return (even,odd)

lst = list()
n = int(input("Enter number of elements to be entered:\t"))
for i in range(0,n):
    x = int(input('Enter next number: '))
    lst.append(x)
even,odd = even_odd_classifier(lst)
print("Even : {} and Odd : {}".format(even,odd))  ##Replace curly bracket with vars

#Classifier to detect names that exceed 5 characters

names = list()
n = int(input("Enter number of names to be entered:\t"))
for i in range(0,n):
    x = input('Enter next name: ')
    names.append(x)

def name_classifier(names):
    small_names = 0
    for name in names:
        if (len(name)<=5):
            small_names += 1
    return small_names
    
small_names = name_classifier(names)
big_names = n-small_names

print("Small names : {} and Big names : {}".format(small_names,big_names))



    
    
    
    
    
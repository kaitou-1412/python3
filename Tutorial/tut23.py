'''Taking user input and add the elements to an array'''

import array as arr

n = int(input("Enter number of elements in the array:\t"))
arr = arr.array('i',[])

for i in range(0,n):
    x = int(input('Enter next element:\t'))
    arr.append(x)
    
print(list(arr))

#Lets write a simple search programette to fetch index of an entry

ind_num = int(input("Enter the term to fetch the index for:\t"))
ind_list = []
for i in range(0,n):
    if(arr[i]==ind_num):
        ind_list.append(i)
        
print("The term",ind_num,"appears at",ind_list)
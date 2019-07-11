'''Linear search using python3'''

arr = [9,4,2,5,7,23,56,69,72,59,45,12,58,78,26,35,15,49,76,16,34]
n = 22
	
def search(arr,n):
	is_present,pos = False,None
	for i in range(len(arr)):
		if arr[i]==n:
			pos = i
			is_present=True
			break
		else:
			continue
	
	return is_present,pos
	
search_true,position = search(arr,n) 

if search_true==True:
	print("Value found at {}".format(position))
else:
	print("Value not found")
    
    
##Note : The position variable can also be set to bogus value and later modified using global keyword
##No return type required in that case
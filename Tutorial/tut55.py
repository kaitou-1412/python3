'''Binary search using python3'''

arr = [9,4,2,5,7,23,56,69,72,59,45,12,58,78,26,35,15,49,76,16,34]
n = 22

arr.sort()
print(arr)
def search(arr,n):
    pos,is_found = None,False
    l = 0
    u = len(arr) - 1
    while l<=u:
        mid = (l+u)//2
        print(mid,len(arr))
        if arr[mid]==n:
            pos = mid
            is_found = True
        else:
            if arr[mid]>n:
                u = arr[mid]
            else:
                l = arr[mid]
                
    return is_found,pos
	
search_true,position = search(arr,n) 

if search_true==True:
	print("Value found at {}".format(position))
else:
	print("Value not found")
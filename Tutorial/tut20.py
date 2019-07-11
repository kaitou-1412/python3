'''For else in python -- Linear search'''
#To search the first number divisible by 5 in a given list
#To return none found once if not present

nums  = [14,10,12,15,17]
nums1  = [14,19,13,22,17]

##Normie method -- gives none found multiple times

for num in nums:
	if num%5==0:
		print(num)
		break
	else:
		print("None found")
		
for num in nums1:
	if num%5==0:
		print(num)
		break
	else:
		print("None found")
        
print("")
        
##for-else chad method

for num in nums:
	if num%5==0:
		print(num)
		break
else:
	print("None found")
		
for num in nums1:
	if num%5==0:
		print(num)
		break
else:
	print("None found")
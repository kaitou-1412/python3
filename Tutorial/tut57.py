'''Selection sort'''

nums = [9,4,2,5,7,23,56,69,72,59,45,12,58,78,26,35,15,49,76,16,34,5]

def selection_sort(nums):
    k=0
    for i in range(len(nums)):
        minpos = i
        for j in range(i+1,len(nums)):
            k+=1
            if nums[minpos] > nums[j]:
                minpos = j
        
        nums[minpos],nums[i] = nums[i],nums[minpos]
    
    print(k)
    return nums    




nums = selection_sort(nums)
print(nums)
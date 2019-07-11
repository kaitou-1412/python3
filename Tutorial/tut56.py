'''Bubble sort'''

nums = [9,4,2,5,7,23,56,69,72,59,45,12,58,78,26,35,15,49,76,16,34,5]

def bubble_sort(nums):
    k = 0
    for i in range(len(nums)-1):
        for j in range(len(nums)-1):
            k+=1
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
            else:
                continue
    print(k)
    return nums
            

nums = bubble_sort(nums)
print(nums)
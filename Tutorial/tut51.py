'''Iterator and generators in Python3'''

nums = [22,45,78,53,57,99]
#Two previously seen methods of iteration

for num in nums:
    print(num,"",end='')

print("")

for i in range(len(nums)):
    print(nums[i],"",end='')
    
print("")
    
class topten:
    def __init__(self):
        self.num = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num<=10:
            val = self.num
            self.num+=1
            return val
        else:
            raise StopIteration

values = topten()
for i in values:
       print(i)

print("")

##Generators -- much faster than using return and keeping on iterating
    
def tt():
    n = 1
    while n<=10:
        sq = n*n
        yield sq
        n += 1
        
values = tt()

for i in values:
    print(i)




    
    
    
    
    
    
    
    
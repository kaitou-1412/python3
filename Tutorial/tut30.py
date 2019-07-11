'''More on funtions -- Arguments/Parameters'''


#A parameterized functionq
def update(x):
	x = 8
	print("x",x)
	
update(10)
print("")

#Pass by reference and pass by value -- kind of
#Python uses none of them. All vars with same value have the same id.

a = 10
update(a)               ##this is pass by value only. One value is considered
print("a",a)

#On the other hand, lists get completely changed
#But the id never changes

def update_list(lst):
    print("1",lst,id(lst))
    lst[1] = 20
    print("2",lst,id(lst))
    
lst = [5,10,15]
print("3",lst,id(lst))
update_list(lst)   
print("4",lst,id(lst))    
    
    
    
    
    
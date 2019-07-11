'''Global and local variables'''

a = 10				##This is a global variable for this file
b = 15

def something():
    a = 17
    ##global a
    ##a = 27
    x = globals()['a']          ##Fetches all global variables by name
    print("in function",a,id(a))
    print("in function",b,id(b))
    print("x from func",x,id(x))
    
something()
print("a global",a,id(a))
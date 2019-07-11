'''Keyworded Variable length arguments KWVARGS'''
#We have variable length arguments and they are all keyworded

def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

person('hebdo',age=22,place='UP',mobile=9767802468)
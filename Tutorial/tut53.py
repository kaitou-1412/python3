'''Multithreading in Python3'''

from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(500):
            print("Hello")
            sleep(0.005)
            
class Hi(Thread):
    def run(self):
        for i in range(500):
            print("Hi")
            sleep(0.005)
			
t1 = Hello()
t2 = Hi()

t1.start()
##Adding sleep to avoid collision
sleep(0.01)
t2.start()

##Preventing main thread from taking over and performing rest of the program -- 

t1.join()
t2.join()

print("Both threads are here, its time to say goodbye.\n")

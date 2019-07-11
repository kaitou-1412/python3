'''Special var -- __name__'''
import calc                                 ##Everythin from calc -- name as calc
print('This is  the base file',__name__)    ##name says __main__

#Lets use this to our advantage
print("")
import kalc       ##Notice how everything in kalc doesn't show up here
kalc.aux()        ##Only explicit function calls are honored
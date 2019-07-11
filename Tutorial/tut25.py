'''Numpy functionality'''

import numpy as np

#array,linspace,logspace,arange,zeros,ones

#Array --
reg_arr = np.array([1,2,4,7,19])
print("Regular array",reg_arr,reg_arr.dtype)

#linspace -- linear spacing or partition

lin_arr = np.linspace(0,16,10) ##(start,end,partitions:default=50)
lin_arr_round = np.array([round(term,2) for term in lin_arr])
print("Linear array",lin_arr_round,lin_arr.dtype)

#logspace -- exponential spacing between elements

log_arr = np.logspace(1,5,5) ##(start,end,partitions:default=50)
log_arr_round = np.array([round(term,2) for term in log_arr])
print("Log array",log_arr_round,log_arr.dtype)

#Arange -- giving out a range

arange_arr = np.arange(0,16,1)
print('arange array:',arange_arr,arange_arr.dtype)

#Zeros -- all zeros
zero_arr = np.zeros(7)
print("zeros",zero_arr)

#Ones -- all ones
one_arr = np.ones(4,int)
print("ones",one_arr)















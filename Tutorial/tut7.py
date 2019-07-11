'''Data Types in Python3'''
##An Entension of variable types

#None data type
void_variable = None
print(void_variable)

#Integers
int_var = 22
print(type(int_var),":",int_var)

#Floats
float_var = 2.2
print(type(float_var),":",float_var)

#Complex
complex_var = 7+6j
print(type(complex_var),":",complex_var)

#Type casting
##Float to int causes truncation
a = 5.6
b = int(a)
print(type(b),b)

c = 25
d = float(c)
print(type(d),d)

e = complex(b,d)
print(type(e),e)

#Boolean
yes = True
no = False
int_yes = int(yes)
int_no = int(no)
print(yes,no,int_yes,int_no)

#Tuple, Strings, Sets, Lists and Range fall under sequence data types
##Tuple, Strings, Sets, Lists have been discussed in detail

#Range
r = range(1,10)
print(type(r),":",r,":",list(r))
r1 = range(2,11,2)
print(list(r1))

#Dictionary -- Consists of a key-value pair
##Example -- To map out words and their occurances in a paragraph

words_dict = {'the':56,'be':27,'to':19,'of':15}
print(words_dict,type(words_dict))
print(tuple(words_dict),words_dict.values())
print('the',words_dict['the'])
print('be',words_dict.get('be'))
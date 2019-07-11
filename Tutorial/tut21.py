'''Program to find if the given number is prime or not'''

lst = []
num = int(input("Enter a positive integer to prime or composite:\n"))
flag=0
for i in range(1,int(num/2),1):
    if num%i==0:
        flag+=1
        lst.append(i)

if flag>1:
    print("Given number",num,"is composite.",lst)
else:
    print("Given number",num,"is prime.")
    
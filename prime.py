import math
flag=0
number=int(input("enter the number:"))
for i in range(2,int(math.sqrt(number))):
    if(number%i==0):
        flag=1
        break
    else:
        flag=0
if(flag==0):
    print("prime number")
else:
    print("not a prime")

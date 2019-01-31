num=int(input("enter the number"))
temp=num
r=0
sum=0
while num>0:
    r=num%10
    sum=sum+(r**3)
    num=num//10
if(sum==temp):
    print("Armstrong")
else:
    print("Not an armstrong")

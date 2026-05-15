a=int(input("enter the number"))
c=a
b=0
while(a>0):
    b=b+1
    a=a//10
if(b%2==0):
    k=c
    d=k%int(pow(10,b//2))
    e=k//int(pow(10,b//2))
    f=(d+e)*(d+e)
if(f==c):
    print("it is a tech number")
else:
    print("it is not a tech number")

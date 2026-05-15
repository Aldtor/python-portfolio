a=int(input("Enter the number:- "))
c=0
d=1
while (a>0):
    b=a%10
    c=c+b
    d=d*b
    a=a//10
if(c==d):
    print("spy number")
else:
    print("not spy number")
    


a=int(input("Enter the number :- "))
ev=0
od=0
b=0
while(a>0):
    b=a%10
    if(b%2==0):
        ev=ev+b
    else:
        od=od+b
    a=a//10
if(od==ev):
    print("Yes Lead Number")
else:
    print("Not A Lead Number")

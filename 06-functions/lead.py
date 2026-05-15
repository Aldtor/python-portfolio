a=int(input("Enter the number :- "))
x=0
y=0
b=0
while(a>0):
    b=a%10
    if(b%2==0):
        x=x+b
    else:
        y=y+b
    a=a//10
if(y==x):
    print("Yes Lead Number")
else:
    print("Not A Lead Number")

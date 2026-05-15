#SPECIAL NUMBER
b=d=0
a=int(input("Enter a number :- "))
c=a
v=1
h=0
while(c>0):
    v=1
    d=c%10
    for i in range(1,d+1):
        v=v*i
    h=h+v
    c=c//10
if(h==a):
    print("The number is a special number")
else:
    print("The number is not a special number")

'''x=int(input("Enter the number"))
c=0
g=str(x)
e=len(g)
b=0
k=1
f=0
for i in range(e):
    b=x%10
    f=f+b
    k=k*b
    x=x//10
if (f==k):
    print("spy number")
else:
    
    print("not a spy number")'''
a=int(input("Enter the number:- "))
c=0
d=1
while (a>0):
    b=a%10
    c=c+b
    d=d*b
    a=a//10
if (c==d):
    print("spy number")

else:
    print("not a spy number")
        

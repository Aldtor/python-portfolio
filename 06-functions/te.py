import math as m
a=int(input("Enter a Number"))
fh=sh=c=d=0
c=a
while(a>0):
    d=d+1
    a=a//10
if(d%2==0):
    fh=c//m.pow(10,d//2)
    sh=c%m.pow(10,d//2)
    e=(fh+sh)*(fh+sh)
if(e==c):
    print("yes tech number")
else:
    print("Not a tech number")

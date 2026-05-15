x=int(input("enter the number"))
p=x
s=0
while(x>0):
    t=x%10
    e=t*t*t
    s=s+e
    x=x//10
if(s==p):
    print("yes it is armstrong")
else:
    print("not armstrong")

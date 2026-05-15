def armstrong(a):
    x=a
    s=0
    e=0
    while(x>0):
        t=x%10
        e=t*t*t
        s=s+e
        x=x//10
    if(s==a):
        return(1)
    else:
        return(2)
n=int(input("Enter a number.."))
b=armstrong(n)
if(b==1):
    print("Haa armstrong hai")
else:
    print("No Armstrong")

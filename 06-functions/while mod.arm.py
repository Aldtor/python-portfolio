def arm(a):
    d=0
    s=0
    k=a
    while (a>0):
        b=a%10
        d=b*b*b
        s=s+d
        a=a//10
    if(s==k):
        print("IT is a armstrong")
    else:
        print("IT is not armstrong")
x=int(input("Enter a value"))
arm(x)
        
    
    

def arm(a):
    d=0
    s=0
    v=str(a)
    for i in v:
        b=int(i)
        d=b*b*b
        s=s+d
    if(s==a):
        print("IT is a armstrong")
    else:
        print("IT is not armstrong")
x=int(input("Enter a value"))
arm(x)

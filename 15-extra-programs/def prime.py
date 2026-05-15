def prime(a):
    c=0
    for i in range(1,a+1):
        if(a%i==0):
            c=c+1
    return(c)
x=int(input("Enter the number :- "))
k=prime(x)
if(k==2):
    print("Prime Number")
else:
    print("Not a Prime Number")
    

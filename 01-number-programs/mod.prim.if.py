def prim(x):
    c=0
    for i in range(1,x+1):
        if(x%i==0):
            c=c+1
    if(c==2):
        print("IT IS A PRIME NUMBER")
    else:
        print("IT IS NOT A PRIME NUMBER")
x=int(input("Enter a number :- "))
prim(x)


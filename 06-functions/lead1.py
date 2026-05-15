a=int(input("Enter the number :- "))
b=str(a)
n=0
g=0
for i in b:
    i=int(i)
    if(i%2==0):
        n=n+i
    else:
        g=g+i
if(g==n):
    print("Yes Lead Number")
else:
    print("Not A Lead Number")

    

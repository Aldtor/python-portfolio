n=int(input("Enter the number ==> "))
a=0
b=1
print(a,b,end=' ')
c=1
for i in range(n+1):
    if(c<=n):
        print(c,end=' ')
        a=b
        b=c
        c=a+b
    
    
    

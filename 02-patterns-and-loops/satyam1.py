ans="y"
while(ans=='y'):
    c=0
    a=int(input("Enter the number"))
    for i in range(1,a+1):
        if(a%i==0):
            c=c+1
    if(c==2):
        print("prime number")
    else:
        print("not a prime number" )
    ans=input("Do you Want to continue(y/n)")
        
    

    

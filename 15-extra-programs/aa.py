def prime(): #1
    c=0
    a=int(input("Enter The Number (for Prime) :- "))
    for i in range(1,a+1):
        if(a%i==0):
            c=c+1
    if(c==2):
        print("It is a Prime Number.")
    else:
        print("It is not a Prime Number.")
prime()

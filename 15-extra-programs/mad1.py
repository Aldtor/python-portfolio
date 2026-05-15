import satyammodule
u=int(input("Enter any Number"))
b=satyammodule.prime(u)
if(b==2):
    print("Yes Prime")
else:
    print("No prime")
c=satyammodule.armstrong(u)
if(c==1):
    print("Yes armstrong")
else:
    print("No Armstrong")

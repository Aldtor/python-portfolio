a=eval(input("Enter elements in a tuple :- "))
x=list(a)
f=e=0
for i in x:

    c=i
    while(i>0):
        e=i%10
        f=f+(e*e*e)
        i=i//10
    if(c==f):
        print("yes ArmStrong")
    else:
        print("No ArmStrong")
    e=f=i=0  '''  
        
        
    
    
    
    

    

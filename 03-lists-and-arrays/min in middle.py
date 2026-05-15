tup=eval(input("Enter the tuple :- "))
ln=len(tup)
lies=False
mn=min(tup)
if ln%2==0:
    half=ln//2
    if mn==tup[half] or mn==tup[half-1]:
        lies=True
else:
    half=ln//2
    if mn==tup[half]:
        lies=True
if lies==True:
    print("minimum lies at tuple's middle.")
else:
    print("minimum doesn't lies at tuple's middle.")
    

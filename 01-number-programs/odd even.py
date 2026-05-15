a=[]
a=eval(input("Enter the list"))
ev=[]
od=[]
for i in a:
    if(i%2==0):
        ev.append(i)
    else:
        od.append(i)
print(ev)
print(od)

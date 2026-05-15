x=int(input("Enter a number"))
t=x
c=0
l=len(str(x))
for i in range(0,l):
    b=x%10
    c=c*10+b
    x=x//10
print(b,"b")
print(c,"c")
print(x,"x")
if(t==c):
    print("yes palendrome")
else:
    print("not palendrome")

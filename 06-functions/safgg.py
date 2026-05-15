a=int(input("Enter the number :- "))
c=0
for i in range(1,a):
    if a%i==0:
        c=c+i
if c==a:
    print("Perfect Number")
else:
    print("Not Perfect Number")
   

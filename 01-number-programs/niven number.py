'''a=int(input("Enter the number:- "))
b=a
d=0
while (a>0):
    c=a%10
    d=d+c
    a=a//10
print("the sum of digits of the number:- ",d)
print("the dividing of the number by their sum :- ",b/d)
if b%d==0:
    print("it is niven number")
else:
    print("it is not niven number")'''
a=int(input("Enter the number:- "))
n=a
d=str(a)
b=len(d)
e=0
for i in range(b):
    c=a%10
    e=e+c
    a=a//10
print("the sum of digits of the number:- ",e)
print("the dividing of the number by their sum :- ",n/e)
if n%e==0:
    print("it is niven number")
else:
    print("it is not niven number")

    

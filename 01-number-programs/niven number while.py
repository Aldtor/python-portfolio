a=int(input("Enter the number :- "))
c=0
h=a
while(a>0):
    b=a%10
    c=c+b
    a=a//10
if(h%c==0):
    print("IT IS A NIVEN NUMBER")
else:
    print("IT IS NOT A NIVEN NUMBER")

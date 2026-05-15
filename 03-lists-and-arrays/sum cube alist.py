val=eval(input("Enter a list:- "))
alist=[]
s=len(val)
print(s)
for i in range(s):
    num=val[i]
    csum=0
    print(num)
    while num:
        dig=num%10
        csum+=(dig*dig*dig)
        num=num//10
    if csum==val[i]:
        alist.append(val[i])
print(alist)
print("Largest number(= sum of its digits'cubes):- ",max(alist))
print("Smallest number(= sum of its digits' cubes):-",min(alist))

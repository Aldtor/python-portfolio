L=[2,5,7,5,4,1]
pos=0
sum1=0
while pos<len(L):
    if L[pos]%2==1:
        sum1=sum1+L[pos]
    pos=(pos+1)
print(sum1)

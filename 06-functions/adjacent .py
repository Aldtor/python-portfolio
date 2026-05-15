'''a=[6,8,4,5,9,1]
s=len(a)
temp=0
for i in range(0,s):
    for j in range(0,s-1):
        print(i)
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)'''

a=[3,7,9,8,4,7,2]
s=len(a)
temp=0
for i in range(0,s):
    for j in range(0,s-1):
        if a[j]<a[j+1]:
            temp=a[j+1]
            a[j+1]=a[j]
            a[j]=temp
print(a)

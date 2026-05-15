lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
'''slc1=lst[5:15:2]
slc2=lst[::4]
sam=avg=0
print(slc1)
print(slc2)
print("Sclice 1")
for a in slc1:
    b=int(a)
    sam+=b
    print(sam,end=' ')
print()
print("Sum of element of sclice 1 :- ",sam)
print("Sclice 2")
sam=0
for a in slc2:
    c=int(a)
    sam+=c
    print(sam,end=' ')
print()
avg=sam/len(slc2)
print("Average of elements of slice 2 :- ",avg)'''

b=lst
print(b)
print(lst)
lst[6]=3
k=list(lst)
print(k)
n=list(b)
print(n)

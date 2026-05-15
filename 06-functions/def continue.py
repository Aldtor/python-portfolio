'''def Total (Num=7):
    Sum=0
    for c in range(1,Num+1):
        if c%2!=0:
            pass
            #continue
        Sum+=c
    return Sum
print(Total(3),end="$")
print(Total(),sep="@")'''

def CountWords():
    fh=open("C:\\Users\\dell\\Desktop\\decode.txt")
    s=fh.read().split()
    for i in s:
        if (len(i)>=5):
            b=b+1
    print("Bigger Word",b)

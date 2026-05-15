fh=open("C:\\Users\\dell\\Desktop\\sam.txt","r").readline()
print("             choice 1=rstrip")
print("             choice 2=lstrip")
ch=int(input("enter the choice"))
if (ch==1):
    a=fh.rstrip('\n')
    print(a)
if(ch==2):
    b=fh.lstrip()
    print(b)


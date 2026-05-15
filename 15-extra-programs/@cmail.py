fh=open("C:\\Users\\dell\\Desktop\\studendetil.txt",'r')
c=fh.read().split(" ")
for i in c:
    if i.startswith("@"):
        print("Word ==> ",i)
fh.close()

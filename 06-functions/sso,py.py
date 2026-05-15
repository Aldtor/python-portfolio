fh=open("C:\\Users\\dell\\Desktop\\sam.txt","r")
a=" "
while a:
    a=fh.readline()
    for b in a.split():
        print(b,end='$')
    print()
fh.close()
    

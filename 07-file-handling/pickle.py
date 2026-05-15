import pickle
a={}
fh=open("C:\\Users\\dell\\Desktop\\stu.dat",'wb')
ch='y'
while ch=='y':
    b=input("enter the name")
    c=int(input("enter the roll no."))
    d=int(input("enter the admission no."))
    e=float(input("enter the percentage"))
    a['NAME']=b
    a['ROLL NO.']=c
    a['ADMISSION NO.']=d
    a['PERCENTAGE']=e
    pickle.dump(a,fh)
    ch=input("want to enter more records(y/n)...")
fh.close()

import json
fh=open("C:\\Users\\dell\\Desktop\\somya.txt","r")
'''a=fh.read()
print(a)
a1=fh.read(30)
print(a1)
a2=fh.readline()
print(a2)'''
a3=fh.readlines()
print(json.dumps(a3))

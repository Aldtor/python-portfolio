import pickle
a={}
fh=open("C:\\Users\\dell\\Desktop\\stu.dat",'rb')
try:
    while True:
        a=pickle.load(fh)
        print(a)
except EOFError:
    fh.close()

import pickle
fh=open("C:\\Users\\dell\\Desktop\\emp.dat","rb")
try:
    while True:
        a=pickle.load(fh)
        print(a)
except EOFError:
    print()
fh.close()

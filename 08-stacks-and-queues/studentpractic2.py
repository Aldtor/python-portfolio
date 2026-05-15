fh=open("C:\\Users\\dell\\Desktop\\studendetil.txt",'w')
z="SNo."+"\t"+"Name"+"\t"+"Class"+"\t"+"Roll"+"\t"+"Fee"
n=int(input("Enter The No. Of Records ==> "))
for i in range(n):
    no=int(input("Enter The SR No. ==> "))
    a=input("Enter The Name Of The Student ==> ")
    b=int(input("Enter The Class Of The Student ==> "))
    c=int(input("Enter The Roll No. Of The Student ==> "))
    d=int(input("Enter The Fees Of The Student ==> "))
    z1="no"+"\t"+a+"\t"+"b"+"\t"+"c"+"\t"+"d"
    fh.write(z1)
    fh.write("\n")
print("** Success **")
fh.close()

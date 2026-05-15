fh=open("C:\\Users\\dell\\Desktop\\som.txt","w")
heading="NAME"+"\t"+"ROLL"+"\t"+"FEE"+"\t"+"Percentage"
fh.write(heading)
fh.write("\n")
n=int(input("enter the no. of details you want to add"))
for i in range(n):
    nm=input("enter the name")
    rl=int(input("enter the roll number"))
    fee=float(input("enter the fee"))
    percent=float(input("enter the percentage"))
    m=nm+"\t"+str(rl)+"\t"+str(fee)+"\t"+str(percent)
    fh.write(m)
    fh.write("\n")
fh.close()

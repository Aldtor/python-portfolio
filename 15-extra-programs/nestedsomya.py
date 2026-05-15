for i in range (1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")
for i in range (1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print("\n")
for i in range (1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")

for i in range (1,6):
    for j in range(1,i+1):
        print("*",end=" #")
    print("\n")
for i in range (1,6):
    for j in range(1,i+1):
        if(j%2!=0):
            print("*",end=" ")
        else:
            print("#",end=" ")
    print("\n")

k=1;
for i in range (1,6):
    for j in range(1,i+1):
        print(k,end=" ")
        k=k+1
    print("\n")




















print("Finding Greatest Number")
print("Lets Begin....")
a=int(input("How many numbers do you want to input? "))
if a > 0:
    #b=float('-inf')
    b=1
    for i in range(a):
        c=float(input(f"Enter number {i + 1}: "))
        if c>b:
            b=c
    print("The greatest number entered is:",b)
else:
    print("Please enter again. ")


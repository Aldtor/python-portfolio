'''def and_truth_table():
    print("A      |B       |A AND B")
    print("_ _ _ _ |_ _ _ _|_ _ _ _")
    for a in[True,False]:
        for b in [True,False]:
            print(f"{a}|{b}|{a and b}")




if _name_=="_main_":
    and_truth_table()'''

'''print("A      | NOT A")
print("-------|---------")
for a in [True, False]:
        c=(not a)
        print(f"{a}   |{c}")'''
a5=int(input("enter the number"))
if(a5>1):
        for i in range(2,(a5//2)+1):
                if(a5%i==0):
                        print("it's NOT a prime number")
                else:
                        print("it's a prime number")




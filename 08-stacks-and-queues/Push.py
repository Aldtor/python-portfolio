def PUSH(Value,li):
    sk=[1,2,3,4,5]
    if(len(sk)>=li):
        print("Over Flow")
    else:
        sk.append(Value)
    print(sk,Value)

li=int(input("Enter The Limit ==> "))
va=input("Enter The Value To Be Added ==> ")
PUSH(va,li)

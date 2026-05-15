a={1:['somya','satyam'],2:['jatin','satvik']}
ch=int(input("Enter the keys"))
if ch in a.keys():
    a.pop(ch,-1)
    print(a)
else:
    print("not found")
    print(a)

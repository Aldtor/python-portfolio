import json
sentence="This is a super idea This \n idea will change the idea of learning"
words=sentence.split()
print(words)
d={}
for one in words:
    key=one
    if key not in d:
        count=words.count(key)
        print(count)
        d[key]=count
print("counting frequencies in list\n",words)
print(json.dumps(d,indent=1))



'''import json
sentence=input("Enter the sentence")
words=sentence.split()
print(words)
d={}
for one in words:
    key=one
    if key not in d:
        count=words.count(key)
        print(count)
        d[key]=count
print("counting frequencies in list\n",words)
print(json.dumps(d,indent=1))'''

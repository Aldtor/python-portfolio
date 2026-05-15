Employee={'John':{'age':25,'salary':25000},'Diya':{'age':22,'salary':22000},'Harshit':{'age':25,'salary':25000},'Himanshu':{'age':24,'salary':24000},'Ankit':{'age':29,'salary':29000}}
for key in Employee:
    print('='*100)
    print("Employee :- ",key,":")
    print("Age :- ",str(Employee[key]['age']))
    print("Salary :- ",str(Employee[key]['salary']))
    print('='*100)
    

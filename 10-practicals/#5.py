#5. Write a program to generate values from 1 to 10 and then remove all the odd numbers from the list.

num1 = []
for i in range(1, 11):
    num1.append(i)
print("Numbers from 1 to 10:\n", num1)
num1 = [i for i in num1 if i % 2 == 0]
print("The values after removing odd numbers:\n", num1)

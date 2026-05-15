#10. Write a program to get five marks using list and display the marksin pie chart.

import matplotlib.pyplot as plt
marks = []
i = 0
subjects = ["Tamil", "English", "Maths", "Science", "Social"]
while i < 5:
    marks.append(int(input(f"Enter Mark for {subjects[i]}: ")))
    i += 1
for j in range(len(marks)):
    print(f"{j+1}. {subjects[j]} Mark = {marks[j]}")
plt.pie(marks, labels=subjects, autopct="%.2f%%")
plt.gca().set_aspect("equal")
plt.title("Marks Distribution")
plt.show()

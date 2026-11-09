import matplotlib.pyplot as plt

# exams = [1, 2, 3, 4, 5]
# marks = [70, 75, 80, 78, 85]


# plt.plot(exams, marks, marker='o', color='y', linestyle='-')
# plt.xlabel('Exams')
# plt.ylabel('Marks')
# plt.title('Exam Performance')
# plt.show()

exams=["aman","jdicj","gfydgu","wdgwu","wuichicj"]
marks=[67,43,67,13,13]


plt.bar(exams, marks, color='b')
plt.xlabel('Exams')
plt.ylabel('Marks')
plt.title('Exam Performance')
plt.show()
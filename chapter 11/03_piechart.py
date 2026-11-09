# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# subjects=['maths','english','hindi','science']
# marks=[90,63,92,94]

# plt.pie(marks,labels=subjects)
# plt.show()


import matplotlib.pyplot as plt
subjects = ['Math','Physics','Chemistry','English']
student1 = [85, 78, 88, 90]
student2 = [80, 82, 85, 87]
plt.plot(subjects, student1, label='Student 1')
plt.plot(subjects, student2, label='Student 2')
plt.title('Marks Comparison')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.legend()
plt.show()
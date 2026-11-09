import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# subjects=['maths','english','hindi','science']
# marks=[90,93,92,94]

# # plt.bar(subjects,marks)
# plt.bar(subjects,marks)

# plt.show()





# HISTOGRAMMMMM

marks50=np.random.randint(1,100,(50))
print(marks50)

# plt.hist(marks50)
# plt.show()

bins=np.arange(0,100,5)

plt.hist(marks50,bins=bins)
plt.xticks(np.arange(1,100,5))
plt.show()
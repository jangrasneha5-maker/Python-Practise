import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# scatter graph
# rollno=[1,2,3,4,5,6,7,8,9,10]
# marks=[10,20,30,40,50,60,70,80,90,100]

# plt.figure(figsize=(5,5))
# plt.scatter(rollno , marks)

# # plt.scatter(rollno , marks,color='green',marker='^')
# plt.show()


temperature_pune=[25,34,21,45,36,47,6,4]
humidity_pune=[28,25,29,52,51,43,45,39] 

temperature_bangalore=[24,53,24,41,32,44,63,8]
humidity_bangalore=[20,34,65,53,50,42,44,38] 

plt.figure(figsize=(8,8))
plt.plot(temperature_pune,humidity_pune , color='red',marker='^')
plt.show()




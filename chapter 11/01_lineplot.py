import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# rollno=[1,2,3,4,5,6,7,8,9,10]
# marks=[10,20,30,40,50,60,70,80,90,100]

# plt.plot(rollno,marks,'r-' , linestyle = "-.")
# plt.show()

# linestyle:
# default -
# dotted :
# dashed -
# none  isse kuch nhi hoggaaaa mtlb blank sheet hi khulegi


study=[1,2,3,4,5,6,7,9,10]
mark=[10,9,9,8,7,4,2,3,5]

plt.figure(figsize=(5,5))
plt.xticks((np.arange(0,15,1)))  # range h yeh 1 to 15 with gap of one
plt.yticks((np.arange(0,100,5)))

plt.plot(study,mark,'r-')
plt.xlabel('study')
plt.ylabel('mark')
plt.show()




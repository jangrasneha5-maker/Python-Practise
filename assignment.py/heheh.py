import numpy as np
import time
size = 1000000
arr = np.arange(size)
start = time.time()
python_list = [x + 2 for x in range(size)]
print(time.time() - start)
start = time.time()
numpy_arr = arr + 2
print(time.time() - start)
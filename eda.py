import numpy as np


data = np.array([[1,2],
                 [3,4],
                 [5,6]])

min_val = np.min(data, axis=0)

max_value = np.max(data, axis=0)

select_data = (data - min_val) / (max_value - min_val)

print(select_data)
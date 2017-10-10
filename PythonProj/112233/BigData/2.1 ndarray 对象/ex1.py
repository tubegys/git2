import numpy as np
height = [1, 2, 3, 4]
weight = [2, 3, 4, 5]
np_height = np.array(height)
np_weight = np.array(weight)
np_BMI = np=height/np_weight**2
print(np_BMI)
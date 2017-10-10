# 随机数
import numpy as np
from numpy import random as nr
np.set_printoptions(precision=2)
r1 = nr.rand(4, 3)  # 产生0-1随机浮点数
r2 = nr.randn(4, 3)  # 产生标准正态分布随机数
r3 = nr.randint(0, 10, (4, 3))  # 产生0-10中不包含10的随机数
print(r3)

ztfb = nr.normal(100, 10, (4, 3))
jyfb = nr.uniform(10, 20, (4, 3))
psfb = nr.poisson(2.0, (4, 3))
print('ztfb', ztfb)
print('jyfb:', jyfb)
print('psfb:', psfb)
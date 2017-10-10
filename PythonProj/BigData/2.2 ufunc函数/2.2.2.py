# 2.2.2 比较运算和布尔运算
import numpy as np
x1 = np.array([2, 3, 6, 1, 2])
x2 = np.array([3, 10, 4, 5, 6])
x3 = x1 == x2
x4 = np.equal(x1, x2)
print(x3, x4)

x5 = np.logical_or(x1 == x2, x1 > x2)
print(x5)
print(np.any(x1 == x2))  # 任意x1元素与x2元素相等，返回TRUE （相同下标元素）
print(np.all(x1 > x2))  # 任意x1元素和x2比，x1 > x2 返回TRUE
print(np.bitwise_or(x1 == x2, x1 > x2))  # 含义：x1和x2元素比较，大于等于的为TRUE

# 2.2 ufunc函数
import numpy as np
import math
a = np.linspace(0, 2*np.pi, 9)
x = np.linspace(0, 360, 9)
print('x=', x)
print('a=', a)
b = np.sin(a)  # 注意这里是sin是计算弧度的
print(b)

print('item方法：')
c = np.arange(6.0).reshape(2, 3)
print(c)
print(c.item(1, 2))  # 通过item方法，将numpy类型直接转换成python标准的数值类型
print('type(c.item(1, 2):', type(c.item(1, 2)))
print('type(c[1, 2]:', type(c[1, 2]))


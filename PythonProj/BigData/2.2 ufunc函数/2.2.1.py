# 2.2.1 s四则运算
import numpy as np
a = np.arange(0, 4)
b = np.arange(1, 5)
c = np.add(a, b)
print('a=', a)
print('b=', b)
print('c=a+b:', c)
d = a + b  # 可以进行如下简化
print(d)

e = np.true_divide(a, b)
print('e=', e)

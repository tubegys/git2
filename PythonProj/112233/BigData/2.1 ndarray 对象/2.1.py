# 2.1.1 创建
import numpy as np
print('查看版本：')
print(np.__version__)  # 查看numpy的版本
print('创建数组：')
a = np.array([1, 2, 3, 4])
b = np.array((5, 6, 7, 8))
c = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])
print('a:', a)
print('b:', b)
print('c:', c)
print('查看数组的形状：shape属性')
print('a.shape:', a.shape)
print('b.shape:', b.shape)
print('c.shape:', c.shape)
print('改变数组的形状:')
c.shape = (4, 3)
print('c:', c)
c.shape = (3, -1)  # 设置某个轴元素个数为-1  将自动计算此轴长度
print(c)
print('使用reshape方法创建指定形状的新数组:')
d = a.reshape(2, 2)
print('d:', d)
print('使用reshape创建的新的数组和原来的数组共享用一个内存：')
a[1] = 100
print('a:', a)
print('d:', d)

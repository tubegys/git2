# 2.1.4 存取元素
import numpy as np
a = np.arange(10)
print('a=', a)
print('数组的存取：')
print('a[5]=', a[5])
print('a[3:5]=', a[3:5])  # 不包含右值
print('a[:5]=', a[:5])
print('a[:-1]=', a[:-1])
print('a[1:-1:2]=', a[1:-1:2])
print('a[::-1]=', a[::-1])
print('a[5:1:-2]=', a[5:1:-2])

b = a[3:7]  # b 和 a 共享内存，b只是a的一个视图
print('b=', b)
b[2] = 100
print('b=', b)
print('a=', a)

x = np.arange(10, 1, -1)
print('x=', x)
print('x[[3, 3, 1, 8]]=', x[[3, 3, 1, 8]])
print('x[np.array([3, 3, 1, 8])]=', x[np.array([3, 3, 1, 8])])
print('x[np.array([[3, 3, 1, 8], [3, 3, -3, 8]])]=', x[np.array([[3, 3, 1, 8], [3, 3, -3, 8]])])
# 得到多维数组

m = np.arange(5, 0, -1)
print('m=', m)
arr_bool = m[np.array([True, False, True, False, False])]
print('arr_bool=', arr_bool)
print(m[[True, False, True, False, False]])
rand = np.random.randint(0, 10, 6)
print(rand)
print(rand[rand > 3])

# 学习总结
# 1.通过切片的方式，存取数组
# 2.可以通过数组（可以多维）的方式，存取数组
# 3.bool数组的试使用

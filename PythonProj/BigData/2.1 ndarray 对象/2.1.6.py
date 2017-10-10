# 2.1.6 结构数组
import numpy as np
persontype = np.dtype({
    'names': ['name', 'age', 'weight'],
    'formats': ['S30', 'i', 'f']}, align=True)
a = np.array([('zhangsan', 32, 75.5), ('wang', 24, 65.2)], dtype=persontype)
print(a)
print(a.dtype)
print('a[0]=', a[0])
print("a[0]['name']=", a[0]['name'])

print('下标获取的新数组，共享内存：')
c = a[0]  # c 和 a 共享内存
c['name'] = 'li'
print(a)
b = np.array([1, 2, 3])
print('b=', b)
b.tofile('b.bin')
a.tofile('test.bin')
# print(a.tostring())
print(a.flags)

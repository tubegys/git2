# 2.1.2 元素类型
import numpy as np
print('查看数组类型：')
a = np.array([1, 2, 3, 4])
print(a.dtype)
print('使用dtype参数指定创建数组的类型：')
ai32 = np.array([1, 2, 3, 4], dtype=np.int32)
af = np.array([1, 2, 3, 4], dtype=np.float)
ac = np.array([1, 2, 3, 4], dtype=np.complex)
print('ai32:', ai32.dtype)
print('af:', af.dtype)  # 64位双精度浮点类型
print('ac:', ac.dtype)  # 128位双精度复数类型

print([key for key, value in np.typeDict.items() if value is np.float64])
print(set(np.typeDict.values()))

num_a = np.int16(200)
print(num_a*num_a)  # 精度溢出

print('使用astype方法可以对数组的元素类型进行转换')
t1 = np.array([1, 2, 3, 4], dtype=np.float)
t3 = t1.astype(np.int32)
print('t1:', t1.dtype)
print('t3:', t3.dtype)

# 学习总结
# 1.查看数组类型
# 2.创建指定数据类型的数组
# 3.用astype方法对数组元素类型进行转换



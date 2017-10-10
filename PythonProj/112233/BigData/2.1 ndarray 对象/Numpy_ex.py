import numpy as np
a = np.array([[1, 2, 3], [2, 3, 4]], dtype=int)
# 通过创建序列，然后使用array函数来创建数组，dtype可以指定元素类型（float，int，complex……）
print("L1:\n", a)
print('L2:\n', a.shape)
a.shape = (6, )  # 可以改变轴的长度，通过改变shape的值（元组形式），数量要保持一致
print('L3:\n', a)
b = a.reshape(3, 2)  # b 和 a 共享内存，改变任意一个就会同时改变，reshape方法创建一个改变了尺寸的数组
b[0][1] = 100
print("L4:\n", b)
print('L5:\n', a)

# -----------------------------------------------------------------------
# 以上都是先创建一个Python序列， 然后通过array函数转换为数组。这样做效率不高。
# 下面用numpy提供的接口函数创建数组
# -----------------------------------------------------------------------

# 第一组 等差等比
c = np.arange(1, 10, 1)  # 第一个参数为开始值，第二个参数是终值，第三个参数为步长，注意：数组是不包含终值的
print('L6:\n', c)
d = np.linspace(1, 16, 5)
# 告诉他等差数列的首项，末项，数组的元素个数，就可以算出公差（通项公式：an = a1 + (n-1)*d），得到一个等差的数列
print('L7:\n', d)
e = np.logspace(1, 4, 4)
# 参数类似于linspace，创建一个等比数列（通项公式百度吧！）
# 其中第一个参数为 10^x ，第二个参数为10^y，第三个参数是数组元素的个数
print('L8:\n', e)

# 第二组 from
string = 'abcdefgh'
f = np.fromstring(string, dtype=np.int8)  # 字符串转换成ASCII
print('L9:\n', f)

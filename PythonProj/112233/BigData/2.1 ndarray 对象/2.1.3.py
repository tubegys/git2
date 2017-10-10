# 2.1.3 自动生成数组
import numpy as np
print('等差数组：arange')
a = np.arange(0, 1, 0.1)  # 起始值，终值，步长（不包含终值）
print('a:', a)
print('linspace创建等差数列:')
b = np.linspace(0, 1, 10)  # 起始值，终值，元素个数，默认包含终值
print('包含终值：', b)
c = np.linspace(0, 1, 10, endpoint=False)
print('不包含终值：', c)

print('logspace生成等比数列：')
d = np.logspace(0, 2, 5)  # 起始值，终值，元素个数
print('d:', d)
print('指定比例为5：')
e = np.logspace(0, 2, 3, base=5)
print('e:', e)

print('zeros,ones,empty函数：')
f = np.zeros((2, 3), dtype=np.int)
g = np.ones((3, 2), dtype=np.int)
h = np.empty((3, 3))
print('zeros:', f)
print('ones:', g)
print('empty:', h)  # empty 生成的是随机的数字

print('zeros_like,empty_like,ones_like:')
arr_like_int = np.array([[1, 2, 3, 4], [2, 3, 4, 5]], dtype=np.int)
arr_like_float = np.array([[3, 4, 5, 6], [11, 22, 33, 44], [77, 66, 55, 99]], dtype=np.float)
i = np.zeros_like(arr_like_int)
j = np.ones_like(arr_like_float)
print('i:', i)
print('j:', j)

print('frombuffer,fromstring,fromfile的使用：')
# frombuffer和fromstirng的区别在于
# frombuffer创建的数组和原始字符串共享内存，fromstring会对字符串的字节序进行复制
st = 'abcdefgh'
k = np.fromstring(st, dtype=np.int8)
print('fromstring:', k)
# l = np.frombuffer(st)


def func(num):
    return num % 4 + 1

m = np.fromfunction(func, (2, ))
print('m:', m)


# 打印99乘法表
def func2(num1, num2):
    return (num1+1)*(num2+1)
n = np.fromfunction(func2,(9, 9))
print('n:', n)

# 学习总结
# 1.arange,linspace,logspace
# 2.zeros,empty,ones & zeros_like,empty_like,ones_like
# 3.fromstring,frombuffer,fromfile

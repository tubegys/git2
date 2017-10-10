import numpy as np


def fun_square(x):
    y = x**2
    return y

ufunc_square = np.frompyfunc(fun_square, 1, 1)
a = np.arange(10)
print(a)
b = ufunc_square(a)
print(b)

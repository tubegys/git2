import os, glob
print(os.getcwd())  # 获得当前工作路径
# os.chdir('E:/')  # 更换工作路径
# print(os.getcwd())

print(os.path.join('E:\PythonProj\ex_datetime', 'ex_1.py'))  # 将参数整合成一个路径的形式
print(os.path.expanduser('~'))  # 获得当前系统的根目录
print(os.path.join(os.path.expanduser('~'), 'examples', 'ex_1.py'))
path = os.path.join(os.path.expanduser('~'), 'examples', 'ex_1.py')
print(os.path.split(path))  # 分解路径，得到路径和文件名
(pathname, filename) = os.path.split(path)
print(pathname, "----", filename)
shortName, extension = os.path.splitext(filename)  # 分解文件名，得到文件名 和 文件后缀
print(shortName, "    ", extension)

# 总结：
# <1> os模块可以操作文件工作路径：os.getcwd()  os.chdir()
# <2>os.path模块可以对文件路径进行相关操作  os.path.join()  os.path.expanduser()  os.path.split()  os.path.splitext()
print("-----------------分割线---------------------------------")
# ----------------------分割线---------------------------------
print(glob.glob('*.py'))  # 获得当前路径下 所有.py的文件，以列表的形式返回

f = glob.iglob('*.py')  # iglob返回一个迭代器
print(f)
for py in f:
    print(py)

# 总结：glob模块可以使用shell风格的通配符, 有2个方法：glob 和 iglob

print("-----------------分割线---------------------------------")
# ----------------------分割线---------------------------------

realpath_list = [os.path.realpath(f) for f in glob.glob("*.py")]
# realpath 返回当前目录下文件的路径
# 通过列表的解释器，完成了显示当前目录下所有py文件的路径
print(realpath_list)

larger_600_list = \
    [(q, os.stat(q).st_size) for q in glob.glob("*.py" ) if os.stat(q).st_size > 152]
# os.stat().st_size 字节数，返回在当前路径下 py文件大于152个字节的列表
print(larger_600_list)

# 总结：列表解析器可以通过for语句去循环遍历，if语句进行过滤

import re

s = 'NORTH BROAD ROAD'
s1 = re.sub('ROAD$', 'RD.', s)
print(s1)
# $ 表示“字符串结尾”。（还有一个相应的表示“字符串开头”的字符 ^ ）。
# 正则表达式模块的re.sub()函数可以做字符串替换，它在字符串s中用正则表达式‘ROAD$’来搜索并替换成‘RD.’
# 它只会匹配字符串结尾 的‘ROAD’，而不会匹配到‘BROAD’中的‘ROAD’，因为这种情况它在字符串的中间

ret = re.search('[0-9]{3}', 'a244')  # re模块search方法匹配正则表达式  参数1为正则表达式，参数2为待匹配的字符串
print(ret)  # search方法若匹配成功，则返回一个MATCH OBJECT对象，若没匹配成功，则返回NONE
print(ret.span())  # span 方法返回匹配到的范围
print(ret.group())  # group 方法返回匹配到的内容

MyPattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-([a-z]{0,3})$')
print(MyPattern.search('800-708-4569-gg').groups())


print('----------------------------------------------------------')
# ---------------------------分割线-------------------------------
pattern = '''^  # zhushi
        [0-9]{8}# it's explnation
        (re|r?x?x?) # dajsbdasbfb'''  # 松散正则表达式，允许写注释。注意要换行！在用search时要传入re.verbose
pattern_1 = '^[0-9]{8}'  # pattern和pattern_1是等价的
print(re.search(pattern, '54632148rxx', re.VERBOSE))




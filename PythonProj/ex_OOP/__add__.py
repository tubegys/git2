class Student(object):
    def __add__(self, other):
        return self.name + other.name

    def __init__(self,name, score):
        self.name = name
        self.score = score

zhangsan = Student('zhangsan', 18)
lisi = Student('lisi', 100)
total_score = zhangsan + lisi
print(total_score)
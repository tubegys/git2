class Rectangle(object):
    def __init__(self, x, y):  # init函数没有返回值
        self.x = x
        self.y = y

    def getPeri(self):
        return (self.x + self.y) * 2

    def getArea(self):
        return self.x * self.y

rect = Rectangle(3, 4)
print(rect.getPeri())
print(rect.getArea())


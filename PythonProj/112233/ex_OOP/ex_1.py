class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def show_info(self):
        print(self.__name, self.__age)


class MsStudent(Student):
    def __init__(self, score):
        self.__score = score

    def show_info(self):
        print(self.__name, self.__age, self.__score)


jack = Student('Jack', 24)
jack.show_info()
Kitty = MsStudent(75)


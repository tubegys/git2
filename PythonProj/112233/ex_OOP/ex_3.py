class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)

    def __init__(self, string):
        string += '123'
        print('i am init')

a = CapStr('I love You')
print(a)

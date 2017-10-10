class C:
    def __init__(self):
        print('i am __init__')

    def __del__(self):
        print('i am __del__')

c1 = C()
c2 = c1
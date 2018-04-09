
class MathFunctions:
    def __init__(self,x):
        self.x = x

    def f(self):
        return self.x*self.x

    def g(self):
        return 3*self.x+1

    def h(self):
        return self.g()+3

M = MathFunctions(5)

for i in range(0,10000):
    M.x = i
    print(M.f())
    print(M.g())
    print(M.h())



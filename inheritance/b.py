from a import A

class B(A):

    def __init__(self):
        self._y = 2

    def getY(self):
        return self._y

    def whoAmI(self):
        print "whoAmI(): Hi, I'm B"

    def getStatic(self):
        return A._z_static

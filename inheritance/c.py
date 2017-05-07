from a import A

class C():

    def __init__(self):
        pass

    def whoAmI(self):
        print "whoAmI(): Hi, I'm C"

    def getStatic(self):
        return A._z_static

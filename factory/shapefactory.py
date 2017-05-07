from circle import Circle
from box import Box

class ShapeFactory:

    shapes = {
        'circle': Circle(),
        'box' : Box()
    }

    def __init__(self):
        pass 

    def createShape(self, _type):
        return self.shapes.get(_type)

#!/usr/local/bin/python
from shapefactory import ShapeFactory 

def main():

    f = ShapeFactory()
    c = f.createShape('circle')
    b = f.createShape('box')

    c.display()
    b.display()

if __name__ == "__main__":
    main()

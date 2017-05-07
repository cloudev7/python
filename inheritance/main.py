#!/usr/local/bin/python

from a import A 
from b import B 
from c import C 

def main():
    o1 = B()
    o2 = C()

    o1.whoAmI()
    o1.getName()
    print "getY(): _y = " + str(o1.getY())
    print "static before: _z_static = " + str(A._z_static)
    A._z_static = 200
    print "static after: _z_static = " + str(A._z_static)
    print "static via B: _z_static = " + str(o1.getStatic())
    print "static via C: _z_static = " + str(o2.getStatic())
    print isinstance(o1, B)
    print isinstance(o1, A)
    print isinstance(o2, A)

if __name__ == "__main__":
    main()

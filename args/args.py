#!/usr/local/bin/python 


def test(*args):
    for key in args:
        print "%s" %(key)


if __name__ == "__main__":
    test(1,"two",0.234)

#!/usr/local/bin/python


def decorator(func):

    def wrapper(*args):
        func(*args) 

    return wrapper


@decorator
def display1(args):
    #print "hello one with args {0}!\n".format(args)
    for i in args:
        print i


@decorator
def display2(args):
    print "hello two!\n"

if __name__ == "__main__":
    #x1 = decorator(display1) 
    #x2 = decorator(display2) 
    #x1()
    #x2()

    x = [10,100,1000]
    display1(x)
    display2(100)

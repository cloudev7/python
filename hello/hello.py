#!/usr/local/bin/python

import sys

def greet(name="Anonymous"):
    print("Hello %s!\n" %(name))

greet()
greet("Python")

name = raw_input("Enter your name: ")
greet(name) if name else greet()

sys.exit(0)

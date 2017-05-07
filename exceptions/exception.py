#!/usr/local/bin/python


class NegativeAgeException(RuntimeError):
    def __init__(self, errMsg):
       RuntimeError.__init__(self, errMsg)

def enterage(age):
    if age <= 0:
        raise NegativeAgeException("Only positive integers are allowed")
 
    if age % 2 == 0:
        print("age is even")
    else:
        print("age is odd")
 
try:
    num = int(input("Enter your age: "))
    enterage(num)
except NegativeAgeException as e:
    print e
except:
    print("something is wrong")


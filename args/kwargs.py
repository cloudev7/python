#!/usr/local/bin/python 


def test(**kwargs):
    for key in kwargs:
        print "%s: %s" %(key, kwargs[key])


if __name__ == "__main__":
    test(a="Apple",b="Boy")

    data = {"c":"Celcius","f":"fahrenheit"}
    test(**data)

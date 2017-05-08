#!/usr/local/bin/perl

def fahrenheit(T):
    return ( (float(9)/5) * T + 32 )

def celcius(T):
    return (float(5)/9) * (T - 32)


temp = (36.5, 37, 37.5, 39)
F =  map(fahrenheit, temp)

print("Printing fahrenheit")
fah = []
for i in F:
    fah.append(i)
    print(i)

print("Printing celcius")
C = map(celcius, fah)
for j in C:
    print(j)

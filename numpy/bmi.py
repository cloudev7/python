#!/usr/local/bin/python

import numpy as np

# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
bmi = []

for i in range(len(height)):
    bmi.append(weight[i] / height[i] **2)


print "\nBMI all "
for i in bmi:
    print i

print "\nBMI >25 "
for i in bmi:
    print True if i > 25 else False 

print "\nBMI >25 "
for i in bmi:
    print i if i > 25 else next 

#!/usr/local/bin/python

import numpy as np

# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]


# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

# Calculate bmi
bmi = np_weight / np_height **2

# Print the result
print "BMI all => " + str(bmi)

print "BMI >25 => " + str(bmi > 25)

print "BMI >25 => " + str(bmi[bmi >25])

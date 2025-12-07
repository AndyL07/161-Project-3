# File Name: <IMUdata.py>
# Date: <11/13/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

from math import sqrt

def magnitude(x, y, z):
    return sqrt(dotProduct([x, y, z], [x, y, z]))
    
def dotProduct(v1, v2):
    dotSum = 0
    for i in range(len(v1)):
        dotSum += v1[i] * v2[i]
        
        return dotSum
    
def average(arr):
    tot = 0
    count = 0
    for val in arr:
        tot += val
        count += 1
    return tot / count

def within(value, center, bound):
    return (center - bound) <= value <= (center + bound)
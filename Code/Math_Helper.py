# File Name: <IMUdata.py>
# Date: <11/13/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

def magnitude(x, y, z):
    return dotProduct([x, y, z], [x, y, z])
    
def dotProduct(v1, v2):
    dotSum = 0
    for i in range(len(v1)):
        dotSum += v1[i] * v2[i]
        
        return dotSum
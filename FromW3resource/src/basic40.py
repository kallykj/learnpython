"""
Write a Python function to compute the Euclidean distance between the points (x1, y1) and (x2, y2).

The expected the output is: 
1.4142135623730951
2
"""

import math
def getEuclideanDistance(x1, y1, x2, y2):
    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return d

print(getEuclideanDistance(1, 1, 2, 2))
print(getEuclideanDistance(1, 1, 3, 1))

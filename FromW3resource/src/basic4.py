"""
4. Write a Python program which accepts the radius of a circle from the user and compute the area.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""

import math
r = float(input("Please input the radius of a circle: "))
Area = (math.pi * pow(r, 2))
print(Area)

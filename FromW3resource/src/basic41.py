"""
Given a file path, write a Python program to check whether this file exists
"""

import os
a = input("enter file path:")
exists = os.path.isfile(a)
if exists == True:
    print("File exists!")
else:
    print("No such file!")
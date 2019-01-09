"""
Write a Python function to add two objects if both objects are an integer type, else return 0.

The expected output below is:
5
0
0
"""

def tryToSum(a, b):
    if type(a) == int and type(b) == int:
        return a + b
    else: 
        return 0
    
	
print(tryToSum(2, 3))
print(tryToSum("2", "3"))
print(tryToSum([2], 3))
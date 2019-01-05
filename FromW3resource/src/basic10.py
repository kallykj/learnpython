"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

Sample value of n is 5
Expected Result : 615
"""

n = int(input("please enter a number:"))
value = n + (n+10*n) + (n+10*n+100*n)
print(value)

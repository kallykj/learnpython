"""
Write a Python program to find whether a given number (accept from the user) is even or odd

input: 456
output: even

input:34349
output: odd
"""

nums = int(input("enter a number:"))
if nums % 2 == 0:
    print("even")
else:
    print("odd")
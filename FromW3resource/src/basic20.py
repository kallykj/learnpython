"""
Write a Python program to take 2 inputs:
the first input is a string (denoted as str), 
the second input is a non-negative integer (denoted as n, non-negative integer),
then output n copies of str. For example:

abc
3

output: abcabcabc
"""

str = input("please enter a string:")
n = int(input("please enter non-negative integer:"))
print(str * n)
"""
Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

Please enter multiple integers : 3,5,7,23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""

int = input("Please enter multiple integers:")
l = int.split(",")
t =tuple(l)
print("List :", l)
print("Tuple : ", t)

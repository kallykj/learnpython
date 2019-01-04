"""
Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.py
Output : py

Sample filename : D:\src4Fun\learnpython\FromW3resource\src\readme.md
Output : md

"""

f = input("Please enter filename : ")
fs = f.split(".")
print(fs[-1])

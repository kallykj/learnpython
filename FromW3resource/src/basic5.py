"""
Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. For example:

Print enter a name:
James Wu
Output reverse name:
Wu James
"""

name = input("Print enter a name:")
words = name.split()
print(words[1], words[0])

"""
Write a Python program to calculate number of days between two dates. Note: try to import datetime module

Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""

from datetime import date
d1 = date(2014, 7, 2)
d2 = date(2014, 7, 11)
nums = d2 - d1
print(nums.days)
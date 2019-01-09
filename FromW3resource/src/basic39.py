"""
Write a Python function to compute the future value of a specified principal amount, rate of interest, and a number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
"""

def getFutureValue(base, interestPerc, years):
    fv = base * pow((1 + interestPerc / 100), years)
    return round(fv, 2)

print(getFutureValue(10000, 3.5, 7))
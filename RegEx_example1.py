# Test Program - Regular Expressions
# Trivial - What is the name of the module used in python for matching regular expressions?
# import module re
import re

# Compare two strings
regularEx1 = "abc"  # pattern to match
inputString1 = "abc"
# match method
testResult1 = re.match(regularEx1, inputString1)  # re.Match object
boolResult1 = True if testResult1 else False  # returns the bool for the expression
# implementations
print("testResult1a :", testResult1.__getitem__(0))  # re.Match object
print("testResult1b :", testResult1.string)  # re.Match object
print("bool1 :", bool(testResult1))
print("boolResult1 :", type(testResult1))

# Find whether a particular string exists
regularEx2 = "xyz"  # pattern to find
inputString2 = "xyz"
# findall method
testResult2 = re.findall(regularEx2, inputString2)  # list object
boolResult2 = True if testResult2 else False  # returns the bool for the expression
# implementations
print("testResult2a :", testResult2[0])  # list object
print("testResult2b :", testResult2.__getitem__(0))  # list object
print("bool2 :", bool(testResult2))
print("boolResult2: ", type(testResult2))

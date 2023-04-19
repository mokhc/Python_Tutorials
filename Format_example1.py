# Test Program
# Format output - example 1
# Trivial - What is needed to print a variable within an output string?

# To get the input
number = input('Enter a number: ')
number = float(number)

# Assignment
sqrtofnum = number ** 0.5

# output format 1
print('The square root of %0.3f is %0.3f' % (number, sqrtofnum)) # whitespace around the % operator

# output format 2
print("The square root of {0:0.3f} is {1:0.3f}".format(number, sqrtofnum))

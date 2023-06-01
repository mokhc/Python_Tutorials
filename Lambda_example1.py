# Test Program - Lambda functions
# Trivial - What is needed in python when you declare a lambda function?

# lambda functions
number1a = lambda num1: print(num1)

number2a = lambda num1, num2: print(num1 + num2)


# equivalence
def number1b(num1):
    print(num1)


def number2b(num1, num2):
    print(num1 + num2)


# lambda functions that return a value
number3a = lambda num1, num2: num1 + num2

number4a = lambda num1 : num1


# equivalence
def number3b(num1, num2):
    return num1 + num2


def number4b(num1):
    return num1


# Invoke the lambda functions
number1a(5)
number1b(5)

number2a(6, 0)
number2b(6, 0)

number3a = number3a(7, 0)
print(number3a)

number3b = number3b(7, 0)
print(number3b)

number4a = number4a(8)
print(number4a)

number4b = number4b(8)
print(number4b)
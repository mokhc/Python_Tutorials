# Test Program - Lambda functions
# Trivial - What is needed in python when you declare a lambda function?

# lambda functions
number1 = lambda num1: print(num1)

number2 = lambda num1, num2: print(num1 + num2)

# lambda functions that return a value
number3 = lambda num1, num2: num1 + num2

number4 = lambda num1 : num1


# Invoke the lambda functions
number1(5)

number2(5, 0)

number3 = number3(4, 0)
print(number3)

number4 = number4(4)
print(number4)
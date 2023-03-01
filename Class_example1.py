# Test Program
# Class with constructor - example 1
# Trivial - What is one of the uses of a constructor?

# Class 1
class Test1:

    # constructor
    def __init__(classself, input = "I am the default input!"):
        classself.name = input


# Class 2
class Test2:

    # constructor
    def __init__(classself, input = "I am the default input!"):
        classself.input = input

# Implementation 1
test1a = Test1('Hello')
print(test1a.name) # output : Hello

# Implementation 2
test1b = Test1()
print(test1b.name) # output : I am the default input!

# Implementation 3
test2a = Test2('Hello')
print(test2a.input) # output : Hello

# Implementation 4
test2b = Test2()
print(test2b.input) # output : I am the default input!
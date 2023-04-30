# Test Program - Class with constructor
# Trivial - What is one of the uses of a constructor?

# Class 1
class Test1:

    # constructor
    def __init__(classself1, input1="I am the default input1!"):
        classself1.name1 = input1


# Class 2
class Test2:

    # constructor
    def __init__(classself2, input2):
        classself2.name2 = input2


# Implementation 1a
test1a = Test1('Hello1')
print(test1a.name1)  # output : Hello

# Implementation 1b
test1b = Test1()
print(test1b.name1)  # output : I am the default input1!

# Implementation 2a
test2a = Test2('Hello2')
print(test2a.name2)  # output : Hello

# Implementation 2b
input2 = "I am the default input2!"
test2b = Test2(input2)
print(test2b.name2)  # output : I am the default input2!

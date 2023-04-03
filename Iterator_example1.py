# Test Program - Iterator
# Trivial - What is needed to create an iterable object in python?

# Design 1
# create a list
my_list1 = ["H", "e", "l", "l", "o"]

# create an iterator from the list
iterator1 = iter(my_list1)

# print
while iterator1:
    try:
        print(next(iterator1))
    except StopIteration:
        break


# Design 2
# create a list
my_list2 = ["H", "e", "l", "l", "o"]
lenmy_list2 = len(my_list2)

# create an iterator from the list
iterator2 = iter(my_list2)

# print
for num in range(0, lenmy_list2):
    print(iterator2.__next__())


# Design 3
# Create a list
my_list3 = ["H", "e", "l", "l", "o"]
lenmy_list3 = len(my_list3)

# create an iterator from the list
iterator3 = my_list3.__iter__()

# print
for num in range(0, lenmy_list3):
    print(iterator3.__next__())
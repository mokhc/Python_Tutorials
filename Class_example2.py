# Test Program - Use the returned values from multiple functions for manipulation
# Trivial - How do you get an instance of a class?

# class
class Building:
    # attribute
    height = 10


# class
class Room(Building):
    # attributes
    object1 = Building
    length = 0
    breadth = 0
    area = 0

    # function
    def get_length(self):
        self.length = 4
        return self.length

    # function
    def get_breadth(self):
        self.breadth = 2
        return self.breadth

    # function
    def area(self):
        self.total = self.length * self.breadth
        return self.total


# implementations
# initialization
study_room = Room()

# call the functions
study_room.get_length();
study_room.get_breadth();

# print the result of the function
print(study_room.area())

# print the default length
print(Room.length)

# print the default height
print(Room.height)

# print the default height
print(Room.object1.height)
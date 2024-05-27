class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    
    def add(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("The argument must be an instance of Point")


# Example usage for init:
point1 = Point()         # x and y default to 0
point2 = Point(3, 4)     # x is set to 3, y is set to 4

print(point1.x, point1.y)  # Output: 0 0
print(point2.x, point2.y)  # Output: 3 4

# Example usage for str:

print(point2)  # Output: (3, 4)


# Example usage for add method:
point1 = Point(1, 2)
point2 = Point(3, 4)
result = point1.add(point2)
print(result)  # Output: (4, 6)

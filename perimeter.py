import math


class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width])


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Triangle(Polygon):
    def __init__(self, side1, side2, side3):
        super().__init__([side1, side2, side3])


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def perimeter(self):
#         return 2 * math.pi * self.radius

#     def area(self):
#         return math.pi * self.radius ** 2


# Take input from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle = Rectangle(length, width)
print(f"Rectangle Perimeter: {rectangle.perimeter()}")

side = float(input("Enter the side length of the square: "))
square = Square(side)
print(f"Square Perimeter: {square.perimeter()}")

side1 = float(input("Enter the first side length of the triangle: "))
side2 = float(input("Enter the second side length of the triangle: "))
side3 = float(input("Enter the third side length of the triangle: "))
triangle = Triangle(side1, side2, side3)
print(f"Triangle Perimeter: {triangle.perimeter()}")

# radius = float(input("Enter the radius of the circle: "))
# circle = Circle(radius)
# print(f"Circle Circumference: {circle.perimeter()}")

import math


class Circle:
    """
    This class implements the Circle API
    """
    def __init__(self, radius: float = None):
        
        validateCircleRadius(radius)

        self.radius = radius
    def area(self):
        return round(math.pi * self.radius ** 2, 2)

class Rectangle:
    """
    This class implements the Rectangle API
    """
    def __init__(self, height: float = None, width: float = None):
        self.height = height
        self.width = width

        if width is None or width <= 0:
            raise ValueError("Supplied width must be >0")
        if height is None or height <= 0:
            raise ValueError("Supplied height must be >0")
        
    def area(self):
        return round(self.height * self.width, 2)


class Cube:
    def __init__(self, edge: float = None):
        self.edge = edge

        if edge is None or edge <= 0:
            raise ValueError("Supplied edge length must be >0")

    def volume(self):
        return round(self.edge ** 3)



def validateCircleRadius(radius):
        if radius is None or radius <= 0:
            raise ValueError("Supplied radius must be >0")

        if type(radius) is not float:
            raise TypeError("Supplied radius must be of type float")
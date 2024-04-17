import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def get_coordinates(self):
        return self.x, self.y
    
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

point1 = Point(1, 2)
point2 = Point(4, 6)

x1, y1 = point1.get_coordinates()
print("Координаты точки 1:", x1, y1)

point2.set_coordinates(3, 5)

x2, y2 = point2.get_coordinates()
print("Новые координаты точки 2:", x2, y2)

distance = point1.distance_to(point2)
print("Расстояние между точками:", distance)
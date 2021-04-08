"""
Author: Electra Bree
Assignment related to Object-Oriented Programming
"""
import math

# Question 1
# Represents points on a 2D plane
class MyPoint:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    
    def __str__(self):
        return "({}, {})".format(self.__x, self.__y)
        
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def set_x(self, x):
        if x >= 0:
            self.__x = x
    
    def set_y(self, y):
        if y >= 0:
            self.__y = y
            
    def get_distance(self, other_point):
        return math.sqrt((other_point.__x - self.__x)**2 + (other_point.__y - self.__y)**2)
        
    def is_near_by(self, other_point):
        if self.get_distance(other_point) < 5:
            return True
        else:
            return False

# Question 2
# Represents a line composed of 2 points
class MyLine:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.__start_point = MyPoint(x1, y1)
        self.__end_point = MyPoint(x2, y2)
        
    def __str__(self):
        return "{} to {}".format(self.__start_point, self.__end_point)
        
    def set_end_point(self, x2, y2):
        if x2 >= 0 and y2 >= 0:
            self.__end_point = MyPoint(x2, y2)
        elif x2 >= 0:
            self.__end_point = MyPoint(x2, 0)
        elif y2 >= 0:
            self.__end_point = MyPoint(0, y2)
        
    def get_end_point(self):
        return self.__end_point
        
    def set_start_point(self, x1, y1):
        if x1 >= 0 and y1 >= 0:
            self.__start_point = MyPoint(x1, y1)
        elif x1 >= 0:
            self.__start_point = MyPoint(x1, 0)
        elif y1 >= 0:
            self.__start_point = MyPoint(0, y1)
    
    def get_start_point(self):
        return self.__start_point
        
    def get_length(self):
        return self.__start_point.get_distance(self.__end_point)

# Question 3
# Represents a circle
class MyCircle:
    def __init__(self, x=0, y=0, radius=1):
        self.__x = x
        self.__y = y
        self.__centre_point = MyPoint(x, y)
        self.__radius = radius
        
    def __str__(self):
        return "Circle at {}, radius = {}".format(self.__centre_point, self.__radius)
    
    def set_radius(self, radius):
        if radius >= 0:
            self.__radius = radius
    
    def get_radius(self):
        return self.__radius
        
    def set_centre_point(self, x, y):
        if x >= 0 and y >= 0:
            self.__centre_point = MyPoint(x, y)
        elif x >= 0:
            self.__centre_point = MyPoint(x, self.__y)
        elif y >= 0:
            self.__centre_point = MyPoint(self.__x, y)
            
    def get_centre_point(self):
        return self.__centre_point
    
    def get_distance(self, another_circle):
        return self.__centre_point.get_distance(another_circle.__centre_point)

# Question 4
# Represents a line with multiple segments
class MyMultiLine:
    def __init__(self, MyPoint):
        self.__points = MyPoint
    
    def __str__(self):
        string = ""
        for point in self.__points:
            string = string + str(point)
        return string
        
    def get_length(self):
        total = 0
        for index in range(len(self.__points) - 1, -1, -1):
            if index > 0:
                total += self.__points[index - 1].get_distance(self.__points[index])
        return total

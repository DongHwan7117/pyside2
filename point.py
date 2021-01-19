from __future__ import annotations
import math

class Point2D() :
    def __init__(self,x_coordinate, y_coordinate):
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate

    def get_x_coordinate(self):
        return self.__x_coordinate

    def get_y_coordinate(self):
        return self.__y_coordinate

    def set_x_coordinate(self, x_coordinate):
        self.__x_coordinate=x_coordinate

    def set_y_coordinate(self, y_coordinate):
        self.__y_coordinate=y_coordinate
   #naming
    def distance_to_another_point(self, point : Point2D):
        distance= math.sqrt(( point.get_x_coordinate() - self.get_x_coordinate() )**2+( point.get_y_coordinate() - self.get_y_coordinate() )**2)
        return distance

    def magnitude(self):
        magnitude=math.sqrt(self.get_x_coordinate()**2+self.get_y_coordinate()**2)
        return magnitude

    def unit_vector(self):
        x_direction = self.get_x_coordinate()/self.magnitude()
        y_direction = self.get_y_coordinate()/self.magnitude()
        temp_point=Point2D(0,0)
        temp_point.set_x_coordinate(x_direction)
        temp_point.set_y_coordinate(y_direction)
        return temp_point
    
    def inner_product(self, point: Point2D):
        inner_product=self.get_x_coordinate()*point.get_x_coordinate()+self.get_y_coordinate()*point.get_y_coordinate()
        return inner_product
    
    def cross_product(self, point: Point2D):
        cross_product=self.get_x_coordinate()*point.get_y_coordinate()-self.get_y_coordinate()*point.get_x_coordinate()
        return cross_product 

    def print_name(self):
        print("Point2D")

from __future__ import annotations
from random import *
import math

class Circle2D():
    def __init__(self, center:Point2D, radius):
        self.__center=center
        self.__radius= radius

    def get_center(self):
        return self.__center
    def get_radius(self):
        return self.__radius
    def set_center(self, center:Point2D):
        self.__center=center
    def set_radius(self, radius):
        self.__radius=radius

    
    def area(self):
        return ((math.pi)*self.get_radius()*self.get_radius())

    def perimeter(self):
        return (2*(math.pi)*self.get_radius())
   
    def is_contain_circle(self, circle: Circle2D):
        if((self.get_center().distance_between_points(circle.get_center())+circle.get_radius())<self.get_radius()):
            return True
        else:
            return False

    #원주와 점 사이의 거리로 정의
    def distance_from_boundary_to_point(self,point):
        tmp_distance= self.get_center().distance_between_points(point)-self.get_radius()
        if tmp_distance>0:
            return tmp_distance
        else:
            return(-tmp_distance)
    #접할때랑 교점일떄랑 포함될때 거리가 0이 되고 그 외의 경우에는 원주와 원주 사이의 거리
    def distance_from_boundary_to_circle(self,circle):
        if(self.get_center().distance_to_another_point(circle.get_center())<(self.get_radius()+circle.get_radius())):
            return 0
        else:
            return(self.get_center().distance_to_another_point(circle.get_center())-(self.get_radius()+circle.get_radius()))
    def print_name(self):
        print("Circle2D")
from random import *
from point import*

class Line2D:
    def __init__(self, start_point: Point2D, end_point:Point2D):
        self.__start_point=start_point
        self.__end_point=end_point
    def get_start_point(self):
        return self.__start_point

    def get_end_point(self):
        return self.__end_point

    
    def set_start_point(self, point:Point2D):
        self.__start_point=point

    def set_end_point(self, point:Point2D):
        self.__end_point=point

    def length(self):
       return self.get_start_point().distance_to_another_point(self.get_end_point())
    def print_name(self):
        print("Line2D")

    def size_adjustment(self,ratio):
        a=self.get_start_point()
        b=self.get_end_point()
        x_direction= a.get_x_coordinate()-b.get_x_coordinate()
        y_direction= a.get_y_coordinate()-b.get_y_coordinate()

        self.set_end_point(Point2D(b.get_x_coordinate()+x_direction*ratio,b.get_y_coordinate()+y_direction*ratio))


    def length_fix(self, length):
        angle=uniform(0,1000)
        
        self.set_end_point(Point2D(self.get_start_point().get_x_coordinate()+length*math.cos(angle),self.get_start_point().get_y_coordinate()+length*math.sin(angle) ))


    def Is_Intersect(self, line):
        x11=self.get_start_point().get_x_coordinate()
        x12=self.get_end_point().get_x_coordinate()
        x21=line.get_start_point().get_x_coordinate()
        x22=line.get_end_point().get_x_coordinate()
        y11=self.get_start_point().get_y_coordinate()
        y12=self.get_end_point().get_y_coordinate()
        y21=line.get_start_point().get_y_coordinate()
        y22=line.get_end_point().get_y_coordinate()
        
        f1= (x12-x11)*(y21-y11) - (y12-y11)*(x21-x11)
        f2= (x12-x11)*(y22-y11) - (y12-y11)*(x22-x11)
        f3= (x21-x22)*(y12-y22) - (y21-y22)*(x12-x22)
        f4= (x21-x22)*(y11-y22) - (y21-y22)*(x11-x22)


        if (f1*f2 > 0 ) & (f3*f4>0 ):
            return False
        else:
            return True


    def Is_Intersect_Circle(self, circle):
        a=self.get_start_point().get_y_coordinate()-self.get_end_point().get_y_coordinate()
        b=self.get_end_point().get_x_coordinate()-self.get_start_point().get_x_coordinate()
        c=(self.get_start_point().get_y_coordinate()-self.get_end_point().get_y_coordinate())*(-1)*(self.get_start_point().get_x_coordinate())+(self.get_start_point().get_y_coordinate())*(self.get_start_point().get_x_coordinate()-self.get_end_point().get_x_coordinate())
        d=circle.get_radius()
        l=abs(a*circle.get_center().get_x_coordinate()+b*circle.get_center().get_y_coordinate()+c)/(math.sqrt(a*a+b*b))
        if l>d:
            return False
        elif ((not self.is_divided_by_center_normal_line(circle))&(circle.get_center().distance_to_another_point(self.get_start_point())>d)&(circle.get_center().distance_to_another_point(self.get_end_point())>d)):
            return False
        else:
            return True

    

    def is_divided_by_center_normal_line(self, circle):
        a=self.get_start_point().get_x_coordinate()-self.get_end_point().get_x_coordinate()
        b=self.get_start_point().get_y_coordinate()-self.get_end_point().get_y_coordinate()
        c=-(circle.get_center().get_x_coordinate()*(self.get_start_point().get_x_coordinate()-self.get_end_point().get_x_coordinate())+circle.get_center().get_y_coordinate()*(self.get_start_point().get_y_coordinate()-self.get_end_point().get_y_coordinate()))


        if (a*self.get_start_point().get_x_coordinate()+b*self.get_start_point().get_y_coordinate()+c)*(a*self.get_end_point().get_x_coordinate()+b*self.get_end_point().get_y_coordinate()+c)<0:
            return True




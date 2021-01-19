from point import*
from line import*
from circle import*


class Calculator:
    
    def __init__(self):
        self.Debugging_list=[]
        self.Debugging_itr=0
        self.full_read=[]
        self.full_read_itr=0
        self.r=1
        self.w=1
        self.circle_number=40
        self.line_number=120

   
    def circle_first_simulation_a(self):
      
        
        shapelist=[]
        circlelist=[]
        
        
        while len(circlelist)<self.circle_number:
            circlelist.append(Circle2D(Point2D(uniform(200,1500), uniform(200,800)),uniform(30,50)))
            
            for i in range(len(circlelist)-1):
                if (circlelist[len(circlelist)-1].distance_from_boundary_to_circle(circlelist[i])==0) :
                    circlelist.pop()
                    break
                



        while len(shapelist)<self.line_number:
            shapelist.append(Line2D(Point2D(uniform(100,1800), uniform(100,900)),Point2D(uniform(100,1800), uniform(100,900))))
            shapelist[len(shapelist)-1].length_fix(uniform(10,500))


            for i in range(len(shapelist)-1):
                if shapelist[len(shapelist)-1].Is_Intersect(shapelist[i]) :
                    shapelist.pop()
                    break

            
            for i in range(len(circlelist)):
                if shapelist[len(shapelist)-1].Is_Intersect_Circle(circlelist[i]):
                    shapelist.pop()
                    break

        

        circlelist.extend(shapelist)
        shapelist=circlelist


        self.Debugging_list=shapelist
        self.Debugging_itr=0
       


    def circle_line_randomly_simulation_m(self):
           
            
            shapelist=[]
            circle_list_number=0
            line_list_number=0
            shape_random=0
            itr=1

            circle_max=0
            line_max=0

            if((self.circle_number/self.line_number)==0):
                circle_max=1
                line_max=self.line_number/self.circle_number
            else:
                circle_max=self.circle_number/self.line_number
                line_max=1

            module=circle_max+line_max

            while len(shapelist)<self.circle_number+self.line_number:
              
                
                if(((itr%module<circle_max)&(circle_list_number<self.circle_number)) or (line_list_number==self.line_number)) : 
                        shapelist.append(Circle2D(Point2D(uniform(200,1500), uniform(200,800)),uniform(30,50)))
                        circle_list_number=circle_list_number+1
                        
                        a=len(shapelist)


                        for i in range(len(shapelist)-1):
                                
                                if(type(shapelist[i]) is Circle2D) :
                                        if (shapelist[len(shapelist)-1].distance_from_boundary_to_circle(shapelist[i])==0) :
                                                shapelist.pop()
                                                circle_list_number=circle_list_number-1
                                                break
                                        

                                elif(type(shapelist[i]) is Line2D) :
                                        if shapelist[i].Is_Intersect_Circle(shapelist[len(shapelist)-1]) :
                                                shapelist.pop()
                                                circle_list_number=circle_list_number-1
                                                break
                                
                        b=len(shapelist)
                        if (a==b):
                            itr=itr+1   

                elif (((itr%module>=circle_max)&(line_list_number<self.line_number)) or (circle_list_number==self.circle_number)):
                        shapelist.append(Line2D(Point2D(uniform(100,1800), uniform(100,900)),Point2D(uniform(100,1800), uniform(100,900))))
                        shapelist[len(shapelist)-1].length_fix(uniform(10,500))
                        line_list_number=line_list_number+1
                        a=len(shapelist)


                        for i in range(len(shapelist)-1):
                                
                                if(type(shapelist[i]) == Circle2D) :
                                        if (shapelist[len(shapelist)-1].Is_Intersect_Circle(shapelist[i])) :
                                                shapelist.pop()
                                                line_list_number=line_list_number-1
                                                break
                            
                            
                                elif(type(shapelist[i]) is Line2D) :
                                        if shapelist[len(shapelist)-1].Is_Intersect(shapelist[i]) :
                                                shapelist.pop()
                                                line_list_number=line_list_number-1
                                                break
                                
                        b=len(shapelist)
                        if (a==b):
                                itr=itr+1   
                

            self.Debugging_list=shapelist
            self.Debugging_itr=0
            
            
            f = open("C:\\Users\\com\\Desktop\\m_angle.txt", 'a')

            line=[]
            for i in range(len(self.Debugging_list)):
                if(type(self.Debugging_list[i]) == Line2D) :
                    f.write(str(math.atan((self.Debugging_list[i].get_start_point().get_y_coordinate()-self.Debugging_list[i].get_end_point().get_y_coordinate())/(self.Debugging_list[i].get_start_point().get_x_coordinate()-self.Debugging_list[i].get_end_point().get_x_coordinate())))+" ")
                    f.write(str(self.Debugging_list[i].length())+"\n")
                    line.append(math.atan((self.Debugging_list[i].get_start_point().get_y_coordinate()-self.Debugging_list[i].get_end_point().get_y_coordinate())/(self.Debugging_list[i].get_start_point().get_x_coordinate()-self.Debugging_list[i].get_end_point().get_x_coordinate())))
                    line.append(self.Debugging_list[i].length())

            f.close()
        
    
            angle=[]
            length=[]



            for i in range(len(line)):
                if (i%2==1) :
                    angle.append(line.pop())
                else : 
                    length.append(line.pop())

            sum=0
            for i in range(len(length)) :
                sum=sum + length[i]

            weight=[]

            for i in range(len(length)) :
                weight.append(length[i]/sum)
            


            temp=0
            for i in range(len(weight)):
                temp=temp+weight[i]*angle[i]


            weighted_mean=temp
            
            mean=0
            temp=0

            for i in range(len(weight)):
                temp=temp+angle[i]

            mean=temp/len(weight)




            temp=0
            for i in range(len(weight)):
                temp=temp+weight[i]*(angle[i]-weighted_mean)*(angle[i]-weighted_mean)

            weighted_variance=temp

            temp=0
            variance=0
            for i in range(len(weight)):
                temp=temp+(angle[i]-mean)*(angle[i]-mean)

            variance=temp/len(weight)




            print(weighted_mean)
            print(weighted_variance)

            f = open("C:\\Users\\com\\Desktop\\m_m.txt", 'a')
            f.write(str(weighted_mean)+"\n")
            f.close()


            f= open("C:\\Users\\com\\Desktop\\m_v.txt", 'a')
            f.write(str(weighted_variance)+"\n")
            f.close()

            f = open("C:\\Users\\com\\Desktop\\n_m_m.txt", 'a')
            f.write(str(mean)+"\n")
            f.close()


            f= open("C:\\Users\\com\\Desktop\\n_m_v.txt", 'a')
            f.write(str(variance)+"\n")
            f.close()


    def circle_line_randomly_simulation_s(self):
            shapelist=[]
            circle_list_number=0
            line_list_number=0
            shape_random=0
            itr=1

            circle_max=0
            line_max=0

            
            circle_max=1
            line_max=1

            module=circle_max+line_max

            while len(shapelist)<self.circle_number+self.line_number:
                
                
                if(((itr%module<circle_max)&(circle_list_number<self.circle_number)) or (line_list_number==self.line_number)) : 
                        shapelist.append(Circle2D(Point2D(uniform(200,1500), uniform(200,800)),uniform(30,50)))
                        circle_list_number=circle_list_number+1
                        
                        a=len(shapelist)


                        for i in range(len(shapelist)-1):
                                
                                if(type(shapelist[i]) is Circle2D) :
                                        if (shapelist[len(shapelist)-1].distance_from_boundary_to_circle(shapelist[i])==0) :
                                                shapelist.pop()
                                                circle_list_number=circle_list_number-1
                                                break
                                        
                                                
                                elif(type(shapelist[i]) is Line2D) :
                                        if shapelist[i].Is_Intersect_Circle(shapelist[len(shapelist)-1]) :
                                                shapelist.pop()
                                                circle_list_number=circle_list_number-1
                                                break
                                
                        b=len(shapelist)
                        if (a==b):
                            itr=itr+1   

                elif (((itr%module>=circle_max)&(line_list_number<self.line_number)) or (circle_list_number==self.circle_number)):
                        shapelist.append(Line2D(Point2D(uniform(100,1800), uniform(100,900)),Point2D(uniform(100,1800), uniform(100,900))))
                        shapelist[len(shapelist)-1].length_fix(uniform(10,500))
                        line_list_number=line_list_number+1
                        a=len(shapelist)


                        for i in range(len(shapelist)-1):
                                
                                if(type(shapelist[i]) == Circle2D) :
                                        if (shapelist[len(shapelist)-1].Is_Intersect_Circle(shapelist[i])) :
                                                shapelist.pop()
                                                line_list_number=line_list_number-1
                                                break
                            
                            
                                elif(type(shapelist[i]) is Line2D) :
                                        if shapelist[len(shapelist)-1].Is_Intersect(shapelist[i]) :
                                                shapelist.pop()
                                                line_list_number=line_list_number-1
                                                break
                                
                        b=len(shapelist)
                        if (a==b):
                                itr=itr+1   
                
            

            self.Debugging_list=shapelist
            self.Debugging_itr=0



            f = open("C:\\Users\\com\\Desktop\\s_angle.txt", 'a')

            line=[]
            for i in range(len(self.Debugging_list)):
                if(type(self.Debugging_list[i]) == Line2D) :
                    f.write(str(math.atan((self.Debugging_list[i].get_start_point().get_y_coordinate()-self.Debugging_list[i].get_end_point().get_y_coordinate())/(self.Debugging_list[i].get_start_point().get_x_coordinate()-self.Debugging_list[i].get_end_point().get_x_coordinate())))+" ")
                    f.write(str(self.Debugging_list[i].length())+"\n")
                    line.append(math.atan((self.Debugging_list[i].get_start_point().get_y_coordinate()-self.Debugging_list[i].get_end_point().get_y_coordinate())/(self.Debugging_list[i].get_start_point().get_x_coordinate()-self.Debugging_list[i].get_end_point().get_x_coordinate())))
                    line.append(self.Debugging_list[i].length())

            f.close()
       
    
            angle=[]
            length=[]

            for i in range(len(line)):
                if (i%2==1) :
                    angle.append(line.pop())
                else : 
                    length.append(line.pop())

            sum=0
            for i in range(len(length)) :
                sum=sum + length[i]

            weight=[]

            for i in range(len(length)) :
                weight.append(length[i]/sum)
            


            temp=0
            for i in range(len(weight)):
                temp=temp+weight[i]*angle[i]


            weighted_mean=temp
            
            mean=0
            temp=0

            for i in range(len(weight)):
                temp=temp+angle[i]

            mean=temp/len(weight)




            temp=0
            for i in range(len(weight)):
                temp=temp+weight[i]*(angle[i]-weighted_mean)*(angle[i]-weighted_mean)

            weighted_variance=temp

            temp=0
            variance=0
            for i in range(len(weight)):
                temp=temp+(angle[i]-mean)*(angle[i]-mean)

            variance=temp/len(weight)




            print(weighted_mean)
            print(weighted_variance)

            f = open("C:\\Users\\com\\Desktop\\s_m.txt", 'a')
            f.write(str(weighted_mean)+"\n")
            f.close()


            f= open("C:\\Users\\com\\Desktop\\s_v.txt", 'a')
            f.write(str(weighted_variance)+"\n")
            f.close()

            f = open("C:\\Users\\com\\Desktop\\n_s_m.txt", 'a')
            f.write(str(mean)+"\n")
            f.close()


            f= open("C:\\Users\\com\\Desktop\\n_s_v.txt", 'a')
            f.write(str(variance)+"\n")
            f.close()    
    
    # def increment_sequencial_record_d(self):
        
    #     if self.r==1:
    #         self.image.fill(Qt.white)
    #         self.update()
    #         self.r=0
        
    #     f = open("C:\\Users\\com\\Desktop\\Debugging.txt", 'a')
    #     painter = QPainter(self.image)
    #     painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
        
    #     if(type(self.Debugging_list[self.Debugging_itr]) is Circle2D) :
    #             painter.drawEllipse(self.Debugging_list[self.Debugging_itr].get_center().get_x_coordinate()-self.Debugging_list[self.Debugging_itr].get_radius(), self.Debugging_list[self.Debugging_itr].get_center().get_y_coordinate()-self.Debugging_list[self.Debugging_itr].get_radius(),self.Debugging_list[self.Debugging_itr].get_radius()*2.0,self.Debugging_list[self.Debugging_itr].get_radius()*2.0 )
    #             self.update()

    #     elif(type(self.Debugging_list[self.Debugging_itr]) is Line2D) :
    #             painter.drawLine(QPoint(self.Debugging_list[self.Debugging_itr].get_start_point().get_x_coordinate(),self.Debugging_list[self.Debugging_itr].get_start_point().get_y_coordinate()),QPoint(self.Debugging_list[self.Debugging_itr].get_end_point().get_x_coordinate(),self.Debugging_list[self.Debugging_itr].get_end_point().get_y_coordinate()))
    #             self.update()
            
    #     elif(type(self.Debugging_list[self.Debugging_itr]) is Point2D) :
    #             self.update()


        
    #     if self.Debugging_itr< len(self.Debugging_list):
            
            
            
    #         if(type(self.Debugging_list[self.Debugging_itr]) == Line2D) :
                
    #             f.write(str(math.atan((self.Debugging_list[self.Debugging_itr].get_start_point().get_y_coordinate()-self.Debugging_list[self.Debugging_itr].get_end_point().get_y_coordinate())/(self.Debugging_list[self.Debugging_itr].get_start_point().get_x_coordinate()-self.Debugging_list[self.Debugging_itr].get_end_point().get_x_coordinate())))+"\n")
    #             f.write(str(self.Debugging_list[self.Debugging_itr].length())+"\n")
           
    #         if self.Debugging_itr!=len(self.Debugging_list)-1:
    #             self.Debugging_itr= self.Debugging_itr +1

    #     f.close()
from calculator import*
import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

class MyApp(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.image = QImage(QSize(1800, 1000), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing = False
        self.brush_size = 0
        self.brush_color = Qt.black
        
        self.calculator=Calculator()
        self.initUI()
        

    def initUI(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('File')

        a_action = QAction('A', self)
        a_action.setShortcut('Ctrl+A')
        a_action.triggered.connect(self.circle_first_simulation_a)
        
    
        s_action=QAction('S', self)
        s_action.setShortcut('Ctrl+S')
        s_action.triggered.connect(self.circle_line_randomly_simulation_s)



        m_action=QAction('M', self)
        m_action.setShortcut('Ctrl+M')
        m_action.triggered.connect(self.circle_line_randomly_simulation_m)


        # d_action = QAction('D', self)
        # d_action.setShortcut('Ctrl+D')
        # d_action.triggered.connect(self.increment_sequencial_record_d)

       
        filemenu.addAction(a_action)
        filemenu.addAction(s_action)
        filemenu.addAction(m_action)
        # filemenu.addAction(d_action)

        self.setWindowTitle('Simple Painter')
        self.setGeometry(900, 900, 1800, 1000)
        self.show()
    
    
    def paintEvent(self, e):
        canvas = QPainter(self)
        canvas.drawImage(self.rect(), self.image, self.image.rect())




   
    def circle_first_simulation_a(self):
          

        self.image.fill(Qt.white)
        self.update()
        
        self.calculator.circle_first_simulation_a()
        shapelist=self.calculator.Debugging_list  
        
        painter = QPainter(self.image)
        painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))

        for i in range(len(shapelist)):
            if(type(shapelist[i]) is Circle2D) :
                self.brush_color = Qt.red
                self.brush_size = 0
                painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
                painter.drawEllipse(shapelist[i].get_center().get_x_coordinate()-shapelist[i].get_radius(), shapelist[i].get_center().get_y_coordinate()-shapelist[i].get_radius(), shapelist[i].get_radius()*2.0, shapelist[i].get_radius()*2.0 )
                self.update()
                self.brush_color = Qt.black
                self.brush_size = 0
                painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))

            elif(type(shapelist[i]) is Line2D) :
                painter.drawLine(QPoint(shapelist[i].get_start_point().get_x_coordinate(),shapelist[i].get_start_point().get_y_coordinate()),QPoint(shapelist[i].get_end_point().get_x_coordinate(),shapelist[i].get_end_point().get_y_coordinate()))
                self.update()
            
            elif(type(shapelist[i]) == Point2D) :
                self.update()
     

    def circle_line_randomly_simulation_m(self):
            self.image.fill(Qt.white)
            self.update()
            
            
            self.calculator.circle_line_randomly_simulation_m()
            shapelist=self.calculator.Debugging_list    

            
            
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
            
            for i in range(len(shapelist)):
                if(type(shapelist[i]) is Circle2D) :
                    self.brush_color = Qt.red
                    self.brush_size = 0
                    painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
                    painter.drawEllipse(shapelist[i].get_center().get_x_coordinate()-shapelist[i].get_radius(), shapelist[i].get_center().get_y_coordinate()-shapelist[i].get_radius(), shapelist[i].get_radius()*2.0, shapelist[i].get_radius()*2.0 )
                    self.update()
                    self.brush_color = Qt.black
                    self.brush_size = 0
                    painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))

                elif(type(shapelist[i]) is Line2D) :
                    painter.drawLine(QPoint(shapelist[i].get_start_point().get_x_coordinate(),shapelist[i].get_start_point().get_y_coordinate()),QPoint(shapelist[i].get_end_point().get_x_coordinate(),shapelist[i].get_end_point().get_y_coordinate()))
                    self.update()
                
                elif(type(shapelist[i]) is Point2D) :
                    self.update()

            self.Debugging_list=shapelist
            self.Debugging_itr=0

            
            
            


    def circle_line_randomly_simulation_s(self):
            self.image.fill(Qt.white)
            self.update()
            
            

            self.calculator.circle_line_randomly_simulation_s()
            shapelist=self.calculator.Debugging_list  
        
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
            
            for i in range(len(shapelist)):
                if(type(shapelist[i]) is Circle2D) :
                    self.brush_color = Qt.red
                    self.brush_size = 0
                    painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
                    painter.drawEllipse(shapelist[i].get_center().get_x_coordinate()-shapelist[i].get_radius(), shapelist[i].get_center().get_y_coordinate()-shapelist[i].get_radius(), shapelist[i].get_radius()*2.0, shapelist[i].get_radius()*2.0 )
                    self.update()
                    self.brush_color = Qt.black
                    self.brush_size = 0
                    painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))

                elif(type(shapelist[i]) is Line2D) :
                    painter.drawLine(QPoint(shapelist[i].get_start_point().get_x_coordinate(),shapelist[i].get_start_point().get_y_coordinate()),QPoint(shapelist[i].get_end_point().get_x_coordinate(),shapelist[i].get_end_point().get_y_coordinate()))
                    self.update()
                
                elif(type(shapelist[i]) is Point2D) :
                    self.update() 
    
    
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
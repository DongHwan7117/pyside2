from PySide2.QtWidgets import (QApplication, QWidget, QPushButton, 
                               QCheckBox, QRadioButton, QVBoxLayout, QGroupBox)
import sys

class MyForm(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setWindowTitle('Button Demo')

        self.button = QPushButton('&Ok',self)
        self.button.clicked.connect(self.okButtonClicked)

        self.checkBox = QCheckBox('&Case sensitivity',self)
        self.checkBox.toggled.connect(self.onCaseSensitivity)

        box = QGroupBox("Sex",self)

        self.button1 = QRadioButton("Male",box)
        self.button2 = QRadioButton("Female",box)
        self.button1.setChecked(True)

        groupBoxLayout = QVBoxLayout(box)
        groupBoxLayout.addWidget(self.button1)
        groupBoxLayout.addWidget(self.button2)
        self.button1.toggled.connect(self.onMale)

        mainlayout = QVBoxLayout()
        mainlayout.addWidget(self.button)
        mainlayout.addWidget(self.checkBox)
        mainlayout.addWidget(box)

        self.setLayout(mainlayout)

    def okButtonClicked(self):
        print('okButtonClicked')        

    def onCaseSensitivity(self,toggle):
        print('okCaseSensitity',toggle)
        print(self.checkBox.isChecked())

    def onMale(self,toggle):
        print('onMale',toggle)        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyForm()    
    form.show()
    app.exec_()
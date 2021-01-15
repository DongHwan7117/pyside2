from __future__ import annotations
from random import *
import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import math
import time
from point import*
from line import*
from circle import*
from gui import*

    
if __name__ == "__main__":
    
    
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

    

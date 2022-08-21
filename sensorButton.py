from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *  
from PyQt5 import uic

from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt

import ColorPallete as colors

class SensorButton(QtWidgets.QWidget):

    #setup stuff not sure what this means
    def __init__ (self, sn, btnColor ,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fill = btnColor
        self.state = True
        self.btnColor = btnColor
        
        #load the sensor button ui
        uic.loadUi("SensorButton.ui", self)
        
        #define the widgets
        self.findChild(QLabel, "sensorName").setText(sn)
        self.sensorValue = self.findChild(QLabel, "sensorData")
        
        #set text values
        
            
        self.show()

        # On click event
        self.mouseReleaseEvent=self.clicked
        
       

    # on click method    
    def clicked(self, event):
        if self.state == False:
            self.fill = self.btnColor
            self.state = True
        else:
            self.fill = colors.g1
            self.state = False
        
        self.update()
        
    def update_Data(self, val):
        self.sensorValue.setText(str(val))
                  
    # Draw rounded rect 
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.NoPen))
        painter.setBrush(self.fill)
        
        #Anti Aliasing
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
        
        w = 36
        x = 100 - (w/2)
        
        painter.drawRoundedRect(x, 95, w, 6, 3.0, 3.0)
    
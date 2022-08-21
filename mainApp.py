from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt

from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

from PyQt5 import uic

import sys
import random

import sensorButton as sb
import ColorPallete as colors
import sensorData as sd
import Settings 

#create a data array to hold sensor values

buttonObjects = []
buttonNames = ["Battery", "Coolant", "Trans", "Exhaust"]
updatePeriod = 33



S1 = [sd.SensorData("test", 0), 
      sd.SensorData("test", 1),
      sd.SensorData("test", 2),
      sd.SensorData("test", 3)]
    
class NavBar(QtWidgets.QWidget):
    #setup stuff not sure what this means
    def __init__ (self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        layout = QtWidgets.QHBoxLayout()
        
        self.setFixedHeight(60)
        
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet('background-color: rgba(' + ','.join(tuple(str(item) for item in colors.g2.getRgb()))  + ')')
        
        self.setLayout(layout)
        self.show()
        
class StatWindow(QWidget):
    #setup stuff not sure what this means
    def __init__ (self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.height = 298
        self.fill = colors.g1
        layout = QtWidgets.QHBoxLayout()
        self.setFixedHeight(self.height)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
    
        #converts color from int tuple to string tuple then converst from a tuple to string (1, 2, 3) -> ('1', '2', '3') -> '1, 2, 3'  
        self.setStyleSheet('background-color: rgba(' + ','.join(tuple(str(item) for item in colors.g3.getRgb()))  + ')')
        self.setLayout(layout)
        self.show()
    
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.getNextDataPoint)
        self.timer.start(updatePeriod)
        
    #update method  
    def getNextDataPoint(self):
        #add a new data point for each sensor
        for ci in range (len(S1)):
            
            if Settings.PiMode:
                value1 = S1[ci].channel.value
            else:
                value1 = 0

            S1[ci].addValue(value1)
            S1[ci].setMaxMin()
            
            self.update()
    
    
    # Draw rounded rect 
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.NoPen))
        
        #Anti Aliasing
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
        
        #draw ellipses for each sensor
        for ci in range (4):
            i = 0
            #change fill color for each sensor
            painter.setBrush(colors.btnColor[S1[ci].color])
            
            #Wont draw 
            if buttonObjects[ci].state:
                for ts in S1[ci].dataArray:
                    
                    #point values
                    wh = 4
                    x = i * (800 / sd.steps) + (800 / sd.steps / 2) - wh/2
                    
                    #math to get the y value
                    ratio = 0
                    if S1[ci].range != 0:
                        ratio = (self.height  - 40) / S1[ci].range
                    
                    newVal = ts - S1[ci].minValue
                    y = self.height - newVal * ratio
                    
                    painter.drawEllipse(x, y-20, wh, wh)
                    i += 1
        
        
        
class ButtonWindow(QWidget):
    #setup stuff not sure what this means
    def __init__ (self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # define the layout
        layout = QtWidgets.QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.show()
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), colors.g2)
        self.setPalette(p)
        
        #create and add button to array
        for i in range(len(buttonNames)):
            buttonObjects.append(sb.SensorButton(buttonNames[i], colors.btnColor[i]))
            layout.addWidget(buttonObjects[i])
            
        #Updates the data every x milliseconds
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateData)
        self.timer.start(updatePeriod)
        
    def updateData(self):
        for i in range(len(buttonObjects)):
            buttonObjects[i].update_Data(round(S1[i].lastVal))
            
        
        
class UI(QtWidgets.QWidget): 
    def __init__(self, *args, **kwargs):
        super(UI, self).__init__(*args, **kwargs)
        
        #set the layout
        layout = QtWidgets.QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        
        #load the sensor button widget
        self.buttonWindow = ButtonWindow()
        self.navBar = NavBar()
        self.statWindow = StatWindow()
        layout.addWidget(self.navBar)
        layout.addWidget(self.statWindow)
        layout.addWidget(self.buttonWindow)
        
        # set the layout
        self.setLayout(layout)
        
        #set size of screen
        self.resize(800, 480)
        
#initalizwe the app
app = QtWidgets.QApplication([])
UIWindow = UI()

if Settings.PiMode:
    UIWindow.showFullScreen()
    UIWindow.setCursor(Qt.BlankCursor)
else:
    UIWindow.show()



app.exec_()



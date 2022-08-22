from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt

from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

import ColorPallete as colors
import Settings 

import GaugePage as gp

#create a data array to hold sensor values


    
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
             
class UI(QtWidgets.QWidget): 
    def __init__(self, *args, **kwargs):
        super(UI, self).__init__(*args, **kwargs)
        
        #set the layout
        layout = QtWidgets.QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        #load the sensor button widget
        self.navBar = NavBar()
        self.statWindow = gp.StatWindow()
        self.buttonWindow = gp.ButtonWindow()
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


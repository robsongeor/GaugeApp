from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt

from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

import Settings 
import Content

import Navigation as nav

#create a data array to hold sensor values   
class UI(QtWidgets.QWidget): 
    def __init__(self, *args, **kwargs):
        super(UI, self).__init__(*args, **kwargs)
        
        #set the layout
        layout = QtWidgets.QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        #Load nav Bar with gauge page
        self.navBar = nav.NavBar("Gauge")
        layout.addWidget(self.navBar)
        
        #Load Content // Get the widgets in a given page
        for w in Content.GetPageWidgets(self.navBar.page):
            layout.addWidget(w())
        
        
        # set the layout
        self.setLayout(layout)
        
        #set size of screen
        self.resize(*Settings.window_Size)
        
#initalizwe the app
app = QtWidgets.QApplication([])
UIWindow = UI()

if Settings.PiMode:
    UIWindow.showFullScreen()
    UIWindow.setCursor(Qt.BlankCursor)
else:
    UIWindow.show()



app.exec_()



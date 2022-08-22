from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

import ColorPallete as colors
import Settings

class NavBar(QtWidgets.QWidget):
    #setup stuff not sure what this means
    def __init__ (self, page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.layout = QtWidgets.QHBoxLayout()
        self.page = page
        
        self.setFixedHeight(60)
        
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet('background-color: rgba(' + ','.join(tuple(str(item) for item in colors.g2.getRgb()))  + ')')
        
        self.layout.addWidget(ColorSettingsButton())
        
        self.setLayout(self.layout)
        
        
class ColorSettingsButton(QtWidgets.QWidget):
    #setup stuff not sure what this means
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QtWidgets.QHBoxLayout()
        
        #add a label/icon
        self.text = QLabel(self)
        self.text.setFont(QFont(Settings.font_reg, Settings.font_sz_nav))
        self.text.setText("Edit")
        
        
        
     
        
        #add a on click event
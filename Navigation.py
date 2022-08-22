from PyQt5 import QtWidgets, QtCore
import ColorPallete as colors

class NavBar(QtWidgets.QWidget):
    #setup stuff not sure what this means
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        layout = QtWidgets.QHBoxLayout()
        
        self.setFixedHeight(60)
        
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet('background-color: rgba(' + ','.join(tuple(str(item) for item in colors.g2.getRgb()))  + ')')
        
        self.setLayout(layout)
        self.show()
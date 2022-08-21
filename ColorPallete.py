from PyQt5 import QtGui
import Settings as s

#Blue light correction constants
blc = 1 - s.BlueLightCorrection / 100
glc = 1 - s.BlueLightCorrection / 200

#Redshifting function
def rs(c):
    r = c[0]
    g = c[1] * glc
    b = c[2] * blc
    return (r,g,b)

#nightmode function
def nm(c):
    return (255-c[0], 255-c[1], 255-c[2])


btnColor = [QtGui.QColor(*rs(s.sensor_1_color)), 
            QtGui.QColor(*rs(s.sensor_2_color)), 
            QtGui.QColor(*rs(s.sensor_3_color)), 
            QtGui.QColor(*rs(s.sensor_4_color))]

if s.NightMode:
    g1 = QtGui.QColor(*rs(nm((182, 182, 182))))
    g2 = QtGui.QColor(*rs(nm((242, 242, 242))))
    g3 = QtGui.QColor(*rs(nm((234, 234, 234))))
else:
    g1 = QtGui.QColor(*rs((182, 182, 182)))
    g2 = QtGui.QColor(*rs((242, 242, 242)))
    g3 = QtGui.QColor(*rs((234, 234, 234)))
    
   

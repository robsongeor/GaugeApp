#Get the widgets to display on the selected page


import GaugePage as gp

#Dictionary of widgets in each page
w_kv = {
    'Gauge': [gp.StatWindow, gp.ButtonWindow],
    'GaugeFlip': [gp.ButtonWindow, gp.StatWindow]
}

def GetPageWidgets(page_name):
    widgets = []
    
    for w in w_kv[page_name]:
        widgets.append(w)
    
    return widgets
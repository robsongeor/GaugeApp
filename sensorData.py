from gpiozero import MCP3208

import Settings

#ch = [MCP3208(channel=0),
#      MCP3208(channel=1),
#      MCP3208(channel=2),
#      MCP3208(channel=3)]

ch = [0,1,2,3]

#initialization
Sensors = []

#how many data points in the array
steps = 100

#create an array that holds the array of sensor data
for x in range(0, 4):
    Sensors.append([])
    
class SensorData:
    def __init__(self, sensorName, color):
        #init
        self.sensorName = sensorName
        self.dataArray = []
        self.maxValue = 0
        self.minValue = 1000
        self.range = 0
        self.lastVal = 0
        self.color = color
        
        if Settings.PiMode:
            self.channel = MCP3208(channel=color)
        else:
            self.channel = color
        
        #fill array with 0
        for x in range(0, steps):
            self.dataArray.append(0.0)
            
        
      
    #adds a new value to end of array, and removes first element        
    def addValue(self,  val ):
        self.lastVal = val
        self.dataArray.append( val )
        self.dataArray.pop(0)
    
    #finds the lowest and highest values and sets them // needs to be called every update
    def setMaxMin(self):
        curMin = 1000

        for i in range(len(self.dataArray)):
            if self.dataArray[i] < curMin:
                curMin = self.dataArray[i]
                         
        curMax = 0

        for i in range(len(self.dataArray)):
            if self.dataArray[i] > curMax:
                curMax = self.dataArray[i]
        
        self.maxValue = curMax
        self.minValue = curMin
        self.range = self.maxValue - self.minValue
        
       
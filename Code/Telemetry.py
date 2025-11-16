# File Name: <Telemetry.py>
# Date: <11/2/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

from Timer import Timer
from Data_Collection import DataCollection
from Math_Helper import magnitude

class Telemetry():
    capText = "------------------------------\n"
    
    def __init__(self, timer=Timer(), data=DataCollection()):
        self.runTime = timer
        self.telemetryStr = self.capText
        self.add(self.runTime.currTime(), "Current Time")
        self.data = data
        self.otherData = []
    
    def add(self, value, label='', addData=False):        
        # Adding test
        if addData:
            self.otherData.append(value)
        if label != '':
            label = label + ": "
        if type(value) is str:
            self.telemetryStr += label + value + "\n"
        else:
            #self.data.addData(value, label)
            self.telemetryStr += label + f"{value:2.3f}" + "\n"
            
    def addAccel(self, x, y, z):
        accelStr = "AX = %7.2f m/s^2 \t AY = %7.2f m/s^2 \t AZ = %7.2f m/s^2" % (x, y, z)
        self.data.addData(x, "xAccel")
        self.data.addData(y, "yAccel")
        self.data.addData(z, "zAccel")
        
        accelStren = magnitude(x, y, z)
        self.data.addData(accelStren, "accelStren")
        
        self.add(accelStr)
        self.add(accelStren, "Accel Strength")
        
    def addGyro(self, x, y, z):
        gyroStr = "GX = %7.2f dps \t GY = %7.2f dps \t GZ = %7.2f dps" % (x, y, z)
        self.data.addData(x, "xGyro")
        self.data.addData(y, "yGyro")
        self.data.addData(z, "zGyro")
        
        gyroStren = magnitude(x, y, z)
        self.data.addData(gyroStren, "gyroStren")
        
        self.add(gyroStr)
        self.add(gyroStren, "Gyro Strength")
        
    def addMag(self, x, y, z):
        magStr = "MX = %7.2f uT \t MY = %7.2f uT \t MZ = %7.2f uT" % (x, y, z)
        self.data.addData(x, "xMag")
        self.data.addData(y, "yMag")
        self.data.addData(z, "zMag")
        
        magStren = magnitude(x, y, z)
        self.data.addData(magStren, "magStren")
        
        self.add(magStr)
        self.add(magStren, "Mag Strength")
        
            
    def reset(self):
        self.telemetryStr = self.capText
        time = self.runTime.currTime()
        self.add(time, "Current Time")
        self.data.addData(time, "Time")
        self.data.addData("hi", "Other")
        self.otherData = []
    
    def __str__(self):
        return self.telemetryStr
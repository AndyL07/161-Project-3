# File Name: <Telemetry.py>
# Date: <11/2/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

from Timer import Timer

class Telemetry():
    capText = "------------------------------\n"
    
    def __init__(self, timer=Timer()):
        self.runTime = timer
        self.telemetryStr = self.capText
        self.add(self.runTime.currTime(), "Current Time")
    
    def add(self, value, label=''):
        if type(value) is str:
            self.telemetryStr += value + "\n"
        else:
            self.telemetryStr += str(label) + f": {value:2.3f}" + "\n"
            
    def reset(self):
        self.telemetryStr = self.capText
        self.add(self.runTime.currTime(), "Current Time")
    
    def __str__(self):
        return self.telemetryStr
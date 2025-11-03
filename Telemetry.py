# File Name: <Telemetry.py>
# Date: <11/2/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

class Telemetry():
    capText = "------------------------------\n"
    
    def __init__(self):
        self.telemetry = self.capText
    
    def add(self, value, label=' '):
        if type(value) is str:
            self.telemetry += value + "\n"
        else:
            self.telemetry += str(label) + f": {value:2.3f}" + "\n"
            
    def reset(self):
        self.telemetry = self.capText
    
    def __str__(self):
        return self.telemetry
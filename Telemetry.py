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
    
    def add(self, label, value):
        if type(value) is str:
            self.telemetry += str(label) + ": " + value + "\n"
        else:
            self.telemetry += str(label) + f": {value:2.3f}" + "\n"
    
    def __str__(self):
        return self.telemetry
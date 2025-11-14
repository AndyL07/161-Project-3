# File Name: <Data_Collection.py>
# Date: <11/3/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

import pandas as pd

class DataCollection():
    def __init__(self):
        time = pd.Series([])
        
        xAccel = pd.Series([])
        yAccel = pd.Series([])
        zAccel = pd.Series([])
        
        xGyro = pd.Series([])
        yGyro = pd.Series([])
        zGyro = pd.Series([])
        
        xMag = pd.Series([])
        yMag = pd.Series([])
        zMag = pd.Series([])
        
        self.df = {
            "Time":time,
            
            "xAccel":xAccel,
            "yAccel":yAccel,
            "zAccel":zAccel,
            
            "xGyro":xGyro,
            "yGyro":yGyro,
            "zGyro":zGyro,
            
            "xMag":xMag,
            "yMag":yMag,
            "zMag":zMag
        }
        
    def addData(self, value, label):
        self.df[label].append([value])
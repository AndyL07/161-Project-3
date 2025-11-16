# File Name: <Data_Collection.py>
# Date: <11/13/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

import pandas as pd
import openpyxl

class DataCollection():
    def __init__(self):
        self.time = []
        self.other = []
        
        self.xAccel = []
        self.yAccel = []
        self.zAccel = []
        self.accelStren = []
        
        self.xGyro = []
        self.yGyro = []
        self.zGyro = []
        self.gyroStren = []
        
        self.xMag = []
        self.yMag = []
        self.zMag = []
        self.magStren = []
        
        self.data = {
            "Time":self.time,
            "Other":self.other,
            
            "xAccel":self.xAccel,
            "yAccel":self.yAccel,
            "zAccel":self.zAccel,
            "accelStren":self.accelStren,
            
            "xGyro":self.xGyro,
            "yGyro":self.yGyro,
            "zGyro":self.zGyro,
            "gyroStren":self.gyroStren,
            
            "xMag":self.xMag,
            "yMag":self.yMag,
            "zMag":self.zMag,
            "magStren":self.magStren
        }
        
    def addData(self, value, label):
        self.data[label].append(value)
        
    def toExcel(self):
        df = pd.read_excel("Pi_Data.xlsx", "Working Sheet", engine='openpyxl')
        
        self.timeSeries = pd.Series(self.time)
        self.otherSeries = pd.Series(self.other)
        
        self.xAccelSeries = pd.Series(self.xAccel)
        self.yAccelSeries = pd.Series(self.yAccel)
        self.zAccelSeries = pd.Series(self.zAccel)
        self.accelStrenSeries = pd.Series(self.accelStren)
        
        self.xGyroSeries = pd.Series(self.xGyro)
        self.yGyroSeries = pd.Series(self.yGyro)
        self.zGyroSeries = pd.Series(self.zGyro)
        self.gyroStrenSeries = pd.Series(self.gyroStren)
        
        self.xMagSeries = pd.Series(self.xMag)
        self.yMagSeries = pd.Series(self.yMag)
        self.zMagSeries = pd.Series(self.zMag)
        self.magStrenSeries = pd.Series(self.magStren)
        
        df["Index"] = df["Index"]
        
        df["Time"] = self.timeSeries
        df["Other"] = self.timeSeries
        
        df["xAccel"] = self.xAccelSeries
        df["yAccel"] = self.yAccelSeries
        df["zAccel"] = self.zAccelSeries
        df["accelStren"] = self.accelStrenSeries
        
        df["xGyro"] = self.xGyroSeries
        df["yGyro"] = self.yGyroSeries
        df["zGyro"] = self.zGyroSeries
        df["gyroStren"] = self.gyroStrenSeries
        
        df["xMag"] = self.xMagSeries
        df["yMag"] = self.yMagSeries
        df["zMag"] = self.zMagSeries
        df["magStren"] = self.magStrenSeries
        
        print(df.describe())
        
        df.to_excel("Pi_Data.xlsx", sheet_name="Working Sheet", engine='openpyxl')
        
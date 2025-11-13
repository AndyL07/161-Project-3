# File Name: <Timer.py>
# Date: <11/3/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

import time

class Timer():
    def __init__(self, flag=0.0):
        self.startTime = time.perf_counter()
        self.flagTime = flag
        
    def currTime(self):
        return time.perf_counter() - self.startTime
    
    def setFlag(self, newFlag):
        self.flagTime = newFlag
        
    def reset(self):
        self.startTime = time.perf_counter()
    
    def flagReached(self):
        return self.currTime() > self.flagTime
    
    def __str__(self):
        return f"Start Time: {self.startTime:2.3f} - Current Time: {self.currTime():2.3f}"
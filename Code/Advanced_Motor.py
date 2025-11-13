# File Name: <Advanced_Motor.py>
# Date: <11/13/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

from buildhat import Motor
from Telemetry import Telemetry
from Timer import Timer
#import time

class AdvMotor(Motor):
    def __init__(self, port):
        super.__init__(port)
        self.runTimer
        
    def runForTime(self, speed, time):
        self.runTimer = Timer(time)
        if self.runTimer.flagReached():
            super.pwm(0)
        else:
            super.pwm(speed)
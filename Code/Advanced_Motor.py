# File Name: <Advanced_Motor.py>
# Date: <11/13/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

from buildhat import Motor
# from Telemetry import Telemetry
# from Timer import Timer
#import time

class AdvMotor(Motor):
    def __init__(self, port, direction='forward'):
        super.__init__(port)
        self.direction = direction
        self.speedChange = 1
        if self.direction == 'reversed':
            self.speedChange = -1
        
    def runToPos(self, targetPos, speed):
        realPos = super.get_apostition()
        
        speed *= (targetPos - realPos) / 360
        if speed < 0.1:
            speed = 0.1
        elif speed > 1:
            speed = 1
            
        self.pwm(speed)
    
    def pwm(self, speed):
        super.pwm(speed * self.speedChange)
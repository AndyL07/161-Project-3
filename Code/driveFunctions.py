#from Advanced_Motor import AdvMotor
from buildhat import Motor
#from Telemetry import Telemetry
from Timer import Timer
#import time

SWEEP_TIME = 0.45
SWEEP_FORWARD_TIME = 0.35

class Drive:
    def __init__(self, telObj, prints=False):
        self.tel = telObj
        
        self.print = prints
        self.leftMotor = Motor('A')
        self.rightMotor = Motor('B')
        
        self.sweeping = 0
        self.sweepTimer = Timer(SWEEP_TIME)
        self.sweepForwardTimer = Timer(SWEEP_FORWARD_TIME)

    def turnLeft(self, angle, power):
        self.leftMotor.stop()
        self.rightMotor.run_for_degrees(angle, speed=power, blocking=False)
        self.tel.add("Turning Left")
        if self.print:
            print(self.tel)
            self.tel.reset()
            
    def goLeft(self, speed):
        self.leftMotor.pwm(-speed)
        self.rightMotor.pwm(-speed)
        self.tel.add("Going Left")
        if self.print:
            print(self.tel)
            self.tel.reset()

    def turnRight(self, angle, power):
        self.rightMotor.stop()
        self.leftMotor.run_for_degrees(angle, speed=-power, blocking=False)
        self.tel.add("Turning Right")
        if self.print:
            print(self.tel)
            self.tel.reset()
            
    def goRight(self, speed):
        self.leftMotor.pwm(speed)
        self.rightMotor.pwm(speed)
        self.tel.add("Going Right")
        if self.print:
            print(self.tel)
            self.tel.reset()
        
    def goStraight(self, speed, resetCase=True):
        self.leftMotor.pwm(speed)
        self.rightMotor.pwm(-speed)
        self.tel.add("Going Straight")
        if resetCase:
            self.sweeping = 0
        if self.print:
            print(self.tel)
            self.tel.reset()
        
    def goGeneralBack(self, speed):
        self.leftMotor.pwm(1.4 * speed)
        self.rightMotor.pwm(-1.4 * speed)
        self.tel.add("Going Back")
        if self.print:
            print(self.tel)
            self.tel.reset()
        
    def sweep(self, speed):
#         self.tel.add(self.sweeping, "Case")
        match self.sweeping:
            case 0:
                self.sweepForwardTimer.reset()
                self.sweepTimer.reset()
                self.sweepTimer.setFlag(SWEEP_TIME)
                self.sweeping = 2
                self.tel.add("Initial Case")
            case 1:
                self.goStraight(speed, False)
                self.tel.add("Sweeping Forward")
#                 self.tel.add(self.sweepForwardTimer.currTime(), "Forward Time")
                
                if self.sweepForwardTimer.flagReached():
                    self.sweepTimer.reset()
                    self.sweepTimer.setFlag(SWEEP_TIME)
                    self.sweeping = 2
            case 2:
                self.goRight(speed)
                self.tel.add("Sweeping Right - 1st")
#                 self.tel.add(self.sweepTimer.getFlag(), "Timer Flag")
                
                if self.sweepTimer.flagReached():
                    self.sweepTimer.reset()
                    self.sweepTimer.setFlag(SWEEP_TIME * 2)
                    self.sweeping = 3
            case 3:
                self.goLeft(speed)
                self.tel.add("Sweeping Left")
#                 self.tel.add(self.sweepTimer.getFlag(), "Timer Flag")
                
                if self.sweepTimer.flagReached():
                    self.sweepTimer.reset()
                    self.sweepTimer.setFlag(SWEEP_TIME)
                    self.sweeping = 4
            case 4:
                self.goRight(speed)
                self.tel.add("Sweeping Right - 2nd")
#                 self.tel.add(self.sweepTimer.getFlag(), "Timer Flag")
                
                if self.sweepTimer.flagReached():
                    self.sweepForwardTimer.reset()
                    self.sweeping = 1
        if self.print:
            print(self.tel)
            self.tel.reset()
            
    def goSmartStriaght(self, speed, difference, resetCase=True):
        self.leftMotor.pwm(speed + difference)
        self.rightMotor.pwm(-(speed - difference))
        self.tel.add("Going Smart Straight")
        if resetCase:
            self.sweeping = 0
        if self.print:
            print(self.tel)
            self.tel.reset()
        
        
    def stop(self):
        self.leftMotor.pwm(0)
        self.rightMotor.pwm(0)
        self.tel.add("Stopping")
        if self.print:
            print(self.tel)
        self.tel.reset()
        
    def gofast(self, speed):
        self.leftMotor.pwm(2 * speed)
        self.rightMotor.pwm(2 * speed)
        self.tel.add("Going Fast")
        if self.print:
            print(self.tel)
            self.tel.reset()
    
